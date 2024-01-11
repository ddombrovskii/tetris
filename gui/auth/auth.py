import sqlite3
import gameplay

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from gui.registr.registr import Registr
from gui.gamer.gamer import Gamer
from gui.admin.admin import Admin


class Auth(Tk):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self):
        super().__init__()
        self.geometry("391x402")
        self.configure(bg="#C0C0C0")
        self.title("Tetris")

        self.canvas = Canvas(self, bg="#C0C0C0", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))

        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(x=2.0, y=381.0, width=18.0, height=18.0)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(195.0, 301.0, image=self.entry_image_1)
        self.password_entry = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, show='*')
        self.password_entry.place(x=73.0, y=291.0, width=244.0, height=18.0)

        self.canvas.create_text(73.0, 273.0, anchor="nw", text="Пароль", fill="#FFFFFF", font=("Inter Bold", 14 * -1))

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(195.0, 246.0, image=self.entry_image_2)
        self.login_entry = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=1)
        self.login_entry.place(x=73.0, y=236.0, width=244.0, height=18.0)

        self.canvas.create_text(73.0, 218.0, anchor="nw", text="Логин", fill="#FFFFFF", font=("Inter Bold", 14 * -1))

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.entry_open, relief="flat")
        self.button_2.place(x=284.0, y=343.0, width=67.0, height=26.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=self.guest_open, relief="flat")
        self.button_3.place(x=186.0, y=343.0, width=66.0, height=26.0)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                               command=self.registr_open, relief="flat")
        self.button_4.place(x=50.0, y=343.0, width=106.88349151611328, height=25.967741012573242)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(195.0, 94.0, image=self.image_image_1)

        self.canvas.create_text(108.0, 54.0, anchor="nw", text="TETRIS", fill="#FFFFFF", font=("Inter Black", 48 * -1))
        self.canvas.create_text(73.0, 174.0, anchor="nw", text="Введите логин и пароль", fill="#FFFFFF",
                                font=("Inter Bold", 20 * -1))

        self.resizable(False, False)

    def registr_open(self):
        self.withdraw()
        registr = Registr(self)
        registr.grab_set()

    @staticmethod
    def guest_open():
        gameplay.main('guest')

    def entry_open(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()

        user_login = self.login_entry.get()
        user_password = self.password_entry.get()

        if user_login == "admin" and user_password == "admin":
            self.withdraw()
            admin = Admin(self)
            admin.grab_set()
            return

        check = False
        db_login = ""
        db_password = ""
        try:
            for value in sql.execute("SELECT login, password, raiting, grid, next_fig, background FROM users"):
                try:
                    db_login, db_password, _, _, _, _ = list(value)
                    if db_login == user_login:
                        check = True
                        print(check)
                        break
                except ValueError:
                    print('empty string')
                    continue

        except sqlite3.OperationalError:
            print("empty table")
            return

        if check:
            if user_password != db_password:
                messagebox.showerror(title='Ошибка', message='Неправильный пароль!')
                return
        else:
            messagebox.showerror(title='Ошибка', message='Такого логина не существует! Зарегистрируйтесь.')
            return

        self.withdraw()
        gamer = Gamer(self, user_login)
        gamer.grab_set()


if __name__ == '__main__':
    app = Auth()
    app.mainloop()
