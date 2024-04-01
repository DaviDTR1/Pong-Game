from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self)->None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,-280)
        self.pendown()
        self.goto(0,270)
    
    def act_score(self, p1, p2):
        self.clear()
        self.penup()
        self.goto(0,-280)
        self.pendown()
        self.goto(0,270)
        self.write(f"{p1}     {p2}",False,"center",("Courier",20,"normal"))
        