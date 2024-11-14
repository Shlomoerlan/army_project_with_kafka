from toolz import pipe

from app.db.database_mongo import explosive_collection
from app.service.producers_service.all_messages_producer import publish_all_message
from app.service.producers_service.explosive_producer import publish_explosive
from app.service.producers_service.hostage_producer import publish_hostage
import re

def is_the_word_in(word, data):
    return any(word in d for d in data)

def selector(data):
    publish_all_message(data)
    if check_sentence_with_partial_word(data['sentences'], 'explos'):
        publish_explosive(data)
        print("explosive")
    elif is_the_word_in('hostage', data['sentences']):
        publish_hostage(data)
        print("hostage")
    else:
        print("else")

def check_sentence_with_partial_word(sentences, partial_word):
    return pipe(
        fr'\b{re.escape(partial_word)}\w*',
        lambda pattern: any(map(lambda sentence:
                                bool(re.search(pattern, sentence, re.IGNORECASE)), sentences)))

