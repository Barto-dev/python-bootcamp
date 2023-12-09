from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        x = position[0]
        y = position[1]
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(x, y)
        self.segments.append(segment)

    def extend(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

    def move(self):
        start = len(self.segments) - 1

        # shift all segments except the first one
        for seg_num in range(start, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def check_food_collision(self, food):
        return self.head.distance(food) < 15

    def check_wall_collision(self):
        return (
            self.head.xcor() > 280
            or self.head.xcor() < -280
            or self.head.ycor() > 280
            or self.head.ycor() < -280
        )

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
