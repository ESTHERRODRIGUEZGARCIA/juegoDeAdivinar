
print("""
    Vamos a jugar al juego de adivinar un número. 

    1) Nivel de dificultad simple (entre 0 y 100)

    2) Nivel de dificultad intermedio (entre 0 y 1.000)

    3) Nivel de dificultad avanzado (entre 0 y 1.000.000)

    4) Nivel de dificultad experto (entre 0 y 1.000.000.000.000)

    5) Nivel IA, Inteligencia Artificial*

""")

nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 o 4: \n "))
if nivel > 4 and nivel != 5:
    print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")
elif nivel < 1 :
    print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")
elif nivel == 5:
    print("\nLo sentimos, nivel bloqueado temporalmente por falta de conocimientos.")
while nivel > 4 and nivel < 1:
    if nivel > 4 and nivel != 5:
        print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")
    elif nivel < 1 :
        print("\nError. Hay 4 posibles niveles. Seleccione de nuevo el nivel: ")
    elif nivel == 5:
        print("\nLo sentimos, nivel bloqueado temporalmente por falta de conocimientos.")
    elif nivel < 4 and nivel > 1:
        print(" ")
    


nivel = int(input(" 1 2 3 o 4: \n "))

nombre= str(input("Introduce tu nombre: "))


if nivel == 1:
    print("\n¡Empezamos! Has elegido el nivel SIMPLE")

    import random
    numero = random.randint(0, 100)
    intentosRealizados = 0
    maxintento = 25
    
    intento = int(input("Adivine el número, entre 0 y 100: \n"))

    if intento < 0 or intento > 100:
        intentosRealizados = intentosRealizados + 1
        print("Error, el número debe estar entre el 0 y el 100 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño. El número es mayor que ", intento)
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande. El numero es menor que ", intento)
    while intento != numero and intentosRealizados < maxintento:
        print("Intenta adivinar el número: ")
        intento = int(input()) 
        if intento < 0 or intento > 100:
            intentosRealizados = intentosRealizados + 1
            print("Error, el número debe estar entre el 0 y el 100 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño. El número es mayor que ", intento)
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande. El número es menor que ", intento)

            if intento == numero:
                    break
    if intentosRealizados == maxintento:
        print("Has superado el máximo de intentos. El número era: ", numero)
    else:
        print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")
        

if nivel == 2:
    print("\n¡Empezamos! Has elegido el nivel INTERMEDIO")

    import random
    numero = random.randint(0, 1000)
    intentosRealizados = 0
    maxintento = 25
    
    intento = int(input("Adivine el número, entre 0 y 1000: \n"))

    if intento < 0 or intento > 1000:
        intentosRealizados = intentosRealizados + 1
        print("Error, el número debe estar entre el 0 y el 1000 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño. El número es mayor que ", intento)
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande. El número es menor que ", intento)
    while intento != numero and intentosRealizados < maxintento:
        print("Intenta adivinar el número: ")
        intento = int(input()) 
        if intento < 0 or intento > 1000:
            intentosRealizados = intentosRealizados + 1
            print("Error, el número debe estar entre el 0 y el 1000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño. El número es mayor que ", intento)
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande. El número es menor que ", intento)

            if intento == numero:
                    break
    if intentosRealizados == maxintento:
        print("Has superado el máximo de intentos. El número era: ", numero)
    else:
        print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")


if nivel == 3:
    print("\n¡Empezamos! Has elegido el nivel AVANZADO")

    import random
    numero = random.randint(0, 1000000)
    intentosRealizados = 0
    maxintento = 25
    
    intento = int(input("Adivine el número, entre 0 y 1.000.000: \n"))

    if intento < 0 or intento > 1000000:
        intentosRealizados = intentosRealizados + 1
        print("Error, el número debe estar entre el 0 y el 1.000.000 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño. El número es mayor que ", intento)
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande. El número es menor que ", intento)
    while intento != numero and intentosRealizados < maxintento:
        print("Intenta adivinar el número: ")
        intento = int(input()) 
        if intento < 0 or intento > 1000000:
            intentosRealizados = intentosRealizados + 1
            print("Error, el número debe estar entre el 0 y el 1.000.000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño. El número es mayor que ", intento)
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande. El número es menor que ", intento)

            if intento == numero:
                    break
    if intentosRealizados == maxintento:
        print("Has superado el máximo de intentos. El número era: ", numero)
    else:
        print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")



if nivel == 4:
    print("\n¡Empezamos! Has elegido el nivel EXPERTO")

    import random
    numero = random.randint(0, 1000000000000)
    intentosRealizados = 0
    maxintento = 25
    
    intento = int(input("Adivine el número, entre 0 y 1.000.000.000.000: \n"))

    if intento < 0 or intento > 1000000000000:
        intentosRealizados = intentosRealizados + 1
        print("Error, el número debe estar entre el 0 y el 1.000.000.000.000 ")
    if intento < numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado pequeño. El número es mayor que ", intento)
    if intento > numero:
        intentosRealizados = intentosRealizados + 1
        print("Demasiado grande. El número es menor que ", intento)
    while intento != numero and intentosRealizados < maxintento:
        print("Intenta adivinar el número: ")
        intento = int(input()) 
        if intento < 0 or intento > 1000000000000:
            intentosRealizados = intentosRealizados + 1
            print("Error, el número debe estar entre el 0 y el 1.000.000.000.000 ")
        if intento < numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado pequeño. El número es mayor que ", intento)
        if intento > numero:
            intentosRealizados = intentosRealizados + 1
            print("Demasiado grande. El número es menor que ", intento)

            if intento == numero:
                    break
    if intentosRealizados == maxintento:
        print("Has superado el máximo de intentos. El número era: ", numero)
    else:
        print("¡Enhorabuena! Has acertado el número. Has realizado ", intentosRealizados, "intentos.")

from tabulate import tabulate

table = [['Nombre', 'Nivel de dificultad', 'Intentos'], [nombre, nivel, intentosRealizados]]
print(tabulate(table))
