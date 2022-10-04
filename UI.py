# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 09/03/2022
# Description:

from tkinter import *
from time import *
from PIL import ImageTk, Image
top = Tk()
top.title("Welcome to Tristan's UI")
top.geometry('400x200')
canvas = Canvas(top, width = 300, height = 300)
canvas.pack()
global photo

def clicked():
    with open('prng-service.txt', 'w', encoding = 'utf-8') as f:
        f.write('run')
        sleep(1)
    while(True):
        sleep(1)
        with open('prng-service.txt', 'r') as f:
            num = f.readline()
        if num != 'run':
            with open('image-service.txt', 'w') as f:
                f.write(num)
                break
    while(True):

        sleep(1)
        with open('image-service.txt', 'r') as f:
            address = f.readline()

            if address[:2] == './':
                #img = Image.open(address)
               # img.show()
                #img = Image.open(address)
                photo = ImageTk.PhotoImage(Image.open(address))
                label = Label(canvas, image = photo)
                label.image = photo
                lbl.image = photo
                label.pack()
                canvas.create_image(20,20, anchor = 'nw', image = photo)
                canvas.image = photo
                break

lbl = Label(canvas, text = "PRNG")
lbl.pack()
button = Button(canvas, text = "Click me", fg = "green", command = clicked)
button.pack()
top.mainloop()
