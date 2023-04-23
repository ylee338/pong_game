from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.pencolor('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Left Score: {self.l_score} | Right Score: {self.r_score} ", True, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)




