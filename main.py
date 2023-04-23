from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(fun=paddle.right_up, key='Up')
screen.onkey(fun=paddle.right_down, key='Down')
screen.onkey(fun=paddle.left_up, key='w')
screen.onkey(fun=paddle.left_down, key='s')



is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detects ball colision and bounces if it hits the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(paddle) < 50 and ball.xcor() > 280:
        ball.x_bounce()

















screen.exitonclick()