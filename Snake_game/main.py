from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True

screen.listen()
screen.onkeypress(snake.snake_up, 'Up')
screen.onkeypress(snake.snake_down, 'Down')
screen.onkeypress(snake.snake_left, 'Left')
screen.onkeypress(snake.snake_right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        scoreboard.reset()
        snake.reset()
        # Old code with game over
        # scoreboard.game_over()
        # game_is_on = False

    # Detect collision with segments
    body_segments = snake.segments[1:]
    for segment in body_segments:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # Old code with game over
            # scoreboard.game_over()
            # game_is_on = False

screen.exitonclick()
