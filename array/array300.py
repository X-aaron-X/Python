"""
Crea un array de numeros de un tamaño pasado por teclado, el array contendra numeros aleatorios entre 1 y 300 mostrar aquellos numeros
que acaben en un digito que mostramos le indiquemos por teclado (debes controlar que se introduce un numero entre 0 y 9), estos
debern guarderse en un nuevo array. Por ejemplo:
en un array de 10 posiciones e indicamos mostrar los numeros acabados en 5, podria salir 155, 25, etc
"""
import numpy as np

try:
    tamanio = int(input("Introduzca el tamaño del array: "))
except ValueError:
    print("Introduce un número")

array = np.random.randint(1, 300, tamanio)
repetir = True

while repetir:
    try:
        mostrar = int(input("Introduzca el número a mostrar (0-9): "))
        
        if 0 <= mostrar <= 9:
            repetir = False
        else:
            print("Introduce un número entre 0 y 9\n")
    except ValueError:
        print("Introduce un número\n")

print(array[array % 10 == mostrar])