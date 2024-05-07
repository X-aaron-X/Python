# Dada una lista de números, obtenga otra lista donde se eliminen los duplicados. 
# Mantenga el orden de los números en la lista de salida tal y como aparecen en la de entrada.

lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
listaFinal = []

for numero in lista:
    if numero not in listaFinal:
        listaFinal.append(numero)

print(listaFinal)