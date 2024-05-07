# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada uno 
# de los strings de la lista de entrada

lista = ['uno', 'dos', 'tres']
nuevaLista = []

for i in lista:
    for j in i:
        nuevaLista.append(j)

print(nuevaLista)