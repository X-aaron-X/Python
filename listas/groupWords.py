# Dada una lista de palabras, agrúpelas por su letra inicial a través de un diccionario de listas.

listas = ['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor','carretera', 'arco']

diccionario = {}
letraInicial = ''

for palabra in listas:
    letraInicial = palabra[0]
    
    if letraInicial not in diccionario:
        diccionario[letraInicial] = [palabra]
    else:
        diccionario[letraInicial].append(palabra)
        
print(diccionario)