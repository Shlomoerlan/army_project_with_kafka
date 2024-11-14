import os
from dotenv import load_dotenv
from flask import Flask
from app.service.producers_service import producer

app = Flask(__name__)

load_dotenv(verbose=True)

def publish_explosive(data):
    producer.send(os.environ['TOPIC_EXPLOSIVE_NAMES'], data)
    producer.flush()
    print("Processing explosive message")


