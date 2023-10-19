import findspark
findspark.init("/opt/spark/")

from pyspark.sql import functions as F
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

### ----------------------------- ETL ----------------------------- ###
### --------------------------------------------------------------- ###

from ETL_Helper import ETL_Helper

kafka_information = {
    "kafka.bootstrap.servers": "kafka:9092",
    "subscribe": "test1"
}

db_properties_dict = {
      "user": "myuser",
      "password": "mypassword",
      "table": "project_test",
      "mode": "append",
      "ip": "postgresql",
      "port": "5432",
      "db": "mydb",
      "streaming output": "file:///tmp/streaming/project_telemetry"
}

etl_helper = ETL_Helper(kafka_information, db_properties_dict)

### ----------------------------- Extract ------------------------- ###
### --------------------------------------------------------------- ###

df = etl_helper.Extract()


### ---------------------------- Transfrom ------------------------ ###
### --------------------------------------------------------------- ###

df = etl_helper.Transfrom(df)


### ------------------------------ Load --------------------------- ###
### --------------------------------------------------------------- ###

etl_helper.Load(df)


### --------------------------------------------------------------- ###
### --------------------------------------------------------------- ###