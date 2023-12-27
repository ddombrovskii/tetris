import sqlite3

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, CENTER, Toplevel


class Registr(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.delete)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")
        self.title("Tetris")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.info_btn_img = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.info_btn = Button(self, image=self.info_btn_img, borderwidth=0, highlightthickness=0,
                          command=lambda: print("? clicked"),
                          relief="flat")
        self.info_btn.place(x=2.0, y=381.0, width=18.0, height=18.0)

        self.reg_img = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.reg_btn = Button(self, image=self.reg_img, borderwidth=0, highlightthickness=0, command=self.reg_btn_click,
                         relief="flat")
        self.reg_btn.place(x=162.0, y=344.0, width=157.0, height=27.0)
        '''
        enter_img = PhotoImage(file=relative_to_assets("button_3.png"))
        enter_btn = Button(image=enter_img, borderwidth=0, highlightthickness=0, command=enter_btn_click, relief="flat")
        enter_btn.place(x=73.0, y=344.0, width=69.0, height=27.0)'''

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(195.0, 322.0, image=self.entry_image_1)
        self.repeat_pass_entry = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.repeat_pass_entry.place(x=73.0, y=312.0, width=244.0, height=18.0)

        self.canvas.create_text(73.0, 294.0, anchor="nw", text="Повторите пароль", fill="#FFFFFF",
                                font=("Inter Bold", 14 * -1))

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(195.0, 284.0, image=self.entry_image_2)
        self.password_entry = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.password_entry.place(x=73.0, y=274.0, width=244.0, height=18.0)

        self.canvas.create_text(73.0, 256.0, anchor="nw", text="Пароль", fill="#FFFFFF", font=("Inter Bold", 14 * -1))

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(195.0, 246.0, image=self.entry_image_3)
        self.login_entry = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.login_entry.place(x=73.0, y=236.0, width=244.0, height=18.0)

        self.canvas.create_text(73.0, 218.0, anchor="nw", text="Логин", fill="#FFFFFF", font=("Inter Bold", 14 * -1))

        self.canvas.create_text(65.0, 166.0, anchor="nw", text="Для регистрации придумайте \nсвой  логин и пароль",
                                fill="#FFFFFF", font=("Arial", 20 * -1), justify=CENTER)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(195.0, 94.0, image=self.image_image_1)

        self.resizable(False, False)

    def delete(self):
        self.parent.deiconify()
        self.destroy()

    def reg_btn_click(self):
        print("btn_reg clicked")
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            password TEXT,
            raiting INTEGER
        )""")

        user_log = self.login_entry.get()
        user_pass = self.password_entry.get()
        user_repeat_pass = self.repeat_pass_entry.get()
        if not self.check_login_pass(user_log, user_pass, user_repeat_pass):
            return

        check = False
        for value in sql.execute("SELECT login, password, raiting FROM users"):
            login_from_sql, _, _ = list(value)
            if user_log == login_from_sql:
                check = True
                break

        if not check:
            sql.execute(f"INSERT INTO users VALUES (?, ?, 0)", (user_log, user_pass))
            db.commit()
            messagebox.showinfo(title='Успех', message='Регистрация прошла успешно')
            self.parent.deiconify()
            self.destroy()
        else:
            messagebox.showerror(title='Ошибка', message='Такой логин уже существует')

    @staticmethod
    def check_login_pass(login, password, repeat_password):
        result = False
        if password != repeat_password:
            messagebox.showerror(title='Ошибка', message='Пароли не совпадают!')
            result = False
        elif login == "admin" and password == "admin":
            messagebox.showerror(title='Ошибка', message='Недопустимое имя пользователя!')
            result = False
        else:
            result = True

        return result


if __name__ == '__main__':
    Registr().mainloop()
