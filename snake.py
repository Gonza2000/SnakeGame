import turtle
import time
import random
import winsound

delay = 0.08

# Pantalla

pantalla = turtle.Screen()
pantalla.title('Snake Game')
pantalla.setup(width=1280, height=720)
pantalla.tracer(0)
pantalla.bgpic('Diseño sin título.png')


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
#funcion sonido para comer manzana

def sonido_manzana():
    winsound.PlaySound("nombre_del_sonido.wav", winsound.SND_FILENAME)

# Creación de objetos

cabeza = crear_elemento('square', '#d40404', 2)
cabeza.tecla = ''
puntaje_snake = crear_elemento('turtle', 'white', 2)
puntaje_snake.hideturtle()
vida_snake = crear_elemento('turtle', 'white', 2)
vida_snake.hideturtle()
vida_snake.goto(400, 300)
puntaje_snake.goto(0, 300)
mensaje_derrota = crear_elemento('square', "black", 2)
mensaje_derrota.hideturtle()
mensaje_derrota.goto(0, 60)
meta = crear_elemento('square', "black", 2)
meta.goto(-600,300)
mensaje_derrota.hideturtle()
mensaje_derrota.goto(0, 60)
villano = crear_elemento('triangle', 'black', 2)
villano.goto(2000, 2000)
villano2 = crear_elemento('triangle', 'black', 2)
meta.hideturtle()
villano2.goto(2000, 2000)
meta.color("white")

# Movimiento

def derecha():
    if cabeza.tecla != 'izquierda':
        cabeza.tecla = 'derecha'


def izquierda():
    if cabeza.tecla != 'derecha':
        cabeza.tecla = 'izquierda'


def arriba():
    if cabeza.tecla != 'abajo':
        cabeza.tecla = 'arriba'


def abajo():
    if cabeza.tecla != 'arriba':
        cabeza.tecla = 'abajo'


def movimiento_snake():
    if cabeza.tecla == 'derecha':
        cabeza.setx(cabeza.xcor() + 30)
    if cabeza.tecla == 'izquierda':
        cabeza.setx(cabeza.xcor() - 30)
    if cabeza.tecla == 'arriba':
        cabeza.sety(cabeza.ycor() + 30)
    if cabeza.tecla == 'abajo':
        cabeza.sety(cabeza.ycor() - 30)


# Teclado

pantalla.listen()
pantalla.onkeypress(derecha, 'd')
pantalla.onkeypress(izquierda, 'a')
pantalla.onkeypress(arriba, 'w')
pantalla.onkeypress(abajo, 's')
# Capturar letras mayusculas, necesario para que el jugador pueda jugar
pantalla.onkeypress(derecha, 'D')
pantalla.onkeypress(izquierda, 'A')
pantalla.onkeypress(arriba, 'W')
pantalla.onkeypress(abajo, 'S')
#Capturar flechas
pantalla.onkeypress(derecha, 'Right')
pantalla.onkeypress(izquierda, 'Left')
pantalla.onkeypress(arriba, 'Up')
pantalla.onkeypress(abajo, 'Down')


# Elemento Manzana
color_random = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]
manzana = crear_elemento('circle', color_random, 0)
manzana.setposition(200, -100)

# Lista donde contiene cuerpo de snake
cuerpo_snake = []

#marcadores
puntaje = 0
puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
vidas = 3
vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
meta.write(f"Reto: llegar a un Puntaje de 20.", align="left", font=("Arial", 16, "italic"))

