"""
De todas las posibles tiradas de dos dados, agupar aquellas tirdas que tengan el mismo valor
"""

resultado = {}

for d1 in range(1, 7):
    for d2 in range(1, 7):
        sumaDados = d1 + d2
        
        if sumaDados not in resultado:
            resultado[sumaDados] = []
            
        resultado[sumaDados].append([d1, d2])

for suma, tiradas in resultado.items():
    print(f"{suma} : {tiradas}")