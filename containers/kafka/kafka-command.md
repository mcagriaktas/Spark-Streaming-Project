## CREATE
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic arzu --replication-factor 3 --partitions 3

## LIST
./kafka-topics.sh --bootstrap-server localhost:9092 --list

## PRODUCER
../kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic1

## CONSUMER
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic arzu --from-beginning

## DESCRIBE
./kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic medium_data

## DELETE
./kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic topic1

## UPGRADE (INCREASE)
./kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic topic1 --partitions 5 

## EXAMPLE
/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 \
--create --topic test1 \
--replication-factor 1 \
--partitions 3