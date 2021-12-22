from kafka.admin import KafkaAdminClient, NewTopic

# bootstrap = "localhost:29092"
bootstrap = "kafka-dev-01.arepa.appier.info:9092"

client = KafkaAdminClient(
    bootstrap_servers=bootstrap,
    client_id="test",
)

client.create_topics(
    new_topics=[NewTopic(
        name="impbid_rtb_cmp",
        num_partitions=1,
        replication_factor=1
    )],
    validate_only=False

)
