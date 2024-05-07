# Dada una lista de entrada, devuelva True si todos sus elementos son iguales o False en otro caso.

lista = ['a', 'b', 'c']

print(True) if len(set(lista)) == 1 else print(False)