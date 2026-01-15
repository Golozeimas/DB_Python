import sqlite3

# 1 -Conectando com o DB
conexao = sqlite3.connect("entretenimento.db")

# 2 - Uso do cursor para manipulacao do banco
cursor = conexao.cursor()

# 3 - Execução do SQL
cursor.execute("""
                CREATE TABLE filmes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_filme TEXT NOT NULL,
                ano_filme INTEGER NOT NULL,
                nota_filme REAL NOT NULL
               );
              """)

# 4 - Fecha a conexao
conexao.close()

print("Tabela foi criada com sucesso!")