#Ping Pong Game

from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.tracer(0)
ball_speed = 0.1

screen.title("Ping Pong Game")

Paddle_left = Paddle((-350, 0))
Paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Paddle_right.move_down_right, "Down")
screen.onkey(Paddle_right.move_up_right, "Up")
screen.onkey(Paddle_left.move_down_left, "s")
screen.onkey(Paddle_left.move_up_left, "w")

game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move_the_ball()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with Paddle
    if ball.distance(Paddle_right) < 50 and ball.xcor() > 320 or ball.distance(Paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball_speed *= 0.9
    #if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball_speed = 0.1
        scoreboard.increase_right_score()

    #if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()


screen.exitonclick()
