from kafka import kafkaProducer
import json


KAFKA_BROKER = 'kafka:9092'
TOPIC_NAME = 'data_ingestion'

producer = kafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )


def send_message(data):
    producer.send(TOPIC_NAME, data)
    producer.flush()
    