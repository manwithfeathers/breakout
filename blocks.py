from turtle import Turtle

class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.setpos(x, y)


    def destroy(self):
        self.hideturtle()







