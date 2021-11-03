import random
numero = random.randint(0, 100)
intento = 0
intento = int(input("Adivina el número: "))
while intento != numero:
    intento = intento + 1
    if intento < numero:
        print("Demasiado pequeño")
    if intento > numero:
        print("Demasiado grande ")
    if intento == numero:
        break

if intento == numero:
    print("¡Has ganado!")

print("Has realizado ", intento, "intentos")



