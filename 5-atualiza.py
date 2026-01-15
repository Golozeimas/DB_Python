import sqlite3

conexao = sqlite3.connect("entretenimento.db")

cursor = conexao.cursor()

# vamos fazer diferente e utilizar o input pra atualizar os dados
# você pode fazer utilizando a mesma função execute
id = 2
nome_do_novo_filme = input("Digite o nome do novo filme: \n")
cursor.execute("UPDATE filmes SET nome_filme=? WHERE id=? ", (nome_do_novo_filme, id))

conexao.commit()

conexao.close()

print("Atualizado com sucesso!")