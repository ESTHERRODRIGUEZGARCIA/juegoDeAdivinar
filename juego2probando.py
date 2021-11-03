print("¡Empezamos!")

import random
numero = random.randint(0, 100)
intentosRealizados = 0

intento = int(input("Adivina el número: "))

while True:
    intentosRealizados = intentosRealizados + 1
    print("Has ganado")
    if intento==numero:
        break 
    if intento < numero:
        print("Demasiado pequeño ")
        print("Introduce otro número: ")
    if intento > numero:
        print("Demasiado grande ")  
        print("Introduce otro número: ")

#mensaje fuera
print("Enhorabuena, has realizado ", intentosRealizados, "intentos")

