from colors import random_rgb
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_rgb())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(3)

screen.exitonclick()
