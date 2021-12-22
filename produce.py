from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import sys


def send(d, topic, it):
    # Asynchronous by default
    future = producer.send(topic, value=d)

    if it % 1000 == 0:
        # Block for 'synchronous' sends
        try:
            record_metadata = future.get(timeout=60)
        except KafkaError:
            # Decide what to do if produce request failed...
            print("error")
            pass
        else:
            # Successful result returns assigned partition and offset
            print("topic", record_metadata.topic)
            print("partition", record_metadata.partition)
            print("offset", record_metadata.offset)


# bootstrap = "localhost:29092"
bootstrap = "kafka-dev-01.arepa.appier.info:9092"
topic = sys.argv[1]
print(topic)

producer = KafkaProducer(
    bootstrap_servers=bootstrap,
    linger_ms=5,
    batch_size=5000,
)

with open("./impbid_rtb_2021122001.json", "r") as f:
    for i, l in enumerate(f):
        d = json.dumps(json.loads(l)).encode()
        send(d, topic, i)
        if i > 50000:
            break

