from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT , font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", mode = 'w') as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg= "Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
