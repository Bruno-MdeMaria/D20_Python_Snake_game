from turtle  import Screen, Turtle, color, penup
import time
from snake import Snake   #importando a biblioteca criada e a classe snake.


#parte relacionada a TELA:
screen = Screen()
screen.setup(width= 600, height= 600)   #tamanho do screnn em pixels
screen.bgcolor("black")      #altera a cor da tela
screen.title("Snake Game")   #adiciona um ítulo a tela
screen.tracer(0)             #desligar o rastreador colocando 0 para mostrar uma nova imagem de cada vez.
                             #para aparecer a movimentacao deverá ser iniaco o update do screnn abaixo do while



#CRIANDO UM OBJETO (snake) ATRAVÉS DA CLASSE CRIADA:
snake = Snake()    

#OUVIR O TECLADO (.listen):
screen.listen()
screen.onkey("Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")



game_iniciado = True
while game_iniciado:
    screen.update()     #inicia o screen para fazer o movimento da snake
    time.sleep(0.1)     #necessário importar o modo TIME. Isto acrescenta um atraso de 0.1 segundo entre cada parte do corpo se mover.
    snake.mover()       #chamar o MÉTODO chamado MOVER






screen.exitonclick()    #fechar a tela somente após um clique



