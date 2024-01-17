import sys
from pathlib import Path
import sqlite3

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from gui.settings.settings import Settings
from gui.raiting.raiting import Raiting
from gui.about_devs.about_devs import AboutDevs
from gui.choose_lvl.choose_lvl import ChooseLvl
import os


class Gamer(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent, login):
        super().__init__(parent)
        self.login = login
        self.about_url = os.path.realpath('./about/index.html')

        self.geometry("391x402")
        self.configure(bg="#D9D9D9")
        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.exit, relief="flat")
        self.button_1.place(x=130.0, y=312.0, width=130.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.about_dev_open, relief="flat")
        self.button_2.place(x=130.0, y=279.0, width=130.0, height=25.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=lambda url=self.about_url: self.open_url(url), relief="flat")
        self.button_3.place(x=130.0, y=246.0, width=130.0, height=25.0)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                               command=self.raiting_open, relief="flat")
        self.button_4.place(x=130.0, y=213.0, width=130.0, height=25.0)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0,
                               command=self.settings_open, relief="flat")
        self.button_5.place(x=130.0, y=180.0, width=130.0, height=25.0)

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0,
                               command=self.game_open, relief="flat")
        self.button_6.place(x=130.0, y=147.0, width=130.0, height=25.0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(194.0, 69.0, image=self.image_image_1)
        self.resizable(False, False)

    def game_open(self):
        self.withdraw()
        settings = ChooseLvl(self, self.login)
        settings.grab_set()

    def settings_open(self):
        self.withdraw()
        settings = Settings(self, self.login)
        settings.grab_set()

    def raiting_open(self):
        self.withdraw()
        raiting = Raiting(self)
        raiting.grab_set()

    def about_dev_open(self):
        self.withdraw()
        about = AboutDevs(self)
        about.grab_set()

    def open_url(self, url):
        os.system(f"start {url}")

    @staticmethod
    def exit():
        sys.exit(0)


if __name__ == '__main__':
    Gamer().mainloop()
