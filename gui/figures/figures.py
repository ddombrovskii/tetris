from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Button, Listbox, Variable
from gui.figure_maker.figure_maker import FigureMaker
import sqlite3


class Figures(Toplevel):
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
        self.button_1.place(x=23.0, y=364.0, width=60.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.open_maker, relief="flat")
        self.button_2.place(x=236.0, y=364.0, width=131.0, height=25.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=self.delete_figure, relief="flat")
        self.button_3.place(x=140.0, y=364.0, width=80.0, height=25.0)

        list_var = self.get_list_figures()
        self.figures_listbox = Listbox(self, listvariable=Variable(value=list_var), selectmode="single")
        self.figures_listbox.place(x=25.0, y=114.0, width=340.0, height=200.0)

        self.canvas.create_text(124.0, 33.0, anchor="nw", text="Список фигур", fill="#000000",
                                font=("Inter Bold", 20 * -1))
        self.resizable(False, False)

    @staticmethod
    def get_list_figures() -> list:
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute("""SELECT * FROM figures""")
        data = sql.fetchall()
        sql.close()

        return [f'Фигура {i[0]}' for i in data]

    def delete_figure(self):
        sel = self.figures_listbox.curselection()
        figure_id = self.figures_listbox.get(sel).split(' ')[-1]
        self.figures_listbox.delete(sel[0])

        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute("""DELETE FROM figures WHERE figure_id = ?""", (figure_id,))
        db.commit()
        sql.close()

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

    def open_maker(self):
        self.withdraw()
        figures = FigureMaker(self)
        figures.grab_set()
