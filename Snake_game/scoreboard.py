from turtle import Turtle


ALIGNMENT = 'center'
FONT = ("Courier", 17, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as file:
            data = file.read()
        self.score = 0
        self.high_score = int(data)
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.write(f'Score : {self.score} High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score} High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')

        self.score = 0
        self.update_scoreboard()
