from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-235, 270)
        self.color("red")
        self.level_no = 1
        self.write(arg=f"LEVEL:{self.level_no}", align="center", font=FONT)

    def level_up(self):
        self.level_no += 1
        self.clear()
        self.write(arg=f"LEVEL:{self.level_no}", align="center", font=FONT)

    def game_over(self):
        self.write(arg="GAMEOVER!", align="center", font=FONT)
