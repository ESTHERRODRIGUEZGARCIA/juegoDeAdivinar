import random
numero = random.randint(0, 100)
intento = int(input("Introduce un número: "))
intento = True
while intento == True:
    if intento < numero:
        print("Demasiado pequeño")
    elif intento == numero:
        print("¡Has ganado!")
    else:
        print("Demasiado grande ")
    intento = False
    print("Introduce otro numero: ")


