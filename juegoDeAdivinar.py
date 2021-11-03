import random
numero = random.randint(0, 100)
intento = int(input("Adivina el número: "))
intento = 1
intento = True
while intento == True:
    intento = intento + 1
    if intento < numero:
        print("Demasiado pequeño")
    elif intento == numero:
        print("¡Has ganado!")
    else:
        print("Demasiado grande ")

print("Has realizado ", intento, "intentos")



