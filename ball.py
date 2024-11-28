from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setpos(random.randint(-100, 100), random.randint(-100, 100))
        self.ballspeed = 5
        self.speed("fastest")

        self.x_move = -20
        self.y_move = -20

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    def returned(self):
        self.y_move *= -1

    def refresh(self):
        self.setpos(random.randint(-100, 100), random.randint(-100, 100))

    def destroy(self):
        self.hideturtle()


