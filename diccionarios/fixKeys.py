# A partir de un diccionario, obtenga un nuevo diccionario eliminando los espacios de sus claves respetando los valores correspondientes.

diccionario = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
nuevoDiccionario = {}

for clave in diccionario:
    nuevoDiccionario[clave.replace(' ', '')] = diccionario[clave]
    

print(nuevoDiccionario)