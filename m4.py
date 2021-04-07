from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]
e_no = list(db.employees.find({"CITY":"Wichita"},{"ENO":1, "_id": 0} ))

for e in e_no:
    c_no = list(db.orders.find({"TAKENBY":int(e["ENO"])},{"CUSTOMER":1,"TAKENBY":1, "_id": 0} ))
c_no = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in c_no)]
c_name=[]
for c in c_no:
    c_name.append(list(db.customers.find({"CNO":int(c["CUSTOMER"])},{"CNAME":1, "_id": 0} )))
print(c_name)