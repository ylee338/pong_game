from turtle import Turtle


POSITION = [(290, 0), (-290, 0)]
FORWARD = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.create()




    def create(self):
        for position in POSITION:
            new = Turtle(shape="square")
            new.shapesize(stretch_wid=5, stretch_len=1)
            new.color("white")
            new.penup()
            new.setposition(position)
            self.segment.append(new)

    def right_up(self):
        self.segment[0].sety(self.segment[0].ycor() + FORWARD)

    def right_down(self):
        self.segment[0].sety(self.segment[0].ycor() - FORWARD)

    def left_up(self):
        self.segment[1].sety(self.segment[1].ycor() + FORWARD)

    def left_down(self):
        self.segment[1].sety(self.segment[1].ycor() - FORWARD)















