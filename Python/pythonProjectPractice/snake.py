from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square_to_snake(position)

    def add_square_to_snake(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend_snake(self):
        self.add_square_to_snake(self.squares[-1].position())

    def move_snake(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)

        self.squares[0].forward(MOVE_DISTANCE)

    def move_left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def move_right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def move_up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def move_down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

