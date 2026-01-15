import sqlite3

conexao = sqlite3.connect("entretenimento.db")

cursor = conexao.cursor()

cursor.execute("DELETE FROM filmes WHERE nota_filme < 9 ")

conexao.commit()

conexao.close()

print("Dados excluídos com sucesso!")