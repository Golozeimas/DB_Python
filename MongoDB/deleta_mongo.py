from pymongo import MongoClient

client = MongoClient()

my_db = client.dbposts

my_col = my_db.posts

delete = {"Nome":"Lucas"}

x = my_col.delete_one(delete) # geralmente usamos o one nesses casos

print(f"{x.deleted_count} Documento(s) excluído(s)")
