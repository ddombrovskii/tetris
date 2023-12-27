from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel


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
                          command=lambda: print("button_2 clicked"), relief="flat")
        self.button_2.place(x=315.0, y=366.0, width=67.0, height=23.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_3 clicked"), relief="flat")
        self.button_3.place(x=142.0, y=276.0, width=107.0, height=25.0)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_4 clicked"), relief="flat")
        self.button_4.place(x=142.0, y=237.0, width=107.0, height=25.0)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_5 clicked"), relief="flat")
        self.button_5.place(x=142.0, y=198.0, width=107.0, height=25.0)

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_6 clicked"), relief="flat")
        self.button_6.place(x=142.0, y=159.0, width=107.0, height=25.0)

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(self, image=self.button_image_7, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_7 clicked"), relief="flat")
        self.button_7.place(x=142.0, y=120.0, width=107.0, height=25.0)

        self.canvas.create_text(22.0, 45.0, anchor="nw", text="Выберите уровень сложности для настройки", fill="#FFFFFF",
                           font=("Inter Bold", 15 * -1))
        self.resizable(False, False)

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

