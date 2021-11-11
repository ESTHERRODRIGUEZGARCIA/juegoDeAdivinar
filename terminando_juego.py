
print("""
    1) nivel de dificultad simple (entre 0 y 100)
    2) nivel de dificultad intermedio (entre 0 y 1.000)
    3) nivel de dificultad avanzado (entre 0 y 1.000.000)
    4) nivel de dificultad experto (entre 0 y 1.000.000.000.000)
""")
nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 o 4: "))



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
