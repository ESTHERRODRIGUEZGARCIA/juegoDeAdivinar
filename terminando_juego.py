
print("""
    Vamos a jugar al juego de adivinar un número. 

    1) Nivel de dificultad simple (entre 0 y 100)

    2) Nivel de dificultad intermedio (entre 0 y 1.000)

    3) Nivel de dificultad avanzado (entre 0 y 1.000.000)

    4) Nivel de dificultad experto (entre 0 y 1.000.000.000.000)

""")

nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 o 4: \n "))
if nivel > 4:
    print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")
elif nivel < 1 :
    print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")



if nivel == 1:
    print("¡Empezamos! Has elegido el nivel simple")

    import random
    numero = random.randint(0, 100)
    intentosRealizados = 0
    maxintento = 25
    
    intento = int(input("Adivine el número: \n"))

    if intento < 0 or intento > 100:
        intentosRealizados = intentosRealizados + 1
        print("Error, el número debe estar entre el 0 y el 99 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño. ")
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande. ")
    while intento != numero :
        print("Intenta adivinar el número: ")
        intento = int(input()) 
        if intentosRealizados > maxintento:
            print("Has superado el máximo de intentos. El número era: ", numero)
        else:
            print("")

        if intento < 0 or intento > 100:
            intentosRealizados = intentosRealizados + 1
            print("Error, el número debe estar entre el 0 y el 99 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño. ")
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande. ")

            if intento == numero:
                if intentosRealizados > maxintento:
                    print("Has superado el máximo de intentos. El número era: ", numero)
                else:
                    print("")
                break
    

#mensaje fuera
    -print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")