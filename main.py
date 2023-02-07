from sensor.configuration.mongo_db_connection_ import MongoDBClient



if __name__=="__main__":
    MongoDBClient = MongoDBClient()
    print("collection_name:",mongodb_client.database.list_collection_names())