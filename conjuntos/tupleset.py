"""
Dada una tupla de duplas (2 valores) obtenga una tupla con dos conjuntos:
• El primer conjunto con los primeros valores de cada dupla.
• El segundo conjunto con los segundos valores de cada dupla.
Ejemplo1: ((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)) => ({8, 9, 4, 7}, {1, 2, 3, 5})
Ejemplo2: ((1, 2), ('|', '@'), ('!', '"')) => ({'|', 1, '!'}, {'"', 2, '@'})
"""
entrada = ((4, 3), (8, 2), (7, 5), (8, 2), (9, 1))

tupla1 = set()
tupla2 = set()

for tupla in entrada:
    tupla1.add(tupla[0])
    tupla2.add(tupla[1])
    
print(tupla1, tupla2)