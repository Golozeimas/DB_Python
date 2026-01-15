import sqlite3

conexao = sqlite3.connect("entretenimento.db")

cursor = conexao.cursor()

cursor.execute("UPDATE filmes SET nome_filme='The batman' WHERE nome_filme='Coringa'")

conexao.commit()

conexao.close()

print("Atualizado com sucesso!")