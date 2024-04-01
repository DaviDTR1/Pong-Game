from tabla import Tabla
from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = Tabla(1)
player2 = Tabla(0)
pong = Ball()
score = Scoreboard()
screen.update()
p1_score = 0
p2_score = 0
p2_col = False
p1_col = False
game_on = True

screen.listen()
while game_on:
    
    
    screen.onkeypress(key="w",fun=player1.move_forward)
    screen.onkeypress(key="s",fun=player1.move_backward)
    
    screen.onkeypress(key="Up",fun=player2.move_forward)
    screen.onkeypress(key="Down",fun=player2.move_backward)
    
    score.act_score(p1_score,p2_score)
    pong.move()
    touch = 0
    goal = False
    
    i = player1.tabla
    if pong.xcor() <= -360 and pong.ycor() > i.ycor()-50 and pong.ycor() < i.ycor()+50 and p1_col==False:
        if pong.heading() < 180:
            touch = 1
        else:
            touch = 2
        p1_col = True
        p2_col = False
            
    i =  player2.tabla
    if pong.xcor() >= 360 and pong.ycor() > i.ycor()-50 and pong.ycor() < i.ycor()+50  and p2_col==False:
        if pong.heading() < 90:
            touch = 2
        else:
            touch = 1
        p2_col = True
        p1_col = False
        
    if (pong.ycor() < -280 and pong.heading() < 360 and pong.heading() > 180): 
        if pong.heading() > 270:
            touch = 2
        else:
            touch = 1
    if (pong.ycor() > 280 and pong.heading() > 0 and pong.heading() < 180):
        if pong.heading() > 90:
            touch = 2
        else:
            touch = 1
    
    if pong.xcor() < -400:
        goal = True
        p2_score += 1
        
    if pong.xcor() > 400:
        goal = True
        p1_score += 1
        
    
    pong.collision(touch)
    if goal:
        pong.goal()
        p1_col = False
        p2_col = False
        
    screen.update()
    time.sleep(0.03)


screen.exitonclick()