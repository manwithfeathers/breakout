from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.setpos(-380, -280)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.paddlespeed = 30
        self.speed("fastest")

    def move_left(self):
        y = self.pos()[1]
        x = self.pos()[0]
        x -= self.paddlespeed
        self.setpos(x,y)

    def move_right(self):
        y = self.pos()[1]
        x = self.pos()[0]
        x += self.paddlespeed

        self.setpos(x, y)



