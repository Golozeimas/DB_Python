import sqlite3

conexao = sqlite3.connect("entretenimento.db")

cursor = conexao.cursor()

# query para selecionar todas as colunas da tabela 'filmes'
tabela_filmes = cursor.execute("SELECT * FROM filmes")

# fetchall -> retorna a consulta do select no caso como tabela completa aqui
print(tabela_filmes.fetchall())