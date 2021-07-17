from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HASHSPEED = 0

class CarManager:
    def __init__(self):
        self.car_obj = []

    def create_car(self):
        random_value = random.randint(0, 6)
        if random_value == 1:
            car = Turtle("square")
            car.shapesize(1, 2, 1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.car_obj.append(car)


    def move_car(self):
        for car_obj in self.car_obj:
            x_cor = car_obj.xcor() - (STARTING_MOVE_DISTANCE + HASHSPEED)
            y_cor = car_obj.ycor()
            car_obj.goto(x_cor, y_cor)

    def increase_carspeed(self):
        global HASHSPEED
        HASHSPEED += MOVE_INCREMENT


