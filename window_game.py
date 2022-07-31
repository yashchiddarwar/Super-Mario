from tkinter import *
from turtle import *



class Window:
   
    def __init__(self):

        SCREEN_DIMENSION = 1000,600         # Screen Dimension
    
        
        # Defining height and width
        width1 = SCREEN_DIMENSION[0]
        height1 = SCREEN_DIMENSION[1]
        
        # Creating screen and set limits to screen
        root = Tk()
        root.maxsize(SCREEN_DIMENSION[0], SCREEN_DIMENSION[1])
        root.minsize(SCREEN_DIMENSION[0], SCREEN_DIMENSION[1])
        
        self.canvas = Canvas(root, height = height1, width = width1)
        self.canvas.pack()

        # Embbed turtle with tkinter
        self.screen = TurtleScreen(self.canvas)
        #self.turtle = RawTurtle(self.canvas)

        #self.turtle.speed(50)
        #self.turtle.setpos(-500 , -100)

        # Spliting Screen
        #self.sky = Frame(bg = "SKYBLUE", width = SCREEN_DIMENSION[0], height = SCREEN_DIMENSION[1]*0.8)
        #self.sky.place(x = 0, y = 0)
        
        #self.ground = Frame(bg = "BROWN", width = SCREEN_DIMENSION[0], height = SCREEN_DIMENSION[1]*0.2)
        #self.ground.place(x = 0, y = SCREEN_DIMENSION[1]*0.8)


        
Window()
