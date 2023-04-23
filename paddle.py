from turtle import Turtle



FORWARD = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.sety(self.ycor() + FORWARD)

    def down(self):
        self.sety(self.ycor() - FORWARD)

















