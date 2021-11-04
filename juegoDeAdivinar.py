print("¡Empezamos!")

import random
numero = random.randint(0, 100)
intentosRealizados = 0
intento = int(input("Adivina el número: "))

if intento == numero:
    print("Enhorabuena, has acertado el número. ")
while intento != numero : 
    if intento < 0 or intento > 100:
        intentosRealizados = intentosRealizados + 1
        print("Error; el número debe estar entre el 0 y el 99 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño ")
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande ")  
    intento = int(input("Introduce otro número: "))


#mensaje fuera
print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")
