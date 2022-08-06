import random
import os
from time import sleep
if os.name == "nt":
    type="cls"

def clear(type):
    os.system(type)

def selec_dificultad():
    global rango
    global dificultad
    clear(type)
    dificultad=input("Seleccione la dificultad(1,2,3,4,5):\nFacil(1):1 al 10\nMedio(2):1 al 50\nDificil(3):1 al 100\nExtremo(4):1 al 1000\nImposible(5):1 al 10000\n")
    while dificultad not in ["1", "2", "3", "4", "5"]:
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

def adivinar_num_compu(rango,dificultad):
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

def adivinar_num_user(rango,dificultad):
    clear(type)
    num_min=1
    num_max=rango
    input(f"Piense en un numero entre el 1 y el {rango}\nPrecione cualquier tecla para continuar:\n")
    estado=True
    while estado == True:
        if num_min != num_max:

            clear(type)
            adiv_num = random.randrange(num_min,num_max)
            sleep(0.5)
            print(f"Pensaste en el numero {adiv_num}?\n")
            feedBack=input("El numero es mas chico(a)\nEl numero es mas grande(b)\nEse es mi numero!(c)\n")

            while feedBack not in ["a", "b", "c"]:
                print("Error, seleccione una opcion a,b o c")
                feedBack=input("El numero es mas chico(a)\nEl numero es mas grande(b)\nEse es mi numero!(c)\n")

            if feedBack == "a": 
                num_max=adiv_num-1
            elif feedBack == "b":
                num_min = adiv_num+1
            else:
                clear(type)
                print(f"La computadora ha adivinado tu numero!({adiv_num}) entre el 1 y el {rango}")
                print(f"Dificultad {dificultad} completada\n")
                estado=False
                continue 
        else:
            clear(type)
            adiv_num=num_min
            print(f"La computadora ha adivinado tu numero!({adiv_num}) entre el 1 y el {rango}")
            print(f"Dificultad {dificultad} completada\n")
            estado=False
            
while True:
    clear(type)
    feedBack=input("Adivinar el numero de la computadora(1)\nQue la computadora adivine tu numero(2)\n")
    if feedBack not in ["1", "2"]:
        print("Error, seleccione la opcion 1 o 2")
        continue

    selec_dificultad()

    if feedBack == "1":
        adivinar_num_compu(rango,dificultad)
    else:
        adivinar_num_user(rango,dificultad)

    feedBack=input("\nDesea volver a jugar?(s/n): ")
    while feedBack != "s" and feedBack != "n":
        clear(type)
        print("Error, valor ingresado invalido")
        feedBack=input("Desea volver a jugar?(s/n): ")
    if feedBack == "n":
        clear(type)
        print("Muchas gracias por jugar")
        sleep(1.2)
        break