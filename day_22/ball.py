from typing import Literal
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def check_top_bottom_wall_collision(self) -> bool:
        return self.ycor() > 280 or self.ycor() < -280

    def check_paddle_collision(self, paddle) -> bool:
        """Returns True if the ball collides with the paddle"""
        left_paddle_hit = self.xcor() < -350 and self.distance(paddle) < 50
        right_paddle_hit = self.xcor() > 350 and self.distance(paddle) < 50
        return left_paddle_hit or right_paddle_hit

    def is_out_of_bounds(self) -> Literal["left", "right", False]:
        if self.xcor() > 380:
            return "right"
        elif self.xcor() < -380:
            return "left"
        return False

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.move_speed *= 0.9
