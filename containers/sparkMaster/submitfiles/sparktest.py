from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("InsertParquetToHDFS") \
    .master("local[*]") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .getOrCreate()


df = spark.read.parquet("/opt/submitfiles/datasets/onlineretail")

df.show()

df.write.format("parquet").mode("overwrite").save("hdfs://172.20.0.5:9000/data")

spark.stop()


