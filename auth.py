import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()


def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Название', message=info_str)

    # error point
    # messagebox.showerror(title='', message='Error!')


root['bg'] = '#D9D9D9'
photo = tkinter.PhotoImage(file='T2.png')
root.iconphoto(False, photo)
root.title("Auth")
# root.wm_attributes('-alpha', 0.7)
root.geometry("800x600")

root.resizable(width=False, height=False)

canvas = Canvas(root, width=800, height=600)
canvas.pack()

frame = Frame(root, bg='#C0C0C0')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

reg = Button(frame, text="регистрация", bg='white', font=40, command=btn_click)
reg.pack(side=BOTTOM)
title = Label(frame, text='XDD', bg='#D9D9D9', font=40)
title.pack(pady=40)

passField = Entry(frame, bg='white', show='*')
passField.pack(side=BOTTOM)
loginInput = Entry(frame, bg='white')
loginInput.pack(side=BOTTOM, pady=10)

root.mainloop()
