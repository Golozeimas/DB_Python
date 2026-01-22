from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.dbposts

mycol = mydb.posts

old_value = {"Idade":21}

new_value = {"$set":{"Idade":22}}

mycol.update_one(old_value, new_value)

for x in mycol.find():
    pprint(x)