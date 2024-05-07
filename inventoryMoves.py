# Somos responsables del inventario de una empresa. A final de mes nos llega una cadena de texto indicando 
# los movimientos del inventario. Esta cadena de texto tiene el formatosiguiente:
# <mov_art>,<mov_art>,<mov_art>,...
# El objetivo es saber el estado final del inventario de cada artículo a través de un diccionario donde las claves
# son los artículos y los valores son la cantidad de artículos existentes.
# Notas:
# • El inventario puede quedar en números negativos.
# • Los nombres de los artículos son letras (cadenas de texto de 1 caracter).
# • Las modificaciones de inventario siempre son números enteros (pueden ser negativos).

imoves = 'X2,Y9,Z3,Y-2,Z-4,Y3,X-8,W5'
diccionario = {}

for inventario in imoves.split(','):
    diccionario[inventario[0]] = diccionario.get(inventario[0], 0) + int(inventario[1:])
    
print(diccionario)
