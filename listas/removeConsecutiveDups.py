# Dada una lista, genere otra lista eliminando los elementos duplicados consecutivos.

lista = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
i = 0

while i < len(lista) - 1:
    if lista[i] == lista[i + 1]:
        lista.pop(i + 1)
    else:
        i += 1

print(lista)