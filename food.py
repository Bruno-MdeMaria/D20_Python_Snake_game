from turtle import Turtle
import random

#CRIANDO A COMIDA DA SERPENTE UTILIZANDO HERANÇA DE CLASSE:

class Food(Turtle):                  #CRIADO A CLASSE FOOD UTILIZANDO A CLASSE PAI: Turtle.
    def __init__(self):              #INICADO OS ATRIBUTOS DA COMIDA __INIT__   
        super().__init__()           #importado da classe pai(super classe)
        self.shape("circle")         #utlizando os atributos da classe pai(Turtle) como .shape, .penup,.color
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color("blue")
        self.speed("fastest")
        self.aparecer()
        
    
    def aparecer(self):
        random_x = random.randint(-660, 650)  #valor aleatório para posição x entre -60 e 650(para não ser muito perto) em um tela de 1400pxl
        random_y = random.randint(-320, 320)
        self.goto(x=random_x, y=random_y)
