from post_connect import conn
cursor_obj = conn.cursor()

id = 4

cursor_obj.execute(f"DELETE FROM games WHERE id={id}")

conn.commit()

print("Apagado com sucesso")

conn.close()