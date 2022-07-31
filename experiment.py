from tkinter import *
from turtle import *

print("hello world")

root = Tk()
canvas = Canvas(root)
canvas.pack()

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
