from tkinter import *
import random

root = Tk()
root.geometry("700x450")

label1 = Label(root, font = ("times", 100))

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label1.config(text = f'{random.choice(number)}')
    label1.pack()

button = Button(root, text = "Roll", command = roll)
button.place(x = 350, y = 400)

root.mainloop()
