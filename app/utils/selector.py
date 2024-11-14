from app.db.database_mongo import explosive_collection
from app.service.producers_service.all_messages_producer import publish_all_message
from app.service.producers_service.explosive_producer import publish_explosive
from app.service.producers_service.hostage_producer import publish_hostage


def is_the_word_in(word, data):
    return any(word in d for d in data)

def selector(data):
    publish_all_message(data)
    publish_hostage(data)
    explosive_collection.insert_one(data)
    if is_the_word_in('explos', data['sentences']):
        publish_explosive(data)
    elif is_the_word_in('hostage', data['sentences']):
        publish_hostage(data)
