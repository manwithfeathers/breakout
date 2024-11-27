from blocks import Block
from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import Scoreboard
import time

#this is where we store the "blocks" so we can check if the ball has hit them
blocklist = []
ballslist =[]
playing = True

#set up screen
s = Screen()
s.setup(width=800, height = 600)
s.bgcolor("black")
s.tracer(0)
s.title("BREAKOUT")

def fill_row(y):
    """fills row with blocks"""
    for x in range(-370, 390, 60):
        block = Block(x, y)
        blocklist.append(block)

def collision_checker(x , y):
    """check if ball hits walls or paddle"""
    if ball.distance(paddle) < 40 or y > 290:
        ball.returned()
    elif x < -380 or x > 380:
        ball.bounce()
    elif y < -300:
        ball.refresh()
        lives_board.update_score(-1)


for y in range(250, 100, -30):
    fill_row(y)

#initialise paddle
paddle = Paddle()

lives_board = Scoreboard(type="lives", x= -250,y= 250)
lives_board.score = 10
scores_board = Scoreboard(type = "score",x= 40,y= 250)
scores_board.score = 0

number_of_balls = int(s.textinput("BALLS", "Choose number of balls"))

for _ in range(number_of_balls):
    ball = Ball()
    ballslist.append(ball)



while playing is True:

    for ball in ballslist:
        ball.move()
        x = ball.xcor()
        y = ball.ycor()
        collision_checker(x, y)
        for block in blocklist:

            if ball.distance(block) < 20:
                block.destroy()
                blocklist.remove(block)
                scores_board.update_score(1)
                ball.returned()





    time.sleep(0.1)

    s.listen()
    s.onkey(paddle.move_left, "Left")
    s.onkey(paddle.move_right,  "Right")
    if lives_board.score <= 0:
        scores_board.game_over()
        playing = False
    elif not blocklist:
        scores_board.win()
        playing = False



    s.update()

s.exitonclick()