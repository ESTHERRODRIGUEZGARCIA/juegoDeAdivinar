def jugar_una_partida(numero, minimo, maximo):
    victoria = False
    while not victoria:
        victoria, minimo, maximo = jugar_una_vez(
            numero,
            minimo,
            maximo,
        )