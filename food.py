from turtle import Turtle,Screen
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x_cor=random.randint(-280, 280)
        y_cor=random.randint(-280, 280)
        self.goto(x_cor,y_cor)
       
    

        
        
    





