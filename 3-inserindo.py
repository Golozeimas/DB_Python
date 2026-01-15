import sqlite3

# 1 - conectando no banco de dados
conexao = sqlite3.connect("entretenimento.db")

# 2 - inicializar o cursor
cursor = conexao.cursor()

# 3 - query de inserção de dados
cursor.execute(
            """
            INSERT INTO  filmes(nome_filme, ano_filme, nota_filme)
            VALUES ('Sonic', 2020, 8)
            """
)

# 4 - processa a query
conexao.commit()

# 5 - fecha a conexão
conexao.close()

print("Inserção de dados com sucesso!")
