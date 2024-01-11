from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Listbox, Variable
from gui.make_lvls.make_lvls import NewLvl, EditLvl
import sqlite3


class Lvls(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.back_delete)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                          command=self.back_delete, relief="flat")
        self.button_1.place(x=22.0, y=364.0, width=60.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                          command=self.make_new_lvl, relief="flat")
        self.button_2.place(x=315.0, y=366.0, width=67.0, height=23.0)

        list_var = self.get_lvls_list()
        self.lvls_listbox = Listbox(self, listvariable=Variable(value=list_var), selectmode="single")
        self.lvls_listbox.bind('<<ListboxSelect>>', self.open_edit_lvl)
        self.lvls_listbox.place(x=25.0, y=114.0, width=340.0, height=200.0)

        self.canvas.create_text(22.0, 45.0, anchor="nw", text="Выберите уровень сложности для настройки", fill="#000000",
                           font=("Inter Bold", 15 * -1))
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

    def make_new_lvl(self):
        self.withdraw()
        settings = NewLvl(self)
        settings.grab_set()

    def open_edit_lvl(self, event):
        self.withdraw()
        settings = EditLvl(self, self.lvls_listbox.get(self.lvls_listbox.curselection()))
        settings.grab_set()

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

