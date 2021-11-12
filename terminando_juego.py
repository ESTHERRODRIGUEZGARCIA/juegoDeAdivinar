
print("""
    Vamos a jugar al juego de adivinar un número. 
    1) Nivel de dificultad simple (entre 0 y 100)
    2) Nivel de dificultad intermedio (entre 0 y 1.000)
    3) Nivel de dificultad avanzado (entre 0 y 1.000.000)
    4) Nivel de dificultad experto (entre 0 y 1.000.000.000.000)
""")

nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 o 4: "))

if nivel == 1:
    print("¡Empezamos!")

    import random
    numero = random.randint(0, 100)
    intentosRealizados = 0
    maxintento = 10
    intento = int(input("Introduce un número; tienes 10 intentos: "))

if intento < 0 or intento > 100:
    intentosRealizados = intentosRealizados + 1
    print("Error; el número debe estar entre el 0 y el 99 ")
if intento < numero:
    intentosRealizados = intentosRealizados + 1
    print("Demasiado pequeño ")
if intento > numero:
    intentosRealizados = intentosRealizados + 1
    print("Demasiado grande ")
while intento != numero :
    print("Intenta adivinar el número: ")  
intento = int(input())
if intento == numero:
        break

    #mensaje fuera
    print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")

elif nivel == 2:
    print("¡Empezamos!")

    import random
    numero = random.randint(0, 1000)
    intentosRealizados = 0
    intento = int(input("Introduce un número: "))

    if intento == numero:
        print("Enhorabuena, has acertado el número. ")
    while intento != numero : 
        if intento < 0 or intento > 1000:
            intentosRealizados = intentosRealizados + 1
            print("Error; el número debe estar entre el 0 y el 1000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño ")
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande ")  
        intento = int(input("Introduce otro número: "))

        #mensaje fuera
    print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")

elif nivel == 3:
    print("¡Empezamos!")

    import random
    numero = random.randint(0, 1000000)
    intentosRealizados = 0
    intento = int(input("Introduce un número: "))

    if intento == numero:
        print("Enhorabuena, has acertado el número. ")
    while intento != numero : 
        if intento < 0 or intento > 1000000000000:
            intentosRealizados = intentosRealizados + 1
            print("Error; el número debe estar entre el 0 y el 1000000000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño ")
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande ")  
        intento = int(input("Introduce otro número: "))


        #mensaje fuera
    print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")

else:
    print("¡Empezamos!")

    import random
    numero = random.randint(0, 1000000000000)
    intentosRealizados = 0
    intento = int(input("Introduce un número: "))

    if intento == numero:
        print("Enhorabuena, has acertado el número. ")
    while intento != numero : 
        if intento < 0 or intento > 1000000000000:
            intentosRealizados = intentosRealizados + 1
            print("Error; el número debe estar entre el 0 y el 1000000000000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño ")
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande ")  
        intento = int(input("Introduce otro número: "))

        #mensaje fuera
    print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")

