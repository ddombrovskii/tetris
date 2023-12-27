from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from gui.figures.figures import Figures
from gui.lvls.lvls import Lvls
import sys


class Admin(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.back_exit, relief="flat")
        self.button_1.place(x=124.0, y=232.0, width=142.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.figures_open, relief="flat")
        self.button_2.place(x=124.0, y=199.0, width=142.0, height=25.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=self.lvls_open, relief="flat")
        self.button_3.place(x=124.0, y=166.0, width=142.0, height=25.0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(194.0, 69.0, image=self.image_image_1)

        self.resizable(False, False)

    @staticmethod
    def back_exit():
        sys.exit(0)

    def figures_open(self):
        self.withdraw()
        figures = Figures(self)
        figures.grab_set()

    def lvls_open(self):
        self.withdraw()
        lvls = Lvls(self)
        lvls.grab_set()
