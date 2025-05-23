from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as high_score_file:
            self.highscore = int(high_score_file.read())
        self.print_scoreboard()

    def print_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(arg = f"Score: {self.score} High Score: {self.highscore}",align = ALIGNMENT, font = FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as high_score_file:
                high_score_file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.print_scoreboard()


from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as high_score_file:
            self.highscore = int(high_score_file.read())
        self.print_scoreboard()

    def print_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(arg = f"Score: {self.score} High Score: {self.highscore}",align = ALIGNMENT, font = FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as high_score_file:
                high_score_file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.print_scoreboard()


