from turtle  import Screen, Turtle, color, penup
import time

screen = Screen()
screen.setup(width= 600, height= 600)   #tamanho do screnn em pixels
screen.bgcolor("black")      #altera a cor da tela
screen.title("Snake Game")   #adiciona um ítulo a tela
screen.tracer(0)             #desligar o rastreador colocando 0 para mostrar uma nova imagem de cada vez.
                             #para aparecer a movimentacao deverá ser iniaco o update do screnn abaixo do while

lista_corpo = []
lista_posicao = [(0,0), (-20, 0), (-40, 0)]   #tupla com a posição inicial(goto) x= e y=

for posicao in lista_posicao:               #loop para cirar 3 partes do corpo usando a lista_posicao
    nova_parte = Turtle(shape="square")         #altera o formato da tataruga para quadrado(square)
    nova_parte.color("white")                   #altera a cor para branco
    nova_parte.penup()                          #ergue a caneta e retira o rastro quando se movimenta
    nova_parte.speed(1)                         #movimento mais lento(1,3,6,10,0) sendo o 0 super rápido.
    nova_parte.goto(posicao)                #posicao inicial recebe a posicao da lista_posicao conforme o loop
    lista_corpo.append(nova_parte)              #lista de corpo recebe tres partes de corpo.
    


game_iniciado = True
while game_iniciado:
    screen.update()     #inicia o screen para fazer o movimento da snake
    time.sleep(0.1)     #necessário importar o modo TIME. Isto acrescenta um atraso de 0.1 segundo entre cada parte do corpo se mover.
    for numero_parte in range(len(lista_corpo) -1, 0,-1):    #para alternar as posiçoes do corpo. 
        nova_posx = lista_corpo[numero_parte -1].xcor()      #Andar seguindo o primeiro 
        nova_posy = lista_corpo[numero_parte -1].ycor()
        lista_corpo[numero_parte].goto(nova_posx, nova_posy)
        
posicao[0].forward(20)






screen.exitonclick()    #fechar a tela somente após um clique



