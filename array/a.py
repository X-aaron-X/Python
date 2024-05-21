"""
Dado un array 'a' de numeros enteros, crea u nuevo array 'b' que contena el cuadrado
de cada elemento de 'a'. Luego calcula la suma de todos los elementos 'b'.
"""
import numpy as np

# Definimos el array 'a'
a = np.array([[1, 2, 3, 4, 5]])

# Creamos el array 'b' con el cuadrado de cada elemento de 'a'
b = a ** 2

# Calculamos la suma de los elementos 'b'
suma_b = np.sum(b)

print("\nArray A: ", a)
print("Array B: ", b)
print("La suma de los elementos al cuadrado es: ", suma_b)
