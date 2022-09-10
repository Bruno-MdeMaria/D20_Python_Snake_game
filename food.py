from turtle import Turtle
import random

#CRIANDO A COMIDA DA SERPENTE UTILIZANDO HERANÇA DE CLASSE:

class food(Turtle):                  #CRIADO A CLASSE FOOD UTILIZANDO A CLASSE PAI: Turtle.
    def __init__(self):              #INICADO OS ATRIBUTOS DA COMIDA __INIT__   
        super().__init__()           #importado da classe pai(super classe)
        self.shape("circle")         #utlizando os atributos da classe pai(Turtle) como .shape, .penup,.color
        self.penup()
        self.shapesize()
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)  #valor aleatório para posição x entre -280 e 280 em um tela de 600pxl
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)