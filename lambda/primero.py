# def areaTriangulo(base: float, altura: float) -> float:
#     return (base * altura) / 2

areaTriangulo = lambda base, altura: (base * altura) / 2

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

print(areaTriangulo(base, altura))