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
        