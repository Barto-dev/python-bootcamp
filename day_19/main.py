from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
).lower()

if user_bet:
    is_race_on = True

for turtle_idx in range(6):
    y_coordinate = -70 + turtle_idx * 30
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(10)
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    new_turtle.setpos(x=-230, y=y_coordinate)
    all_turtles.append(new_turtle)


def check_winner(current_turtle):
    global is_race_on
    if current_turtle.xcor() > 215:
        winning_color = current_turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_color} turtle is the winner!")
        is_race_on = False


while is_race_on:
    for turtle in all_turtles:
        check_winner(turtle)
        rand_distance = randint(1, 10)
        turtle.fd(rand_distance)

screen.exitonclick()
