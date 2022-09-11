from turtle  import Screen
import time
from snake import Snake   #importando a biblioteca criada e a classe snake.
from food import Food
from scoreboard import Scoreboard

#parte relacionada a TELA:
screen = Screen()
screen.setup(width= 600, height= 600)   #tamanho do screnn em pixels
screen.bgcolor("black")      #altera a cor da tela
screen.title("Snake Game")   #adiciona um ítulo a tela
screen.tracer(0)             #desligar o rastreador colocando 0 para mostrar uma nova imagem de cada vez.
                             #para aparecer a movimentacao deverá ser iniaco o update do screnn abaixo do while



#CRIANDO UM OBJETO (snake) ATRAVÉS DA CLASSE CRIADA:
snake = Snake()    

#CRIANDO UM OBEJTO (food) ATRAVÉS DA CLASSE CRIADA NO MODO HERANÇA:
food = Food()

#CRIANDO UM OBJETO (scocreboard) ATRAVÉS DA CLASSE CRIADA NO MODO HERANÇA:
scoreboard = Scoreboard()

#OUVIR O TECLADO (.listen):
screen.listen()
screen.onkey(snake.up,"Up")     #quando ouvir up chamará o MÉTODO snake.up criado na CLASSE snake.
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_iniciado = True
while game_iniciado:
    screen.update()     #inicia o screen para fazer o movimento da snake
    time.sleep(0.1)     #necessário importar o modo TIME. Isto acrescenta um atraso de 0.1 segundo entre cada parte do corpo se mover.
    snake.mover()       #chamar o MÉTODO chamado MOVER
    
    
    
    #DETECTAR A COLISÃO DA SERPTENTE COM A COMIDA:
    if snake.cabeça.distance(food) < 15:
        food.aparecer()       #após importar a classe criada chamar o método .aparecer para aparecer a comida
        snake.crescer()       #apóa importar a classe criada chamar o método .crescer para aumentar tamanho.       
        scoreboard.pontuar()  #após importar a classe chamar o método .pontuar para marcar placar
    
   
   
    #DETECTAR COLISÃO DA SERPENTE COM A PAREDE:
    if snake.cabeça.xcor() > 280 or snake.cabeça.xcor() < -280 or snake.cabeça.ycor() > 280 or snake.cabeça.ycor() < -280:
        game_iniciado = False
        scoreboard.game_over()

    #DETECTAR COLISÃO DA SERPENTE COM A CALDA:
    for parte in snake.partes_corpo:
        if parte != snake.cabeça:
            if snake.cabeça.distance(parte) <10:
                game_iniciado = False
                scoreboard.game_over()






screen.exitonclick()    #fechar a tela somente após um clique



