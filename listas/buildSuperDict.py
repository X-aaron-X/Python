# Dada lista de listas con varios elementos, obtenga un diccionario donde las claves serán los primeros 
# elementos de las sublistas y los valores serán los restantes (como listas).

listas = [['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]]
diccionario = {}

for lista in listas:    
    diccionario[lista[0]] = lista[1:]

print(diccionario)