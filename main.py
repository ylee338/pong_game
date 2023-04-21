from turtle import Screen
from paddle import Paddle
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(700, 700)
screen.tracer(0)
paddle = Paddle()

screen.listen()
screen.onkey(fun=paddle.right_up, key='Up')
screen.onkey(fun=paddle.right_down, key='Down')
screen.onkey(fun=paddle.left_up, key='w')
screen.onkey(fun=paddle.left_down, key='s')



is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)















screen.exitonclick()