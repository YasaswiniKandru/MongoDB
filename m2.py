from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]
p_no = list(db.parts.find({"PRICE" : {"$lt" : 15}}, {"PNO":1, "_id": 0}))
for p in p_no:
    taken = list(db.orders.aggregate([{ "$match": {"ITEMS.PARTNUMBER" : int(p["PNO"])}},
                                 {"$project":{"TAKENBY":1, "_id": 0}}
    ]))
result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in taken)]
emp=[]
for t in result:
    x = list(db.employees.aggregate([
        {"$match":{"ENO": int(t["TAKENBY"])}},
        {"$project" : {"ENAME":1, "CITY":1, "_id": 0}}
    ]))
    emp.append(x[0])
for e in emp:
    print(e)
