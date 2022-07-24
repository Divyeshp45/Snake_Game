from turtle import Turtle

FONT = "Courier"
ALIGN = "center"
FONT_SIZE = 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(F"Score: {self.score}", align=ALIGN, font=(FONT, FONT_SIZE, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(F"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=(FONT, FONT_SIZE, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.clear()
        self.update_scoreboard()

