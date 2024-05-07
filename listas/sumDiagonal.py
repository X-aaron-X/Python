# Escriba un programa en Python que acepte una lista de listas representando una matriz numérica de valores enteros y 
# compute la suma de los elementos de la diagonal principal.
# Notas:
# • Si no se trata de una Matriz cuadrada devuelva None.
# • Puede afrontar el ejercicio en versión clásica o con listas por comprensión. ¡O incluso ambas!

lista = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]

if len(lista) == len(lista[0]):
    suma = 0
    
    for i in range(len(lista)):
        suma += lista[i][i]
        
    print(suma)
else:
    print(None)