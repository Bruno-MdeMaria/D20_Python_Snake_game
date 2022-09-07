POSICAO_INICIAL = [(0,0), (-20, 0), (-40, 0)]   #constante e, tupla com a posição inicial(goto) x= e y=
lista_corpo = []

class Snake:
    def __init__(self):  # _init_para atribuir valores p propriedades do objeto ou operações quandoobjeto for criado:
       self.partes_corpo = []
       self.criar_snake()

    def criar_snake():   #adionando um MÉTODO para criar a snake
        for posicao in lista_posicao:               #loop para cirar 3 partes do corpo usando a lista_posicao
            nova_parte = Turtle(shape="square")         #altera o formato da tataruga para quadrado(square)
            nova_parte.color("white")                   #altera a cor para branco
            nova_parte.penup()                          #ergue a caneta e retira o rastro quando se movimenta
            nova_parte.speed(1)                         #movimento mais lento(1,3,6,10,0) sendo o 0 super rápido.
            nova_parte.goto(posicao)                #posicao inicial recebe a posicao da lista_posicao conforme o loop
            lista_corpo.append(nova_parte)              #lista de corpo recebe tres partes de corpo.
