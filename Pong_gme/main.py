from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key='Up')
screen.onkeypress(fun=r_paddle.move_down, key='Down')
screen.onkeypress(fun=l_paddle.move_up, key='w')
screen.onkeypress(fun=l_paddle.move_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Collision with paddles
    elif ball.xcor() > 320 and ball.distance(r_paddle) < 50 or \
            ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Collision with right wall
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Collision with left wall
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    scoreboard.update_scoreboard()

screen.exitonclick()
