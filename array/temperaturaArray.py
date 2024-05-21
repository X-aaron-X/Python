"""
Crea una funcion que rellene una matriz de 12x30 con las temperaturas de Alpelandia. 
Se rellenara con doubles con valores entre 0 y 35. Una vez hecho esto se pedira un numero de mes al usuario y mostrara las temperaturas de ese mes.
"""
import numpy as np

def rellenarArray(filas: int = 12, columnas: int = 30)->np.ndarray:
    return np.random.uniform(0, 35, size=(filas, columnas))

def verTemperaturas(array: np.ndarray, mes: int)->None:
    if 1 <= mes <= 12:
        print(f"Las temperaturas de Alpelandia en el mes {mes} son:\n")
        print(array[mes-1])
    else:
        print("El mes ingresado no es válido. Por favor, ingrese un número entre 1 y 12.")

def pedirMes()->int:
    while True:
        mes = int(input("Ingrese el número del mes (1-12): "))
        
        if 1 <= mes <= 12:
            return mes
        else:
            print("Por favor, ingrese un número entre 1 y 12.")

array = rellenarArray()
mes = pedirMes()

verTemperaturas(array, mes)

