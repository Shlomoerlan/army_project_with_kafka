import json
import os
from dotenv import load_dotenv
from app.service.producers_service import producer
from app.utils.createing_models import json_serializer

load_dotenv(verbose=True)


def publish_all_message(data):
    producer.send(os.environ['TOPIC_MESSAGES_NAMES'], json.dumps(data, default=json_serializer).encode('utf-8'))
    producer.flush()
    print("Processing New all_message number")