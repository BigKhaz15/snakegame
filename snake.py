from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

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

    def move(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_num - 1].xcor()
            new_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(x=new_x, y=new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.snake_segments:
            segment.hideturtle()
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]