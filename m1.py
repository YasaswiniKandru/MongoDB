from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
filter = {"CNO": 1111}
db=client["moDB"]
collection = db["parts"]
cursor = collection.find({"PRICE" : {"$lt" : 20}})
for each_doc in cursor:
    print(each_doc["PNAME"])
