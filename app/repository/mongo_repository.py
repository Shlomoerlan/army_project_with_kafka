from app.db.database_mongo import all_details_collection


def insert_data_to_mongo(data):
    success = all_details_collection.insert_one(data)
    return success
