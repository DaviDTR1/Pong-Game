import random
from turtle import Turtle

DIRECT = [60,-60,240,-240]

class Ball(Turtle):
    def __init__(self) ->None:
        super().__init__()
        self.vel = 12
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.penup()
        self.setheading(random.choice(DIRECT))
        
    def move(self):
        self.forward(self.vel)
    
    def collision(self,direct):
        if direct == 1:
            self.setheading(self.heading()-random.randint(90,95))
        if direct == 2:
            self.setheading(self.heading()+random.randint(90,95))
        if direct != 0:
            self.vel += 0.5
    
    def goal(self,):
        self.goto(0,0)
        self.vel = 15
        self.setheading(random.choice(DIRECT))
        
    def camb_vel(self, point):
        self.vel = self.vel + point