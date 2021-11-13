print("""
    Vamos a jugar al juego de adivinar un número. 

    1) Nivel de dificultad simple (entre 0 y 100)

    2) Nivel de dificultad intermedio (entre 0 y 1.000)

    3) Nivel de dificultad avanzado (entre 0 y 1.000.000)

    4) Nivel de dificultad experto (entre 0 y 1.000.000.000.000)

    5) Nivel maestro IA

""")

nivel = int(input("Seleccione un nivel de dificultad, 1 2 3 4 o IA: \n "))


if nivel < 1 or nivel > 4 and nivel != 5:
    print("Error, el número debe estar entre el 0 y el 4 ")
if nivel ==1 or nivel == 4 or nivel == 2 or nivel == 3:
    print(" correcto")
if nivel == 5:
    print("tontita no lo sabes hacer")
while nivel < 1 or nivel > 4:
    print("Introduce otro nivel: ")
    nivel = int(input()) 
    if nivel < 1 or nivel > 4:
        print("Error, el número debe estar entre el 0 y el 4 ")
    if nivel == 1 or nivel == 4 or nivel == 2 or nivel == 3:
        print(" correcto")
    if nivel == 5:
        print("tontita no lo sabes hacer")
            
        if nivel ==1 or nivel == 4 or nivel == 2 or nivel == 3:
                break
if nivel ==1 or nivel == 4 or nivel == 2 or nivel == 3:
    print(" ")
    