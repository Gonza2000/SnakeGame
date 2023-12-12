import turtle
import time
import random


delay = 0.06

# Pantalla

pantalla = turtle.Screen()
pantalla.title('Snake Game')
pantalla.setup(width=1280, height=720)
pantalla.tracer(0)
pantalla.bgcolor('black')


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
puntaje_snake = crear_elemento('turtle', '#d40404', 2)
puntaje_snake.hideturtle()
vida_snake = crear_elemento('turtle', '#d40404', 2)
vida_snake.hideturtle()
vida_snake.goto(-560, 200)
puntaje_snake.goto(-600, 300)

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
puntaje = 0
vidas=3
puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
vida_snake.write(f"Vidas: {vidas}", align="center", font=("Arial", 16, "italic"))


while True:
    pantalla.update()
    #si pierdes
    if vidas == 0:
        ventana_perdiste = crear_elemento('square','#d40404',0)
        ventana_perdiste.hideturtle()
        ventana_perdiste.write("Perdiste :( intentalo de nuevo", align="center", font=("Arial", 16, "italic"))
        puntaje=0
        vidas = 3
        vida_snake.clear()
        vida_snake.write(f"Vidas: {vidas}", align="center", font=("Arial", 16, "italic"))
        puntaje_snake.clear()
        puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
        for i in cuerpo_snake:
            i.goto(1000,1000)    
        cuerpo_snake=[]
    # Límites
    if cabeza.xcor() > 600 or cabeza.xcor() < -620 or cabeza.ycor() > 340 or cabeza.ycor() < -335:
        cabeza.tecla = ''
        time.sleep(1)
        cabeza.home()
        manzana.setposition(200, 100)
        for i in cuerpo_snake:
            i.goto(1000,1000)    
        vidas-=1 
        vida_snake.clear()
        vida_snake.write(f"Vidas: {vidas}", align="center", font=("Arial", 16, "italic"))
    
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
        puntaje+=1
        puntaje_snake.clear()
        puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
   
  
    for i in range(len(cuerpo_snake) - 1, 0, -1):
        x = cuerpo_snake[i - 1].xcor()
        y = cuerpo_snake[i - 1].ycor()
        cuerpo_snake[i].goto(x, y)

    if len(cuerpo_snake) > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo_snake[0].goto(x, y)    

    movimiento_snake()
    
    time.sleep(delay)