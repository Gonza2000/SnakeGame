import turtle
import time
import random

# Pantalla

pantalla = turtle.Screen()

delay = 0.001
pantalla.title('Snake Game')
#las animaciones se dibujan con cierto delay
pantalla.tracer(1)

pantalla.setup(width=1280, height=720)


# Función para crear elementos


def crear_elemento(forma, color, velocidad):
    elemento = turtle.Turtle()
    elemento.speed(velocidad)
    elemento.shape(forma)
    elemento.shapesize(stretch_len=1.5, stretch_wid=1.5, outline=1)
    elemento.color(color)
    elemento.penup()
    elemento.home()
    return elemento

# Creación objeto cabeza

cabeza = crear_elemento('square', '#d40404', 2)
cabeza.tecla = ''


# Movimiento

def derecha():
    cabeza.tecla = 'd'


def izquierda():
    cabeza.tecla = 'c'


def arriba():
    cabeza.tecla = 'a'


def abajo():
    cabeza.tecla = 'b'


def movimiento_snake():
     
    if cabeza.tecla == 'd':
        cabeza.setx(cabeza.xcor() + 30)
    if cabeza.tecla == 'c':
        cabeza.setx(cabeza.xcor() - 30)
    if cabeza.tecla == 'a':
        cabeza.sety(cabeza.ycor() + 30)
    if cabeza.tecla == 'b':
        cabeza.sety(cabeza.ycor() - 30)


# Teclado

pantalla.listen()
pantalla.onkeypress(derecha, 'd')
pantalla.onkeypress(izquierda, 'a')
pantalla.onkeypress(arriba, 'w')
pantalla.onkeypress(abajo, 's')
#Capturar letras mayusculas, necesario para que el jugador pueda jugar
pantalla.onkeypress(derecha, 'D')
pantalla.onkeypress(izquierda, 'A')
pantalla.onkeypress(arriba, 'W')
pantalla.onkeypress(abajo, 'S')

# Elemento Manzana
color_random = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]
manzana = crear_elemento('circle', color_random, 0)
manzana.setposition(200, 100)


# Lista donde contiene cuerpo de snake
cuerpo_snake = []
# Bucle Principal


while True:
    pantalla.update()

    # Límites
    if cabeza.xcor() > 600 or cabeza.xcor() < -620 or cabeza.ycor() > 340 or cabeza.ycor() < -335:
        cabeza.tecla = ''
        time.sleep(0.5)
        cabeza.home()

    # Cambio de posición de la Manzana
    if cabeza.distance(manzana) < 50:
        color_manzana = manzana.pencolor()
        x = random.randint(-620, 620)
        y = random.randint(-340, 340)
        manzana.goto(x, y)
        color_random = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]
        manzana.color(color_random)
        cuerpo = crear_elemento('square', color_manzana, 0)
        cuerpo_snake.append(cuerpo)

   
    if len(cuerpo_snake) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo_snake[0].goto(x, y)    
        
    for i in range(len(cuerpo_snake) - 1, 0, -1):
        x = cuerpo_snake[i - 1].xcor()
        y = cuerpo_snake[i - 1].ycor()
        cuerpo_snake[i].goto(x, y)

    

    movimiento_snake()
    time.sleep(delay)
