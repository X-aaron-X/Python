# Dados dos vectores (listas) de la misma dimensión, utilice la función zip() para calcular su
# producto escalar.

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

resultado = sum(a * b for a, b in zip(v1, v2))

print("El resultado es: ", resultado)


