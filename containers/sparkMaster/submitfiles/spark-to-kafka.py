from pyspark.sql import SparkSession
from confluent_kafka.admin import (AdminClient, NewTopic)
from config import config

spark = SparkSession.builder \
    .appName("InsertParquetToHDFS") \
    .master("local[*]") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .getOrCreate()


def topic_exists(admin, topic):
    metadata = admin.list_topics()
    for t in iter(metadata.topics.values()):
        if t.topic == topic:
            return True
    return False

def create_topic(admin, topic):
    new_topic = NewTopic(topic)
    admin.create_topics([new_topic])

topic_name = "emine"

#config = {'bootstrap.servers': 'localhost:9092,localhost:9292,localhost:9392'}
admin = AdminClient(config)

if topic_exists(admin=admin, topic=topic_name):
    print("Topic exists")
else:
    print("Topic not exist")
    create_topic(admin=admin, topic=topic_name)
    print(topic_name, "topic has been created")
