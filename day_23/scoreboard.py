from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
LEVEL_POSITION = (-220, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.update_score()

    def increase_level(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
