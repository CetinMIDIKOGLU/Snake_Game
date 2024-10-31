from turtle import Turtle
from snake import Snake
ALIGNMENT = "center"
FONT= ("Arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
     
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
       
        
   
        

        
        
        
    