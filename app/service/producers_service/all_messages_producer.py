import os
from dotenv import load_dotenv
from app.service.producers_service import producer

load_dotenv(verbose=True)


def publish_all_message(data):
    producer.send(os.environ['TOPIC_MESSAGES_NAMES'], data)
    producer.flush()
    print("Processing New all_message number")