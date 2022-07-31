from tkinter import *
from turtle import *



root = Tk()
canvas = Canvas(root)
canvas.pack()

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
