from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
score.update()


screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

is_playing = True

while is_playing:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detects ball collision and bounces if it hits the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()


    # Detects if ball hits paddle and adds bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.y_bounce()


    # Detects if the ball went out of bounds and increments players points
    if ball.xcor() < -400:
        score.r_point()
        ball.reset()
    elif ball.xcor() > 400:
        score.l_point()
        ball.reset()

    if score.l_score == 8 or score.r_score == 8:
        score.game_over()


















screen.exitonclick()