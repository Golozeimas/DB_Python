from post_connect import conn

cursor_obj = conn.cursor()

games = [("The last of us part II", "Action", 2020, 10)]

for game in games:
    cursor_obj.execute("""
            INSERT INTO games(nome_jogo, genero, ano, nota) VALUES (%s,%s,%s,%s)
""",game)
    conn.commit()
    print("Adicionado com sucesso")
    conn.close()