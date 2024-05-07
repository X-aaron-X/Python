# Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de texto dada.
# NOTA: No se puede usar la función "count".

palabra = "tree"
contarLetras = {}

for letra in palabra:
    contarLetras[letra] = contarLetras.get(letra, 0) + 1
    
print(contarLetras)