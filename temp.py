import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()
for value in sql.execute("SELECT login, password, raiting FROM users"):
    login, pas, raiting = list(value)
    print(login, pas, raiting)
