# Dada una lista de números enteros positivos y un número no negativo N, calcule el valor del elemento en la posición N elevado a N
# Ejemplo: [1, 2, 3, 4] y N=2, el resultado sería 9
# Ejemplo2: [1, 2, 3]y n=3, el resultado sería -1
# Ejemplo3: [10, 20, 30, 40, 50] y N=4, el resultado sería 6250000
# Notas:
# • Si N está fuera de rango, hay que devolver el valor -1.
# • N se representa por "power" en el parámetro de entrada.

lista = [1, 2, 3]
n = 3

if n < len(lista):
    print(pow(lista[n], n))