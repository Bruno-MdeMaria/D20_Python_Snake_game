from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.write("Pontuação = ", move=False, align="center", font= ('Arial', 8, "normal"))
        self.pontuar()

    def pontuar(self):
        placar = 0
        self.pontuar_placar = placar + 1



