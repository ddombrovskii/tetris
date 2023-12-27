from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel


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

        self.canvas = Canvas(
            self,
            bg="#D9D9D9",
            height=402,
            width=391,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_delete,
            relief="flat"
        )
        self.button_1.place(
            x=23.0,
            y=364.0,
            width=60.0,
            height=25.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=236.0,
            y=364.0,
            width=131.0,
            height=25.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=140.0,
            y=364.0,
            width=80.0,
            height=25.0
        )

        self.canvas.create_rectangle(
            23.0,
            71.0,
            368.0,
            341.0,
            fill="#7D7D7D",
            outline="")

        self.canvas.create_rectangle(
            302.0,
            278.0,
            352.0,
            328.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            236.0,
            278.0,
            286.0,
            328.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            170.0,
            278.0,
            220.0,
            328.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            104.0,
            278.0,
            154.0,
            328.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            38.0,
            278.0,
            88.0,
            328.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            302.0,
            213.0,
            352.0,
            263.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            236.0,
            213.0,
            286.0,
            263.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            170.0,
            213.0,
            220.0,
            263.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            104.0,
            213.0,
            154.0,
            263.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            38.0,
            213.0,
            88.0,
            263.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            302.0,
            148.0,
            352.0,
            198.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            236.0,
            148.0,
            286.0,
            198.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            195.0,
            173.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            104.0,
            148.0,
            154.0,
            198.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            104.0,
            148.0,
            154.0,
            198.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            129.0,
            173.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            63.0,
            173.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            327.0,
            108.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            261.0,
            108.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            195.0,
            108.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            129.0,
            108.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            63.0,
            108.0,
            image=self.image_image_8
        )

        self.canvas.create_text(
            124.0,
            33.0,
            anchor="nw",
            text="Список фигур",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )
        self.resizable(False, False)

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

