import sqlite3

conexao = sqlite3.connect("entretenimento.db")

cursor = conexao.cursor()

# query para selecionar todas as colunas da tabela 'filmes'
tabela_filmes = cursor.execute("SELECT * FROM filmes")

# fetchall -> retorna a consulta do select no caso como tabela completa aqui
dados_de_filmes = tabela_filmes.fetchall()

for dados in dados_de_filmes:
    id, nome, ano, nota = dados
    print(f"Esse é o nome do filme: {nome}")