import turtle as tl
import tkinter as tk
from window_game import Window as window


class Player:

    def __init__(self, canvas):
        self.leg = self.Leg(canvas)


    def Leg(self, canvas):
        #  Create Leg_l and Leg_R their shape and size
        self.screen = tl.TurtleScreen(canvas)
        self.leg_L = tl.RawTurtle(canvas)
        self.leg_L.ht()
        self.leg_L.penup()
        self.leg_L.shape('square')
        self.leg_L.turtlesize(2, 0.5)
        
        self.leg_R = tl.RawTurtle(canvas)
        self.leg_R.ht()
        self.leg_R.penup()
        self.leg_R.shape('square')
        self.leg_R.turtlesize(2, 0.5)

        # Placing Legs
        self.leg_L.speed(40)
        self.leg_L.setpos(-480, -100)
        self.leg_L.st()
        
        self.leg_R.speed(40)
        self.leg_R.setpos(-460, -100)
        self.leg_R.st()

        
    def Body(self):
        pass


    def Head(self):
        pass



canvas = window()
Player(canvas.canvas)
