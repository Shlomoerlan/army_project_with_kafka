import os
from dotenv import load_dotenv
from app.service.producers_service import producer


load_dotenv(verbose=True)

def publish_hostage(data):
    producer.send(os.environ['TOPIC_HOSTAGE_NAMES'], data)
    producer.flush()
    print("Processing hostage message")

