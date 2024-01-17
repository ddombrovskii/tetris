from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Checkbutton, IntVar
import sqlite3


class FigureMaker(Toplevel):
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
                               command=self.add_figure, relief="flat")
        self.button_1.place(x=295.0, y=366.0, width=78.0, height=25.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=self.back_delete, relief="flat")
        self.button_3.place(x=15.0, y=366.0, width=60.0, height=25.0)

        self.c_0_0 = IntVar()
        self.c_0_1 = IntVar()
        self.c_0_2 = IntVar()
        self.c_0_3 = IntVar()
        self.c_0_4 = IntVar()
        self.c_1_0 = IntVar()
        self.c_1_1 = IntVar()
        self.c_1_2 = IntVar()
        self.c_1_3 = IntVar()
        self.c_1_4 = IntVar()
        self.c_2_0 = IntVar()
        self.c_2_1 = IntVar()
        self.c_2_2 = IntVar()
        self.c_2_3 = IntVar()
        self.c_2_4 = IntVar()
        self.c_3_0 = IntVar()
        self.c_3_1 = IntVar()
        self.c_3_2 = IntVar()
        self.c_3_3 = IntVar()
        self.c_3_4 = IntVar()
        self.c_4_0 = IntVar()
        self.c_4_1 = IntVar()
        self.c_4_2 = IntVar()
        self.c_4_3 = IntVar()
        self.c_4_4 = IntVar()

        self.checkbutton_0_0 = Checkbutton(self, variable=self.c_0_0)
        self.checkbutton_0_0.place(x=101.0, y=95.0, width=50, height=50)

        self.checkbutton_0_1 = Checkbutton(self, variable=self.c_0_1)
        self.checkbutton_0_1.place(x=101.0, y=145.0, width=50, height=50)

        self.checkbutton_0_2 = Checkbutton(self, variable=self.c_0_2)
        self.checkbutton_0_2.place(x=101.0, y=195.0, width=50, height=50)

        self.checkbutton_0_3 = Checkbutton(self, variable=self.c_0_3)
        self.checkbutton_0_3.place(x=101.0, y=245.0, width=50, height=50)

        self.checkbutton_0_4 = Checkbutton(self, variable=self.c_0_4)
        self.checkbutton_0_4.place(x=101.0, y=295.0, width=50, height=50)

        self.checkbutton_1_0 = Checkbutton(self, variable=self.c_1_0)
        self.checkbutton_1_0.place(x=151.0, y=95.0, width=50, height=50)

        self.checkbutton_1_1 = Checkbutton(self, variable=self.c_1_1)
        self.checkbutton_1_1.place(x=151.0, y=145.0, width=50, height=50)

        self.checkbutton_1_2 = Checkbutton(self, variable=self.c_1_2)
        self.checkbutton_1_2.place(x=151.0, y=195.0, width=50, height=50)

        self.checkbutton_1_3 = Checkbutton(self, variable=self.c_1_3)
        self.checkbutton_1_3.place(x=151.0, y=245.0, width=50, height=50)

        self.checkbutton_1_4 = Checkbutton(self, variable=self.c_1_4)
        self.checkbutton_1_4.place(x=151.0, y=295.0, width=50, height=50)

        self.checkbutton_2_0 = Checkbutton(self, variable=self.c_2_0)
        self.checkbutton_2_0.place(x=201.0, y=95.0, width=50, height=50)

        self.checkbutton_2_1 = Checkbutton(self, variable=self.c_2_1)
        self.checkbutton_2_1.place(x=201.0, y=145.0, width=50, height=50)

        self.checkbutton_2_2 = Checkbutton(self, variable=self.c_2_2)
        self.checkbutton_2_2.place(x=201.0, y=195.0, width=50, height=50)

        self.checkbutton_2_3 = Checkbutton(self, variable=self.c_2_3)
        self.checkbutton_2_3.place(x=201.0, y=245.0, width=50, height=50)

        self.checkbutton_2_4 = Checkbutton(self, variable=self.c_2_4)
        self.checkbutton_2_4.place(x=201.0, y=295.0, width=50, height=50)

        self.checkbutton_3_0 = Checkbutton(self, variable=self.c_3_0)
        self.checkbutton_3_0.place(x=251.0, y=95.0, width=50, height=50)

        self.checkbutton_3_1 = Checkbutton(self, variable=self.c_3_1)
        self.checkbutton_3_1.place(x=251.0, y=145.0, width=50, height=50)

        self.checkbutton_3_2 = Checkbutton(self, variable=self.c_3_2)
        self.checkbutton_3_2.place(x=251.0, y=195.0, width=50, height=50)

        self.checkbutton_3_3 = Checkbutton(self, variable=self.c_3_3)
        self.checkbutton_3_3.place(x=251.0, y=245.0, width=50, height=50)

        self.checkbutton_3_4 = Checkbutton(self, variable=self.c_3_4)
        self.checkbutton_3_4.place(x=251.0, y=295.0, width=50, height=50)

        self.checkbutton_4_0 = Checkbutton(self, variable=self.c_4_0)
        self.checkbutton_4_0.place(x=301.0, y=95.0, width=50, height=50)

        self.checkbutton_4_1 = Checkbutton(self, variable=self.c_4_1)
        self.checkbutton_4_1.place(x=301.0, y=145.0, width=50, height=50)

        self.checkbutton_4_2 = Checkbutton(self, variable=self.c_4_2)
        self.checkbutton_4_2.place(x=301.0, y=195.0, width=50, height=50)

        self.checkbutton_4_3 = Checkbutton(self, variable=self.c_4_3)
        self.checkbutton_4_3.place(x=301.0, y=245.0, width=50, height=50)

        self.checkbutton_4_4 = Checkbutton(self, variable=self.c_4_4)
        self.checkbutton_4_4.place(x=301.0, y=295.0, width=50, height=50)

        self.canvas.create_text(96.0, 40.0, anchor="nw", text="Конструктор фигур", fill="#000000",
                                font=("Inter Bold", 20 * -1))
        self.resizable(False, False)
        self.mainloop()

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()

    def get_figure_list(self):
        binary_list = [[self.c_0_0.get(), self.c_1_0.get(), self.c_2_0.get(), self.c_3_0.get(), self.c_4_0.get()],
                       [self.c_0_1.get(), self.c_1_1.get(), self.c_2_1.get(), self.c_3_1.get(), self.c_4_1.get()],
                       [self.c_0_2.get(), self.c_1_2.get(), self.c_2_2.get(), self.c_3_2.get(), self.c_4_2.get()],
                       [self.c_0_3.get(), self.c_1_3.get(), self.c_2_3.get(), self.c_3_3.get(), self.c_4_3.get()],
                       [self.c_0_4.get(), self.c_1_4.get(), self.c_2_4.get(), self.c_3_4.get(), self.c_4_4.get()]]

        # letter_list = []
        row = ''
        for i in range(5):
            for j in range(5):
                if binary_list[i][j] == 1:
                    row += 'x'
                else:
                    row += 'o'
            row += ' '

        return row

    def add_figure(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS figures(figure_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        data TEXT);""")

        sql.execute("""INSERT INTO figures(data) VALUES(?);""", (str(self.get_figure_list()),))
        db.commit()
        sql.close()
        self.parent.deiconify()
        self.destroy()
