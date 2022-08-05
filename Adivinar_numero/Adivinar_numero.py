import random
import os
from time import sleep

if os.name == "nt":
    type="cls"

def clear(type):
    os.system(type)

def adivinar(rango):
    clear(type)
    numero_aleatorio = random.randrange(1,rango)
    while True:
        numero=int(input("Ingrese un numero: "))
        if numero > numero_aleatorio:
            clear(type)
            print("El numero es mas pequeño")
        elif numero < numero_aleatorio:
            clear(type)
            print("El numermo es mas grande")
        else:
            clear(type)
            print(f"Felicidades !! El numero era {numero_aleatorio}\nHas superado la dificultad {dificultad}\n")
            break

while True:

    clear(type)
    dificultad=input("Seleccione la dificultad(1,2,3,4,5):\nFacil(1):1 al 10\nMedio(2):1 al 50\nDificil(3):1 al 100\nExtremo(4):1 al 1000\nImposible(5):1 al 10000\n")
    while dificultad != "1" and dificultad != "2" and dificultad != "3" and dificultad != "4" and dificultad != "5":
        clear(type)
        dificultad=input("Error, por favor selecciona una dificultad del 1 al 5\nFacil(1):1 al 10\nMedio(2):1 al 50\nDificil(3):1 al 100\nExtremo(4):1 al 1000\nImposible(5):1 al 10000\n")

    if dificultad=="1":
        rango=10
        dificultad="Facil"
    elif dificultad=="2":
        rango=50
        dificultad="Media"
    elif dificultad=="3":
        rango=100
        dificultad="Dificil"
    elif dificultad=="4":
        rango=1000
        dificultad="Extrema"
    else:
        rango=10000
        dificultad="Imposible"
            
    adivinar(rango)

    estado=input("\nDesea volver a jugar?(s/n): ")
    while estado != "s" and estado != "n":
        clear(type)
        print("Error, valor ingresado invalido")
        estado=input("Desea volver a jugar?(s/n): ")
    if estado == "n":
        clear(type)
        print("Muchas gracias por jugar")
        sleep(1.2)
        break