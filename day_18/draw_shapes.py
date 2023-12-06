from turtle import Turtle, Screen
from colors import turtle_color_list
from random import choice

timmy = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.fd(100)
        timmy.rt(angle)


for i in range(3, 11):
    random_color = choice(turtle_color_list)
    timmy.color(random_color)
    draw_shape(i)

screen = Screen()
screen.exitonclick()
