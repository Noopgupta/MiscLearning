#Snake Game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")

screen.title("Snake Game")
screen.tracer(0)

snake1 = Snake()
snake_food = Food()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake1.move_down, "Down")
screen.onkey(snake1.move_up, "Up")
screen.onkey(snake1.move_left, "Left")
screen.onkey(snake1.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move_snake()

    #Collision with Food
    if snake1.squares[0].distance(snake_food) < 15:
        snake_food.refresh()
        snake1.extend_snake()
        Scoreboard.increase_score()


    # # Collision with Walls
    # if snake1.squares[0].xcor() > 290 or snake1.squares[0].xcor() < -290 or snake1.squares[0].ycor() > 290 or \
    #         snake1.squares[0].ycor() < -290:
    #     game_is_on = False
    #     Scoreboard.game_over()

    # Collision with Snake itself
    for sq in snake1.squares[1:]:
        if snake1.squares[0].distance(sq) < 10:
            game_is_on = False
            Scoreboard.game_over()




screen.exitonclick()