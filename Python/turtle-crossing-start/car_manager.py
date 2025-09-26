import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 1
CAR_POSITION = range(-240, 240, 40)
# global car_speed
# car_speed = MOVE_INCREMENT

class CarManager(Turtle):
    car_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1.5, 3)
        self.speed = CarManager.car_speed
        self.game_over = False
        self.generate_cars()

    def generate_cars(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.choice(CAR_POSITION))

    def move_cars(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        CarManager.car_speed += MOVE_INCREMENT
        self.speed = CarManager.car_speed










