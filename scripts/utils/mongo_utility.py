from pymongo import MongoClient


class MongoUtility:
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db = db_name
        self.collection = collection_name

    def get_client(self):
        return MongoClient(self.uri)

    def get_db(self):
        client = self.get_client()
        return client[self.db]

    def get_collection(self):
        db = self.get_db()
        return db[self.collection]

    def get_all_documents(self):
        collection = self.get_collection()
        return list(collection.find())

    def get_document_by_id(self, id):
        collection = self.get_collection()
        return collection.find_one({"_id": id})

    def insert_document(self, document):
        collection = self.get_collection()
        return str(collection.insert_one(document).inserted_id)

    def update_document(self, query:dict, document:dict):
        collection = self.get_collection()
        collection.update_one(query, {"$set": document})

    def delete_document(self, query: dict):
        collection = self.get_collection()
        collection.delete_one(query)

    def delete_all_documents(self):
        collection = self.get_collection()
        collection.delete_many({})

    def get_documents_by_query(self, query:dict):
        collection = self.get_collection()
        return collection.find(query)

    def push_to_array(self, query, field, value):
        collection = self.get_collection()
        collection.update_one(query, {"$push": {field: value}})

    def pull_from_array(self, query, field, value):
        collection = self.get_collection()
        collection.update_one(query, {"$pull": {field: value}})

    def get_by_aggregation(self, pipelines: list):
        collection = self.get_collection()
        return collection.aggregate(pipelines)