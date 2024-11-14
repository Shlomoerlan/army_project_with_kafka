import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.database_psql import session_maker
from app.repository.mongo_repository import insert_data_to_mongo

load_dotenv(verbose=True)

def process_to_sql(data):
    print(f"Processing: {data}")
    with session_maker() as session:
        session.add(data)

def consume_explosive():
    consumer = KafkaConsumer(
        os.environ['TOPIC_MESSAGES_NAMES'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for msg in consumer:
        process_to_sql(msg.value)

if __name__ == '__main__':
    consume_membership()