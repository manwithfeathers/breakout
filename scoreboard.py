from turtle import Turtle

FONT = ("courier new", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        self.penup()
        self.color("white")
        self.score = 0
        self.setpos(x, y)
        self.hideturtle()
        self.write(f"{self.type}: {self.score}", font=FONT)

    def update_score(self, points):
        self.clear()
        self.score += points
        self.write(f"{self.type}: {self.score}", font=FONT)

    def game_over(self):
        self.setpos(-250,0)
        self.write(f"GAME OVER! FINAL SCORE {self.score}", font= FONT)

    def win(self):
        self.setpos(-250, 0)
        self.write(f"YOU WON! FINAL SCORE {self.score}", font=FONT)

    def setscore(self, score):
        self.score = score
        self.clear()
        self.write(f"{self.type}: {self.score}", font=FONT)

