from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEFT_PADDLE_X_POSITION,
    RIGHT_PADDLE_X_POSITION,
)
import time


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

right_paddle = Paddle((RIGHT_PADDLE_X_POSITION, 0))
left_paddle = Paddle((LEFT_PADDLE_X_POSITION, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=right_paddle.up, key="w")
screen.onkey(fun=right_paddle.down, key="s")

screen.onkey(fun=left_paddle.up, key="Up")
screen.onkey(fun=left_paddle.down, key="Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.check_top_bottom_wall_collision():
        ball.bounce_y()

    is_right_paddle_hit = ball.check_paddle_collision(right_paddle)
    is_left_paddle_hit = ball.check_paddle_collision(left_paddle)

    if is_right_paddle_hit or is_left_paddle_hit:
        ball.bounce_x()
        ball.increase_speed()

    out_of_bounds = ball.is_out_of_bounds()
    if out_of_bounds == "right":
        ball.reset_position()
        scoreboard.left_point()
    elif out_of_bounds == "left":
        ball.reset_position()
        scoreboard.right_point()

    screen.update()

screen.exitonclick()
