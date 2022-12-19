
from pymongo import MongoClient
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc={
    'a':20,
    'b':30

}
db.shop.insert_one(doc)
print(20)