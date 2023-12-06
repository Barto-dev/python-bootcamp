from turtle import Turtle, Screen
from random import choice
from colors import random_rgb

timmy = Turtle()
timmy.pensize(10)
timmy.speed(5)
screen = Screen()
screen.colormode(255)


def random_direction():
    directions = [0, 90, 180, 270]
    return choice(directions)


def draw_line():
    random_color = random_rgb()
    timmy.color(random_color)
    direction = random_direction()
    timmy.setheading(direction)
    timmy.fd(25)


for _ in range(100):
    draw_line()


screen.exitonclick()
