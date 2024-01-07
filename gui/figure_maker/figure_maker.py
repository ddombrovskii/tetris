
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("391x402")
window.configure(bg = "#D9D9D9")


canvas = Canvas(
    window,
    bg = "#D9D9D9",
    height = 402,
    width = 391,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=295.0,
    y=366.0,
    width=78.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=165.0,
    y=366.0,
    width=114.0,
    height=25.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=15.0,
    y=366.0,
    width=60.0,
    height=25.0
)

canvas.create_rectangle(
    245.0,
    251.0,
    295.0,
    301.0,
    fill="#FF9191",
    outline="")

canvas.create_rectangle(
    195.0,
    251.0,
    245.0,
    301.0,
    fill="#FF9191",
    outline="")

canvas.create_rectangle(
    145.0,
    251.0,
    195.0,
    301.0,
    fill="#FF9191",
    outline="")

canvas.create_rectangle(
    95.0,
    251.0,
    145.0,
    301.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    245.0,
    201.0,
    295.0,
    251.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    195.0,
    201.0,
    245.0,
    251.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    145.0,
    201.0,
    195.0,
    251.0,
    fill="#FF9191",
    outline="")

canvas.create_rectangle(
    95.0,
    201.0,
    145.0,
    251.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    245.0,
    151.0,
    295.0,
    201.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    195.0,
    151.0,
    245.0,
    201.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    145.0,
    151.0,
    195.0,
    201.0,
    fill="#FF9191",
    outline="")

canvas.create_rectangle(
    95.0,
    151.0,
    145.0,
    201.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    245.0,
    101.0,
    295.0,
    151.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    195.0,
    101.0,
    245.0,
    151.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    145.0,
    101.0,
    195.0,
    151.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    95.0,
    101.0,
    145.0,
    151.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    96.0,
    40.0,
    anchor="nw",
    text="Конструктор фигур",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()