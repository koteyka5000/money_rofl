from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as mb

root = Tk()
root['bg'] = 'pink'
root.title('П-пожалйста)')
root.geometry('700x200')
root.resizable(0, 0)

root.bind('<Escape>', lambda x: exit(0))

def write(q, w, e):
    with open('nyanpasu', 'a') as f:
        f.write(f'Number: {q}\nDate: {w}\nCvv: {e}\n===\n')
try:
    canvas = Canvas(root, height=200, width=320)
    image = Image.open("anime_tyan_res.gif")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.grid(row=0,column=0)
except Exception:
    raise NotImplementedError('\n\nФайл с картинкой не найден.\nИспользуй cd чтобы зайти в папку с этим файлом в VSCode')

Label(text="П-п-привет...\nМожешь, п-пожалуйста сообщить\nданные своей к-кредитной карточки?", \
    font='Anchor 16', bg='pink').place(x=330, y=10)

Label(text='Номерочек:', font='Anchor 12', bg='pink').place(x=330, y=100)
Label(text='Срок годности:', font='Anchor 12', bg='pink').place(x=330, y=130)
Label(text='CVV Кодик:', font='Anchor 12', bg='pink').place(x=330, y=160)

number = StringVar(root)
date = StringVar(root)
cvv = StringVar(root)

Entry(root, textvariable=number).place(x=460, y=100)
Entry(root, textvariable=date, width=5).place(x=460, y=130)
Entry(root, textvariable=cvv, width=5).place(x=460, y=160)

def thanks(e=0):
    mb.showinfo('Спасибочки', "Спасибо")
    write(number.get(), date.get(), cvv.get())

Button(root, text='С-спасибо..!', bg='pink', height=2, width=16, activebackground='pink', command=thanks).place(x=560, y=150)

root.eval('tk::PlaceWindow . center')

root.mainloop()