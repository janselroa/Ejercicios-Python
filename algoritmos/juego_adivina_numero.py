"""
juego de adivina el numero
"""
import random

numero_intentos=0
numero_aleatorio=random.randint(1, 20)
nombre_usuario=input("Hola, cual es tu nombre:\n")

print(f"Hola {nombre_usuario} estoy pensando en un numero del 1 al 20")

while numero_intentos<7:
    estimacion=int(input("Intenta adivinar:\n"))
    numero_intentos+=1

    if estimacion==numero_aleatorio: 
        print(f"!Ganaste, en solo {numero_intentos} intentos")
        break

    elif estimacion>numero_aleatorio:
        print("Intenta con un numero mas bajo")
        
    elif estimacion<numero_aleatorio:
        print("Intenta con un numero mas alto")

if numero_intentos==7:
    print(f"uff perdiste {nombre_usuario} el numero era {numero_aleatorio}")
