from turtle import Turtle

POSICAO_INICIAL = [(0,0), (-20, 0), (-40, 0)]   #constante e, tupla com a posição inicial(goto) x= e y=
MOVER_DISTANCIA = 20

class Snake:
    #AQUI DEFINIMOS OS ATRIBUTOS:
    def __init__(self):  # _init_para atribuir valores p propriedades do objeto ou operações quandoobjeto for criado:
       self.partes_corpo = []         
       self.criar_snake()
       self.cabeça = self.partes_corpo[0]   #foi incluido depois..atributo cabeça: definido que a cabeça será a parte [0] do corpo


    #adionando um MÉTODO para criar a snake.:

    def criar_snake(self):   
        for posicao in POSICAO_INICIAL:               #loop para cirar 3 partes do corpo usando a lista_posicao
            nova_parte = Turtle(shape="square")         #altera o formato da tataruga para quadrado(square)
            nova_parte.color("white")                   #altera a cor para branco
            nova_parte.penup()                          #ergue a caneta e retira o rastro quando se movimenta
            nova_parte.speed(1)                         #movimento mais lento(1,3,6,10,0) sendo o 0 super rápido.
            nova_parte.goto(posicao)               #posicao inicial recebe a posicao da lista_posicao conforme o loop
            self.partes_corpo.append(nova_parte)         #lista [] partes_corpo recebe tres partes de corpo.


    #adicionando um MÉTODO para mover a snake:

    def mover(self):
        for numero_parte in range(len(self.partes_corpo) -1, 0,-1):    #para alternar as posiçoes do corpo. 
            nova_posx = self.partes_corpo[numero_parte -1].xcor()      #Andar com a calda seguindo a cabeça 
            nova_posy = self.partes_corpo[numero_parte -1].ycor()
            self.partes_corpo[numero_parte].goto(nova_posx, nova_posy)
        self.cabeça.forward(MOVER_DISTANCIA)
        
    #SEMPRE DENTRO(IDENTAÇÃO) DA CLASSE SNAKE:
    #adicionado MÉTODOS para mover conforme as direções do teclado:
    
    def up(self):
        self.cabeça.setheading(90)  #parte [0]do corpo é a cabeça que queremos movimentar. podemos incluir um nome como cabeça. e se está para cima é 90 graus. SETHEADING é um método da TURTLE.
        
    def down(self):
        self.cabeça.setheading(270)

    def left(self):
        self.cabeça.setheading(180)

    def right(self):
        self.cabeça.setheading(0)