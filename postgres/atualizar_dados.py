from post_connect import conn

cursor_obj = conn.cursor()

games = [("Red dead 2", "Action/Adventure", 2018, 10)]

id = 1

for game in games:
    cursor_obj.execute(f"UPDATE games SET nome_jogo=%s, genero=%s, ano=%s, nota = %s WHERE id={id}",game)
    conn.commit()
    print("Atualizado com sucesso")
    conn.close()
