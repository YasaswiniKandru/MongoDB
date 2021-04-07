from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]
i_no = db.orders.find({"ONO":1024},{"ITEMS":1,"_id": 0} )
total =0
for i in i_no:
    for j in range(0,len(i["ITEMS"])):
        price = list(db.parts.find({"PNO":int(i["ITEMS"][j]["PARTNUMBER"])},{"PRICE":1,"_id": 0} ))
        total += price[0]["PRICE"] * i["ITEMS"][j]["QUANTITY"]
print(total)