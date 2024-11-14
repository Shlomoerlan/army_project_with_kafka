import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.utils.createing_models import insert_user_data

load_dotenv(verbose=True)


def process_to_sql(data):
    print(f"Processing: {data}")
    insert_user_data(data, 'h')


def consume_hostage():
    consumer = KafkaConsumer(
        os.environ['TOPIC_HOSTAGE_NAMES'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for msg in consumer:
        process_to_sql(msg.value)


if __name__ == '__main__':
    consume_hostage()
