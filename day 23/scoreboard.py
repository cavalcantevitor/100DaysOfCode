from turtle import Turtle

FONT = ("monospaced", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 245)
        self.write(f"Level: {self.level}", align="center", font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(FONT))

    def next_level(self):
        self.level += 1