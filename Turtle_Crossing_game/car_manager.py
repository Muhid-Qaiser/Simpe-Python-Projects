from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):

        rand = random.randint(1, 6)

        if rand == 1:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.setheading(180)
            y_axis = random.randint(-220, 230)
            car.goto(300, y_axis)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT
