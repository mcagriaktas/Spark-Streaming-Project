import findspark
findspark.init("/opt/spark")

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import *

class ETL_Helper:
    def __init__(self, kafka_information, db_properties_dict):

        self.kafka_information = kafka_information

        self.db_properties_dict = db_properties_dict

        self.spark = SparkSession.builder \
            .appName("Read From Kafka") \
            .config("spark.sql.streaming.stateStore.stateSchemaCheck", "false").getOrCreate()

        self.spark.sparkContext.setLogLevel('ERROR')

    def Extract(self):
        df = (self.spark
              .readStream
              .format("kafka")
              .option("kafka.bootstrap.servers", self.kafka_information["kafka.bootstrap.servers"])
              .option("subscribe", self.kafka_information["subscribe"])
              .load())

        df = df.createOrReplaceTempView("table")
        df = self.spark.sql("""
            SELECT CAST(key AS STRING) as keys, CAST(value AS STRING) as values
            FROM table
        """)

        return df

    def Transfrom(self, df):
        df = df.withColumn("values", split(col("values"), ","))
        df = df.select(
            "keys",
            df.values[0].cast(DoubleType()).alias("timestamp"),
            df.values[1].cast(StringType()).alias("device"),
            df.values[2].cast(DoubleType()).alias("co"),
            df.values[3].cast(DoubleType()).alias("humidity"),
            df.values[4].cast(BooleanType()).alias("light"),
            df.values[5].cast(DoubleType()).alias("lpg"),
            df.values[6].cast(BooleanType()).alias("motion"),
            df.values[7].cast(DoubleType()).alias("smoke"),
            df.values[8].cast(DoubleType()).alias("temp")
        )

        df = df.withColumn("event_time", from_unixtime(col("timestamp")).cast("timestamp"))

        df = df.createOrReplaceTempView("table2")
        df = self.spark.sql("""
            SELECT event_time, device, co, humidity, light, lpg, motion, smoke, temp
            FROM table2
        """)

        df.printSchema()

        return df

    def Load(self, df):
        def write_to_multi_sinks(df, batchId):
            df.persist()
            df.show()

            db_properties = {
                "user": self.db_properties_dict["user"],
                "password": self.db_properties_dict["password"],
                "driver": "org.postgresql.Driver"
            }

            df.write.jdbc(
                url=f"jdbc:postgresql://{self.db_properties_dict['ip']}:{self.db_properties_dict['port']}/{self.db_properties_dict['db']}",
                table=self.db_properties_dict['table'],
                mode=self.db_properties_dict['mode'],
                properties=db_properties)

        
        streamingQuery = (df
                          .writeStream
                          .foreachBatch(write_to_multi_sinks)
                          .option("checkpointLocation", self.db_properties_dict["streaming output"])
                          .start())

        streamingQuery.awaitTermination()