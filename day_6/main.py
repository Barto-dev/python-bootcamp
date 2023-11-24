# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_left():
    print("Left")


def right_is_clear():
    print("Clear")


def move():
    print("Move")


def front_is_clear():
    print("Clear")


def wall_in_front():
    print("Clear")


def at_goal():
    print("Finish")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
