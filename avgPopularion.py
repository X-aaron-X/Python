# Partiendo de un diccionario de ciudades (claves) y poblaciones (valores) -suponiendo que estas ciudades son las
# únicas que existen en el planeta- calcule el porcentaje de población relativo de cada una de ellas con respecto al
# total, dando como salida un diccionario. Obtenga la media de población con una precisión de 3 decimales.

ciudades = {'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000}

totalPoblacion = sum(ciudades.values())

for indice, valor in ciudades.items():
    ciudades[indice] = round((valor / totalPoblacion) * 100, 3)

print(ciudades)