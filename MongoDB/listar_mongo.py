from pymongo import MongoClient
from pprint import pprint # biblioteca pra deixar o JSON mais bonito

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

result = mycol.find() # já procura todos em JSON

for r in result:
    pprint(r)