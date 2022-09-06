from re import X
from turtle  import Screen, Turtle, color, penup

screen = Screen()
screen.setup(width= 600, height= 600)   #tamanho do screnn em pixels
screen.bgcolor("black")      #altera a cor da tela
screen.title("Snake Game")   #adiciona um ítulo a tela

lista_corpo = []
lista_posicao = [(0,0), (-20, 0), (-40, 0)]

for parte_corpo in lista_posicao:
    nova_parte = Turtle(shape="square")
    nova_parte.color("white")
    nova_parte.penup()
    nova_parte.goto(parte_corpo)
    lista_corpo.append(nova_parte)







screen.exitonclick()    #fechar a tela somente após um clique


