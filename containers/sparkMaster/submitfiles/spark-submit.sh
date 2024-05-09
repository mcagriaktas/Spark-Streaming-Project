#!/bin/bash
docker exec spark-master spark-submit --master spark://spark-master:7077 --packages io.delta:delta-core_2.12:2.4.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 /opt/submitfiles/"$@"
