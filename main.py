from blocks import Block
from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import Scoreboard
import time

#this is where we store the "blocks" and balls so we can check if the ball has hit them
blocklist = []
ballslist =[]

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

def collision_checker(ball, paddle, x , y):
    """check if ball hits walls or paddle"""
    if ball.distance(paddle) < 40 or y > 290:
        ball.returned()
    elif x < -380 or x > 380:
        ball.bounce()
    elif y < -300:
        ball.refresh()
        lives_board.update_score(-1)

# initialise paddle
p = Paddle()

#initialise scoreboards
lives_board = Scoreboard(type="lives", x=-250, y=250)
lives_board.score = 10
scores_board = Scoreboard(type="score", x=40, y=250)
scores_board.score = 0


def initialise():
    global ballslist
    global blocklist

    for ball in ballslist:
        ball.destroy()

    """ initialise everything"""

    blocklist = []
    ballslist = []

    for y in range(250, 100, -30):
        fill_row(y)

    number_of_balls = int(s.textinput("BALLS", "Choose number of balls"))
    difficulty = int(s.textinput("DIFFICULTY", "Choose difficulty level 1, 2 or 3"))

    for _ in range(number_of_balls):
        b = Ball()
        ballslist.append(b)

    if difficulty == 1:
        lives_board.score = 20
    elif difficulty == 2:
        lives_board.score = 10
    else:
        lives_board.score = 5


def breakout():

    for ball in ballslist:
        ball.move()
        x = ball.xcor()
        y = ball.ycor()
        collision_checker(ball, p, x, y)
        for block in blocklist:
            if ball.distance(block) < 20:
                block.destroy()
                blocklist.remove(block)
                scores_board.update_score(1)
                ball.returned()

    # if lives_board.score <= 0:
    #     scores_board.game_over()
    #     playing = False
    # elif not blocklist:
    #     scores_board.win()
    #     playing = False

    s.listen()
    s.onkey(p.move_left, "Left")
    s.onkey(p.move_right, "Right")
    time.sleep(0.1)
    s.update()
    return lives_board.score


initialise()

while True:
    life = breakout()
    if life <= 0:
        cont = s.textinput("CONTINUE", "Do you want to continue? (Y/N)")
        if cont == "n":
            s.bye()
            break
        else:
            initialise()
            continue


s.exitonclick()