# Bucle Principal
while True:
    pantalla.update()
    #si ganas
    if puntaje == 20:
        mensaje_derrota.color("#9B00FF")
        mensaje_derrota.write(f"¡FELICIDADES,ERES EL MEJOR!", align="center",
                              font=("Verdana", 30, "italic"))

        villano.goto(2000, 2000)
        villano2.goto(2000, 2000)
        manzana.setposition(200, -100)
        cabeza.tecla = ""
        vidas = 3
        vida_snake.clear()
        vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
        puntaje = 0
        puntaje_snake.clear()
        puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
        for cuerpo in cuerpo_snake:
            cuerpo.goto(1000, 1000)
        cuerpo_snake = []
        time.sleep(1)

    if puntaje >= 5:
        delay= 0.06
        villano.goto(-200, 100)
        villano.forward(50)
        villano.left(19)


    if puntaje >= 10:
        villano2.goto(100, -200)
        villano2.forward(50)
        villano2.left(19)
    #aumentar complejidad
    if puntaje >=15:
        delay = 0.05
        villano.left(19.1)
        villano2.left(19.1)
    #reiniciar delay
    if puntaje ==0:
        delay = 0.08
    if vidas == 0:
        villano.goto(2000,2000)
        villano2.goto(2000, 2000)
        manzana.setposition(200, -100)
        cabeza.tecla = ""
        vidas = 3
        vida_snake.clear()
        vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
        puntaje = 0
        puntaje_snake.clear()
        puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))
        for cuerpo in cuerpo_snake:
            cuerpo.goto(1000, 1000)
        cuerpo_snake = []
        mensaje_derrota.color("#9B00FF")
        mensaje_derrota.write(f"Perdiste :(, pulsa cualquier tecla para intentarlo de nuevo", align="center",
                              font=("Verdana", 30, "italic"))

    # Límites
    if cabeza.xcor() > 600 or cabeza.xcor() < -620 or cabeza.ycor() > 340 or cabeza.ycor() < -335:

        vidas -= 1
        vida_snake.clear()
        vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
        cabeza.tecla = ''
        time.sleep(1)
        cabeza.home()
        manzana.setposition(200, 100)
        for cuerpo in cuerpo_snake:
            cuerpo.goto(1000, 1000)
    # si la cabeza topa al villano, te resta una vida y te vas al home
    if cabeza.distance(villano) < 20 or cabeza.distance(villano2) < 20:
        cabeza.tecla = ""
        cabeza.home()
        time.sleep(1)
        vidas -= 1
        vida_snake.clear()
        vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
        for cuerpo in cuerpo_snake:
            cuerpo.goto(1000, 1000)

    for cuerpo in cuerpo_snake:
        if cuerpo.distance(villano) < 20 or cuerpo.distance(villano2) < 20:
            cabeza.tecla = ""
            cabeza.home()
            vidas -= 1
            vida_snake.clear()
            vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
            for cuerpo in cuerpo_snake:
                cuerpo.goto(1000, 1000)

    # Comer y cambiar posicion de manzana
    if cabeza.distance(manzana) < 50:
        color_manzana = manzana.pencolor()
        x = random.randint(-620, 620)
        y = random.randint(-340, 340)
        manzana.goto(x, y)
        color_random = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]
        manzana.color(color_random)
        cuerpo = crear_elemento('square', color_manzana, 0)
        cuerpo_snake.append(cuerpo)
        puntaje += 1
        puntaje_snake.clear()
        puntaje_snake.write(f"Puntaje: {puntaje}", align="left", font=("Arial", 16, "italic"))

    #los segmentos del cuerpo de snake siguen a la cabeza
    for i in range(len(cuerpo_snake) - 1, 0, -1):
        x = cuerpo_snake[i - 1].xcor()
        y = cuerpo_snake[i - 1].ycor()
        cuerpo_snake[i].goto(x, y)

    if len(cuerpo_snake) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo_snake[0].goto(x, y)

    movimiento_snake()
    #reanudar juego luego de derrota
    if cabeza.tecla != "":
        mensaje_derrota.clear()
        mensaje_derrota.write(f"", align="left", font=("Arial", 16, "italic"))
    # checar la colisión con el cuerpo
    for cuerpo in cuerpo_snake:
        if cuerpo.distance(cabeza) < 20 and cabeza.xcor() != 0 and cabeza.ycor() != 0:
            cabeza.tecla = ""
            vidas -= 1
            vida_snake.clear()
            vida_snake.write(f"Vida: {vidas}", align="left", font=("Arial", 16, "italic"))
            cabeza.home()
            time.sleep(1)
            time.sleep(0.5)
            for cuerpo in cuerpo_snake:
                cuerpo.goto(1000, 1000)

    time.sleep(delay)