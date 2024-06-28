from turtle import Turtle, Screen
import random


race_is_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_axes = [-70, -40, -10, 20, 50, 80]

all_turtles = []

winner_turtle = ''

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axes[index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        movement = random.randint(0, 10)
        turtle.forward(movement)

        if turtle.xcor() >= 220:
            race_is_on = False
            winner_turtle = turtle.pencolor()

if winner_turtle == user_bet:
    print("You Won!")
else:
    print("You Lost.")

print("The winner turtle is " + winner_turtle + ".")

screen.exitonclick()
