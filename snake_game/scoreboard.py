from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        self.i = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write("Score: " + str(self.i), align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score(self):
        self.i += 1
        self.clear()
        self.write(f"Score: {self.i}", False, align=ALIGNMENT, font=FONT)
