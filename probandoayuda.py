print("""
    Vamos a jugar al juego de adivinar un número. 

    1) Nivel de dificultad simple (entre 0 y 100)

    2) Nivel de dificultad intermedio (entre 0 y 1.000)

    3) Nivel de dificultad avanzado (entre 0 y 1.000.000)

    4) Nivel de dificultad experto (entre 0 y 1.000.000.000.000)

    5) Nivel maestro IA

""")

nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 4 o IA: \n "))
if nivel > 5:
    print("\nError. Hay 5 posibles niveles. Seleccione de nuevo el nivel: ")
elif nivel < 1 :
    print("\nError. Hay 5 posibles niveles. Seleccione de nuevo el nivel: ")



nombre = str(input("Introduce tu nombre: "))
ayuda = str(input("¿Quiere jugar con una ayuda? \n Sí - Se muestra el número mínimo y máximo deducidos de las anteriores entradas \n No - rechazar \n "))

if ayuda == 1 and nivel ==1:
    print("bien")
if ayuda == 2 and nivel == 1:
    print("sin ayuda")
