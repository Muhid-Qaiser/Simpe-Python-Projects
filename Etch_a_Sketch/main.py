from turtle import Turtle, Screen
# import turtle as t


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clockwise():
    tim.right(10)


def move_anticlockwise():
    tim.left(-10)


def move_diagonal():
    tim.right(10)
    tim.forward(10)


def clear():
    tim.reset()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=move_anticlockwise)
screen.onkeypress(key='d', fun=move_clockwise)
screen.onkeypress(key='c', fun=clear)

screen.exitonclick()
