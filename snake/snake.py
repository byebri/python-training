from turtle import Turtle

SNAKE_CORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.make_snake()
        self.front = self.all_snakes[0]

    def make_snake(self):
        for pos in SNAKE_CORDS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.all_snakes.append(snake)

    def move(self):
        for snake_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[snake_num - 1].xcor()
            new_y = self.all_snakes[snake_num - 1].ycor()
            self.all_snakes[snake_num].goto(new_x, new_y)
        self.front.forward(MOVE_DISTANCE)

    def left(self):
        if self.front.heading() != RIGHT:
            self.front.setheading(LEFT)

    def right(self):
        if self.front.heading() != LEFT:
            self.front.setheading(RIGHT)

    def up(self):
        if self.front.heading() != DOWN:
            self.front.setheading(UP)

    def down(self):
        if self.front.heading() != UP:
            self.front.setheading(DOWN)

    def extend(self):
        tail = Turtle("square")
        tail.color("white")
        tail.penup()
        tail.goto(self.all_snakes[-1].xcor(), self.all_snakes[-1].ycor())
        self.all_snakes.append(tail)

