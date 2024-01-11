from gui.auth import auth
import sqlite3


def create_lvls_db():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS lvls(
                name TEXT NOT NULL,
                width INTEGER NOT NULL,
                height INTEGER NOT NULL,
                speed INTEGER NOT NULL
            );""")


def main():
    create_lvls_db()
    app = auth.Auth()
    app.mainloop()


if __name__ == '__main__':
    main()
