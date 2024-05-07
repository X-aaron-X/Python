# Dado un diccionario cuyos valores son listas, genere un diccionario nuevo donde se borre el contenido de dichas listas.
# Resuelva el ejercicio utilizando diccionarios por comprensión.

dicconario = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

print({valores: [] for valores in dicconario})