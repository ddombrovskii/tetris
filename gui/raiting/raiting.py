from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Listbox, Variable
import sqlite3


class Raiting(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.back_delete)
        self.parent = parent
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.back_delete, relief="flat")
        self.button_1.place(x=142.0, y=360.0, width=107.0, height=25.0)

        self.canvas.create_text(24.0, 31.0, anchor="nw", text="Рейтинг по очкам ", fill="#FFFFFF",
                                font=("Inter Black", 38 * -1))

        db_list = self.get_db_list()
        db_list_var = Variable(value=db_list)
        self.raiting_listbox = Listbox(self, listvariable=db_list_var)
        self.raiting_listbox.place(x=25.0, y=114.0, width=340.0, height=200.0)
        self.resizable(False, False)

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

    @staticmethod
    def get_db_list():
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        db_list = []
        for value in sql.execute("SELECT login, password, raiting FROM users"):
            try:
                login, _, raiting = list(value)
                db_list.append(login + '_________________________________________________________' + str(raiting))
            except ValueError:
                print('empty string in db')

        return db_list

