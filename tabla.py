from turtle import Turtle

class Tabla(Turtle):
    def __init__(self, side) -> None:
        pos = 0
        if side == 1:
            pos = -380 
        else:
            pos = 380
        n_bloque = Turtle()
        n_bloque.color("white")
        n_bloque.speed("normal")
        n_bloque.shape("square")
        n_bloque.penup()
        n_bloque.goto(pos,0)
        n_bloque.shapesize(stretch_wid=5,stretch_len=1)
        self.tabla = n_bloque
        
    def move_backward(self):
        if self.tabla.ycor() > -240:
            self.tabla.goto(self.tabla.xcor(),self.tabla.ycor()-20)
    
    def move_forward(self):
        if self.tabla.ycor() < 240:
            self.tabla.goto(self.tabla.xcor(),self.tabla.ycor()+20)