# Dada una lista de entrada de valores numéricos y dado un número de referencia, obtenga una lista de dos listas,
# donde la primera lista contenga todos los números de la lista de entrada menores que el número de referencia y
# donde la segunda lista contenga todos los números de la lista de salida mayores o iguales que el número de referencia.                                                                                                         │
# Mantenga el mismo orden en el que vienen los números de la lista de entrada.

lista = [1, 2, 3]
numero = -10

nuevaLista = [[], []]

for numeros in lista:
    if numeros < numero:
        nuevaLista[0].append(numeros)
    else:
        nuevaLista[1].append(numeros)

print(nuevaLista)
