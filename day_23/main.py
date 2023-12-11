import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

timmy = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=timmy.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()
    cars.remove_offscreen_cars()

    if timmy.has_reached_finish():
        timmy.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_score()
        cars.level_up()

    if cars.has_collision_with_turtle(timmy):
        game_is_on = False
        scoreboard.game_over()

    screen.update()

screen.exitonclick()
