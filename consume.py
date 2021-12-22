from kafka import KafkaConsumer
from kafka.structs import OffsetAndMetadata
from kafka.structs import TopicPartition

# bootstrap = "localhost:29092"
bootstrap = "kafka-dev-01.arepa.appier.info:9092"

consumer = KafkaConsumer(
    bootstrap_servers=bootstrap,
    enable_auto_commit=False
)
partition_0 = TopicPartition('example', 0)
offset = 1
consumer.assign([partition_0, ])
consumer.seek(partition_0, offset)

for message in consumer:
    print(message)
