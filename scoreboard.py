from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_scoreboard()

    def print_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(arg = f"Score: {self.score}",align = ALIGNMENT, font = FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_scoreboard()

    def game_over(self):
        self.teleport(0,0)
        self.write(arg = "GAME OVER", align= "center", font = ("Roboto", 20, "bold"))

    def reset_scoreboard(self):
        self.clear()
        self.score = 0
        self.print_scoreboard()