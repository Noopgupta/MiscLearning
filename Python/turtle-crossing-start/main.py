import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")
iterator = 1
car_list = []
car = CarManager()
car_list.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    if iterator % 50 == 0:
        car = CarManager()
        car_list.append(car)
    if iterator % 20 == 0:
        for car_var in car_list:
            car_var.move_cars()
    for car_var in car_list:
        if car_var.distance(player) < 30:
            game_is_on = False

    #if turtle crosses the level
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        for car_var in car_list:
            car_var.increase_speed()
    iterator += 1

scoreboard.game_over()


screen.exitonclick()