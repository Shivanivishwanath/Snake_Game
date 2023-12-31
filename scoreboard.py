from turtle import Turtle
ALIGNMENT = "center"
FONT=("blue",24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,268)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER \n\nYOUR SCORE IS: {}".format(self.score), align=ALIGNMENT, font=FONT)
        
