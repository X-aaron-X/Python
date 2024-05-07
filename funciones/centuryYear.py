anno = int(input("Introduce el año: "))

"""
Calcula el siglo de un año.

Args:
    anno (int): El año para el cual se desea calcular el siglo.

Returns:
    int: El siglo del año dado.
"""
def calcularSiglo(anno: int):
    siglo = (anno - 1) // 100 + 1
    return siglo

siglo = calcularSiglo(anno)

print(siglo)