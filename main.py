import random
from tkinter import *
# -----------------------------Global Variables-------------------------------------- #


cH = 700
cW = 1000

size = 1
currX, currY = 0,0
colour = 'black'


# -----------------------------Command Functions-------------------------------------- #


def locate_mouse(event):
    global currX,currY
    currX, currY = event.x, event.y
    drawing.create_oval((currX, currY, currX, currY), width=size, fill=colour, outline=colour)


def add_line(event):
    global currX, currY
    drawing.create_oval((currX, currY, currX, currY), width=size, fill=colour, outline=colour)
    currX, currY = event.x, event.y


def show_colour(new_colour):
    global colour
    colour = new_colour


def scale_used(value):
    global size
    size = value


def erase_all():
    drawing.delete("all")


def erase():
    global colour
    colour = "white"


# -----------------------------Drawing Canvas-------------------------------------- #
painting = Tk()

painting.title("Painting")
painting.state("zoomed")
painting.config()

painting.rowconfigure(0, weight=1)
painting.columnconfigure(0, weight=1)

drawing = Canvas(painting, bg='white', highlightthickness=0)
drawing.grid(row=0, column=0)
drawing.config(height=cH,width=cW)

drawing.bind("<Button-1>", locate_mouse)
drawing.bind("<B1-Motion>", add_line)

# -----------------------------Colour Chooser Buttons-------------------------------------- #
colours = ["black", "gray", "brown4", "red", "orange", "yellow", "green", "purple", "blue"]

btn = Button(height=1, width=2, bg="black", command=lambda: show_colour("black"))
btn.place(x=15, y=10)

btn = Button(height=1, width=2, bg="gray", command=lambda: show_colour("gray"))
btn.place(x=15, y=40)

btn = Button(height=1, width=2, bg="brown4", command=lambda: show_colour("brown4"))
btn.place(x=15, y=70)

btn = Button(height=1, width=2, bg="red", command=lambda: show_colour("red"))
btn.place(x=15, y=100)

btn = Button(height=1, width=2, bg="orange", command=lambda: show_colour("orange"))
btn.place(x=15, y=130)

btn = Button(height=1, width=2, bg="yellow", command=lambda: show_colour("yellow"))
btn.place(x=15, y=160)

btn = Button(height=1, width=2, bg="green", command=lambda: show_colour("green"))
btn.place(x=15, y=190)

btn = Button(height=1, width=2, bg="purple", command=lambda: show_colour("purple"))
btn.place(x=15, y=220)

btn = Button(height=1, width=2, bg="blue", command=lambda: show_colour("blue"))
btn.place(x=15, y=250)
# -----------------------------Erasers-------------------------------------- #
erase_all_photo = PhotoImage(file="erase_all.png").subsample(6, 6)
erase_all = Button(height=19, width=19, image=erase_all_photo, command=erase_all)
erase_all.place(x=15, y=280)

eraser_photo = PhotoImage(file="eraser.png").subsample(50,50)
eraser = Button(height=19, width=19, image=eraser_photo, command=erase)
eraser.place(x=15, y=310)

# -----------------------------Brush Scale Slider-------------------------------------- #
scale = Scale(from_=1, to=20, command=scale_used)
scale.place(x=10, y=340)

painting.mainloop()

