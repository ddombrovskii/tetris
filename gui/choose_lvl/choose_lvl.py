from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Listbox, Variable
import sqlite3
import gameplay


class ChooseLvl(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent, login):
        super().__init__(parent)
        self.parent = parent
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")
        self.protocol("WM_DELETE_WINDOW", self.back_delete)
        self.login = login

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.back_delete, relief="flat")
        self.button_1.place(x=23.0, y=361.0, width=60.0, height=25.0)

        list_var = self.get_lvls_list()
        self.lvls_listbox = Listbox(self, listvariable=Variable(value=list_var), selectmode="single")
        self.lvls_listbox.bind('<<ListboxSelect>>', self.game_open)
        self.lvls_listbox.place(x=25.0, y=114.0, width=340.0, height=200.0)

        self.canvas.create_text(42.0, 50.0, anchor="nw", text="Выберите уровень сложности", fill="#000000",
                                font=("Inter Bold", 20 * -1))
        self.resizable(False, False)

    @staticmethod
    def get_lvls_list():
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        lvls_list = []
        for value in sql.execute("SELECT * FROM lvls"):
            try:
                lvls_list.append(value[0])
            except ValueError:
                print('empty string in db')

        return lvls_list

    def game_open(self, event):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_query = """SELECT * FROM lvls WHERE name = ?"""
        lvl_name = self.lvls_listbox.get(self.lvls_listbox.curselection())
        sql.execute(sql_query, (lvl_name,))
        lvl_name, lvl_width, lvl_height, lvl_speed = sql.fetchall()[0]

        points = gameplay.main(self.login, lvl_width, lvl_height, lvl_speed)

        print(self.login, ': ', points, sep='')

        sql_select_query = """SELECT * FROM users WHERE login = ?"""
        data = (self.login,)
        sql.execute(sql_select_query, data)
        rating = sql.fetchall()[0][2]
        if rating < points:
            sql_update_query = """UPDATE users SET raiting = ? WHERE login = ?"""
            data = (points, self.login)
            sql.execute(sql_update_query, data)
            db.commit()
        sql.close()

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()
