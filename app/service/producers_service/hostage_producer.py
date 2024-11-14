import os
from dotenv import load_dotenv
from app.service.producers_service import producer


load_dotenv(verbose=True)

def publish_hostage(data):
    producer.send(os.environ['TOPIC_HOSTAGE_NAMES'], data)
    producer.flush()
    print("Processing hostage message")

def field_the_data(data):
    danger_sen = [index for index, s in enumerate(data['sentences']) if 'hostage' in s]
    print(f"get the data: {danger_sen}")
    if danger_sen:
        d = data.pop(danger_sen[0])
        data['sentences'].insert(0, d)
    return data