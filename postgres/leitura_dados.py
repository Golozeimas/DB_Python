from post_connect import conn

cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * FROM games")

games = cursor_obj.fetchall()

print(games)
