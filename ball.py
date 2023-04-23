from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.y_move = 10
        self.x_move = 10


    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)



    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1




