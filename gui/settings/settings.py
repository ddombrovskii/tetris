import tkinter
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Checkbutton, ttk, IntVar
import sqlite3


class Settings(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent, login):
        super().__init__(parent)

        self.login = login
        self.grid_checkbutton = IntVar()
        self.next_fig_checkbutton = IntVar()

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.back_delete)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(x=198.0, y=336.0, width=140.46551513671875, height=24.999969482421875)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.back_delete, relief="flat")
        self.button_2.place(x=48.0, y=336.0, width=121.0, height=25.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_3 clicked"), relief="flat")
        self.button_3.place(x=250.3937225341797, y=268.0, width=87.60626983642578, height=20.0)

        self.canvas.create_text(49.0, 269.0, anchor="nw", text="Выбор фона", fill="#FFFFFF", font=("Inter", 15 * -1))
        '''
        combobox_list = ["По времени", "По очкам", "Череда побед"]
        self.raiting_choose_combobox = ttk.Combobox(self, values=combobox_list)
        self.raiting_choose_combobox.place(x=48.0, y=234.0, width=290.0, height=18.0)

        self.canvas.create_text(52.0, 234.0, anchor="nw", text="По очкам", fill="#000000",
                                font=("Shrikhand Regular", 15 * -1))

        self.canvas.create_text(48.0, 210.0, anchor="nw", text="Выбор способа подсчёта результата", fill="#FFFFFF",
                                font=("Inter", 15 * -1))'''

        self.checkbutton_1 = Checkbutton(self, borderwidth=0, highlightthickness=0, relief="flat",
                                         variable=self.next_fig_checkbutton, command=self.next_fig_changed)
        self.checkbutton_1.place(x=319.0, y=181.0, width=19.0, height=19.0)

        self.canvas.create_text(48.0, 178.0, anchor="nw", text="Показ следующей фигуры", fill="#FFFFFF",
                                font=("Inter", 20 * -1))

        self.checkbutton_2 = Checkbutton(self, borderwidth=0, highlightthickness=0, relief="flat",
                                         variable=self.grid_checkbutton, command=self.grid_changed)
        self.checkbutton_2.place(x=319.0, y=154.0, width=19.0, height=19.0)

        self.canvas.create_text(48.0, 151.0, anchor="nw", text="Показ сетки ", fill="#FFFFFF", font=("Inter", 20 * -1))

        self.canvas.create_text(67.0, 47.0, anchor="nw", text="НАСТРОЙКИ", fill="#FFFFFF",
                                font=("Inter Black", 38 * -1))
        self.resizable(False, False)

    def load_next_fig(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_update_query = """UPDATE users SET next_fig = ? WHERE login = ?"""
        data = (self.next_fig_checkbutton.get(), self.login)
        sql.execute(sql_update_query, data)
        db.commit()
        sql.close()

    def next_fig_changed(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_update_query = """UPDATE users SET next_fig = ? WHERE login = ?"""
        data = (self.next_fig_checkbutton.get(), self.login)
        sql.execute(sql_update_query, data)
        db.commit()
        sql.close()

    def grid_changed(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_update_query = """UPDATE users SET grid = ? WHERE login = ?"""
        data = (self.grid_checkbutton.get(), self.login)
        sql.execute(sql_update_query, data)
        db.commit()
        sql.close()

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()
