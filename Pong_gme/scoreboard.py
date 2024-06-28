from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 220)
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align='center', font=('Courier', 50, 'normal'))
