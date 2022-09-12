from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14 , "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  #hamando todos os atributos e métodos(turtle) para dentro de nossa classe
        self.color("white")
        self.penup()
        self.hideturtle()     #método da Turtle faz desaparecer a seta ou qualquer outro formato da tartaruga.
        self.goto(0,1170)
        self.pontos = 0
        self.update_scoreboard() #método criado abaixo:
        
        
    def update_scoreboard(self):         #este método vai atualizar a pontuação, pois dentro dos atributos ele nã funiona corretamente.
        self.write(f"Pontos= {self.pontos} ", move=False, align=ALIGN, font= FONT)

    def game_over(self):                 #informar ao jogador quando o jogo acabou
        self.goto(0,0)                   #aparecer no centro da tela e não no topo como no atributo inicial
        self.write("GAME OVER", move=False, align=ALIGN, font= FONT)
        
    def pontuar(self):
        self.pontos += 1     #aumenta um ponto toda vez que o método é chamado.
        self.clear()         #método limpar da Turtle para não sobrepor os valores
        self.update_scoreboard()
        
        



