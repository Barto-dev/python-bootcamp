from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def read_highscore():
    with open("data.txt") as file:
        content = file.read()
        return int(content) if content else 0


def write_highscore(new_score):
    with open("data.txt", mode="w") as file:
        file.write(new_score)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = read_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            write_highscore(str(self.highscore))
        self.score = 0
        self.update_score()
