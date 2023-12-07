from turtle import Turtle, Screen
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X = -230
STARTING_Y = -70
Y_INCREMENT = 30
FINISH_LINE_X = 215
MIN_MOVE_DISTANCE = 1
MAX_MOVE_DISTANCE = 10


def create_turtle(color, y_coordinate):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(10)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setpos(x=STARTING_X, y=y_coordinate)
    return new_turtle


def check_winner(current_turtle):
    global is_race_on
    if current_turtle.xcor() > 215:
        winning_color = current_turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_color} turtle is the winner!")
        is_race_on = False


screen = Screen()
screen.setup(width=500, height=400)

while True:
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
    ).lower()
    if user_bet in COLORS:
        break
    print(f"Invalid color. Please enter one if the following {', '.join(COLORS)}")

is_race_on = True
all_turtles = []

for turtle_idx in range(6):
    y_coordinate = STARTING_Y + turtle_idx * Y_INCREMENT
    color = COLORS[turtle_idx]
    new_turtle = create_turtle(color, y_coordinate)
    all_turtles.append(new_turtle)


while is_race_on:
    for turtle in all_turtles:
        check_winner(turtle)
        rand_distance = randint(MIN_MOVE_DISTANCE, MAX_MOVE_DISTANCE)
        turtle.fd(rand_distance)

screen.exitonclick()
