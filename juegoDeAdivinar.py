import random
numero = random.randint(0, 100)
intentosRealizados = 0

intento = int(input("Adivina el número: "))

while intento != numero :
    intentosRealizados = intentosRealizados + 1   
    if intento < numero:
        print("Demasiado pequeño ")
        print("Introduce otro número: ")
    elif intento > numero:
        print("Demasiado grande ")  
        print("Introduce otro número: ")
    else:
        print("¡Has ganado en tu primer intento!")
        break      
    print("Enhorabuena, has realizado ", intentosRealizados, "intentos")

if intento == numero:
    print("¡Has ganado en tu primer intento!")


