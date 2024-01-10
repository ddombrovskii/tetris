from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel


class AboutDevs(Toplevel):
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
        self.title("Tetris")

        self.canvas = Canvas(self, bg="#D9D9D9", height=402, width=391, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(71.0, 11.0, anchor="nw", text="О разработчиках", fill="#000000",
                           font=("Inter Black", 28 * -1))

        self.canvas.create_text(18.0, 177.0, anchor="nw",
                           text="Разработчики:\n  Обучающиеся группы 6404-090301D:\n  Домбровский Данила Валерьевич\n  Быстров Михаил Артёмович\nРуководитель:\n  Зеленко Лариса Сергеевна\n\nСамарский университет им. С. П. Королёва, 2023 г.",
                           fill="#000000", font=("Inter", 14 * -1))

        self.canvas.create_text(18.0, 66.0, anchor="nw",
                           text="Лабораторный практикум по дисциплине:\n“Технологии программирования”\n\nТема: “Автоматизированная система \n«Игра «Тетрис» с функциями администратора»”",
                           fill="#000000", font=("Inter", 14 * -1))

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                          command=self.back_delete, relief="flat")
        self.button_1.place(x=142.0, y=339.0, width=107.0, height=25.0)
        self.resizable(False, False)

    def back_delete(self):
        self.parent.deiconify()
        self.destroy()


if __name__ == '__main__':
    AboutDevs().mainloop()
