from app.db.database_mongo import all_messages_collection


def insert_data_to_mongo(data):
    success = all_messages_collection.insert_one(data)
    return success