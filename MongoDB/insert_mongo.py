from pymongo import MongoClient

clients = MongoClient()

mydb = clients.dbposts # serve para criar a conexao com o Mongo DB
mycol = mydb.posts # serve para fazer execução de operações, como inserção aqui

post1 ={
    "Nome":"Lucas",
    "Idade":19,
    "Profissao":{
        "Salario":"1200",
        "Tem vale?":False
    }
}

result = mycol.insert_one(post1)

print("Documento inserido com sucesso!")
