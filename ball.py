from turtle import Turtle


BOUNCE = [x for x in range(-300, 300)]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = []
        self.create()


    def create(self):
        new_ball = Turtle(shape="circle")
        new_ball.color("red")
        new_ball.penup()
        self.ball.append(new_ball)


    def move(self):
        self.ball[0].forward(20)




