from pymongo import MongoClient
mongo_client = MongoClient('mongodb://172.19.10.104:27017')
db = mongo_client['army']
all_messages_collection = db['all_messages']
explosive_collection = db['explosive']
