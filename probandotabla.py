from tabulate import tabulate

nombre= str(input("introduce tu nombre"))
table = [['Nombre', 'Nivel de dificultad', 'Puntuación'], [nombre, 'Doe', 28]]
print(tabulate(table))