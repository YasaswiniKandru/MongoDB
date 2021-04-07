from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]
emps = db.employees.find({})
orders = db.orders.find({})
final={}


for o in orders:
        total = 0
        for j in range(0,len(o["ITEMS"])):
            price = list(db.parts.find({"PNO":int(o["ITEMS"][j]["PARTNUMBER"])},{"PRICE":1,"_id": 0} ))
            total += price[0]["PRICE"] * o["ITEMS"][j]["QUANTITY"]
        if o["TAKENBY"] in final:
            final[o["TAKENBY"]] += total
        else:
            final[o["TAKENBY"]] = total

for e in emps:
    if e["ENO"] not in final.keys():
        final[e["ENO"]] = 0
print(final)