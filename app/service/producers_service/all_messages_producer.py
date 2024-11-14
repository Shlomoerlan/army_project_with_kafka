import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

producer = KafkaProducer(
    bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_message(data):
    producer.send(os.environ['TOPIC_MESSAGES_NAMES'], data)
    producer.flush()
    print("Processing New message number")





