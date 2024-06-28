# Extracts Color from Picture
# import colorgram
#
# colors = colorgram.extract("hirst_spot.jpg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random


def random_color():
    rand = random.randint(0, len(color_list)-1)
    return color_list[rand]


def print_colored_dots():
    color = random_color()
    tim.color(color)
    tim.fillcolor(color)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()


def make_dot(x, y, space):
    tim.penup()
    tim.setpos(y*space, x*space)
    tim.pendown()
    print_colored_dots()


color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181),
              (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68),
              (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177),
              (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182),
              (175, 94, 98), (179, 192, 205)]

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.hideturtle()

grid_size = 35
tim.speed('fastest')

for x in range(-5, 5):
    for y in range(-5, 5):
        make_dot(x, y, grid_size)

screen.exitonclick()
