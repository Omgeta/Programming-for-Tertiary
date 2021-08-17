import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client["DB"]
coll = db["COLL"]

doc = {
    "Name": "Test",
    "Age": 1
}
coll.insert_one(doc)
coll.insert_many([doc, doc])

coll.find_one({"Name": "Test"})
coll.find({"Age": 1})
coll.find({})

coll.update_one({"Name": "Test"}, {"$set": {"Name": "Test2"}})

coll.delete_one({"Name": "Test"})
