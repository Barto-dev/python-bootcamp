import colorgram
from turtle import Turtle, Screen
from random import choice

rgb_colors = []
colors = colorgram.extract("dots.jpeg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)

# remove first two colors as they very light
rgb_colors = rgb_colors[2:]

timmy = Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
x_position = -380
y_position = -300
dot_size = 20
forward_distance = 50
dots_per_row = 15
dots_per_column = 13
# set position left bottom corner
timmy.setpos(x_position, y_position)

screen = Screen()
screen.colormode(255)

for _ in range(dots_per_column):
    for _ in range(dots_per_row):
        timmy.dot(dot_size, choice(rgb_colors))
        timmy.fd(forward_distance)
    timmy.setpos(x_position, timmy.ycor() + forward_distance)

screen.exitonclick()
