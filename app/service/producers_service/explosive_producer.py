import json
import os
from dotenv import load_dotenv
from flask import Flask

from app.service.producers_service import producer
from app.utils.createing_models import json_serializer

app = Flask(__name__)

load_dotenv(verbose=True)

def publish_explosive(data):
    data = field_the_data(data)
    producer.send(os.environ['TOPIC_EXPLOSIVE_NAMES'], json.dumps(data, default=json_serializer).encode('utf-8'))
    # producer.send(os.environ['TOPIC_EXPLOSIVE_NAMES'], data)
    producer.flush()
    print("Processing explosive message")

def field_the_data(data):
    danger_sen = [index for index, s in enumerate(data['sentences']) if 'explosive' in s]
    if danger_sen:
        d = data.pop(danger_sen[0])
        data['sentences'].insert(0, d)
    return data

