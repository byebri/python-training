from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game Over! Score: {self.score}", align="center", font=("Arial", 15, "normal"))