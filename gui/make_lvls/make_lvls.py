from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Scale, IntVar, StringVar
import sqlite3


class NewLvl(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_button)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.name = StringVar(value="Новый уровень")
        self.speed = IntVar(value=10)
        self.height = IntVar(value=10)
        self.width = IntVar(value=10)

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.close_button, relief="flat")
        self.button_1.place(x=125.0, y=358.0, width=60.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.accept_button, relief="flat")
        self.button_2.place(x=198.0, y=358.0, width=140.46551513671875, height=24.999969482421875)

        self.speed_scale = Scale(self, orient="horizontal", length=100, from_=1, to=100, variable=self.speed)
        self.speed_scale.place(x=267.0, y=224.0)
        self.canvas.create_text(20.0, 230.0, anchor="nw", text="Скорость падения", fill="#000000",
                                font=("Inter", 20 * -1))

        self.height_scale = Scale(self, orient="horizontal", length=100, from_=18, to=30, variable=self.height)
        self.height_scale.place(x=267.0, y=189.0)
        self.canvas.create_text(20.0, 197.0, anchor="nw", text="Высота стакана", fill="#000000",
                                font=("Inter", 20 * -1))

        self.width_scale = Scale(self, orient="horizontal", length=100, from_=10, to=20, variable=self.width)
        self.width_scale.place(x=267.0, y=156.0)
        self.canvas.create_text(20.0, 164.0, anchor="nw", text="Длина стакана", fill="#000000", font=("Inter", 20 * -1))

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(250.5, 106.0, image=self.entry_image_1)
        self.entry_1 = Entry(self, textvariable=self.name, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=130.0, y=95.0, width=241.0, height=20.0)

        self.canvas.create_text(20.0, 93.0, anchor="nw", text="Название", fill="#000000", font=("Inter", 20 * -1))

        self.canvas.create_text(50.0, 42.0, anchor="nw", text="Настройка уровня сложности", fill="#000000",
                                font=("Inter Bold", 20 * -1))

        self.resizable(False, False)

    def close_button(self):
        self.parent.deiconify()
        self.destroy()

    def accept_button(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_query = """INSERT INTO lvls VALUES (?, ?, ?, ?)"""
        data = (self.name.get(), self.width.get(), self.height.get(), self.speed.get())
        sql.execute(sql_query, data)
        db.commit()
        sql.close()
        self.parent.deiconify()
        self.destroy()


class EditLvl(Toplevel):
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

        return ASSETS_PATH / Path(path)

    def __init__(self, parent, name):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_button)
        self.geometry("391x402")
        self.configure(bg="#D9D9D9")

        self.old_name = name
        self.name = StringVar(value=name)
        self.speed = IntVar(value=10)
        self.height = IntVar(value=10)
        self.width = IntVar(value=10)

        self.load_lvl_settings()

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                               command=self.close_button, relief="flat")
        self.button_1.place(x=125.0, y=358.0, width=60.0, height=25.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=self.accept_button, relief="flat")
        self.button_2.place(x=198.0, y=358.0, width=140.46551513671875, height=24.999969482421875)

        self.speed_scale = Scale(self, orient="horizontal", length=100, from_=1, to=100, variable=self.speed)
        self.speed_scale.place(x=267.0, y=224.0)
        self.canvas.create_text(20.0, 230.0, anchor="nw", text="Скорость падения", fill="#000000",
                                font=("Inter", 20 * -1))

        self.height_scale = Scale(self, orient="horizontal", length=100, from_=18, to=30, variable=self.height)
        self.height_scale.place(x=267.0, y=189.0)
        self.canvas.create_text(20.0, 197.0, anchor="nw", text="Высота стакана", fill="#000000",
                                font=("Inter", 20 * -1))

        self.width_scale = Scale(self, orient="horizontal", length=100, from_=10, to=20, variable=self.width)
        self.width_scale.place(x=267.0, y=156.0)
        self.canvas.create_text(20.0, 164.0, anchor="nw", text="Длина стакана", fill="#000000", font=("Inter", 20 * -1))

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(250.5, 106.0, image=self.entry_image_1)
        self.entry_1 = Entry(self, textvariable=self.name, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=130.0, y=95.0, width=241.0, height=20.0)

        self.canvas.create_text(20.0, 93.0, anchor="nw", text="Название", fill="#000000", font=("Inter", 20 * -1))

        self.canvas.create_text(50.0, 42.0, anchor="nw", text="Настройка уровня сложности", fill="#000000",
                                font=("Inter Bold", 20 * -1))

        self.resizable(False, False)

    def close_button(self):
        self.parent.deiconify()
        self.destroy()

    def load_lvl_settings(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_query = """SELECT * FROM lvls WHERE name = ?"""
        sql.execute(sql_query, (self.name.get(),))
        data = sql.fetchall()[0]
        self.width.set(data[1])
        self.height.set(data[2])
        self.speed.set(data[3])
        sql.close()

    def accept_button(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql_query = """UPDATE lvls SET name = ?, width = ?, height = ?, speed = ? WHERE name = ?"""
        data = (self.name.get(), self.width.get(), self.height.get(), self.speed.get(), self.old_name)
        sql.execute(sql_query, data)
        db.commit()
        sql.close()
        self.parent.deiconify()
        self.destroy()
