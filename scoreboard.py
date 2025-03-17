from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT , font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

