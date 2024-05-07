# Dado un número entero no negativo obtenga una lista con todas las potencias de 2 con el exponente variando desde 0hasta dicho valor (inclusive).
# ¿Podrías resolverlo también con listas por comprensión?

numero = 2

print([pow(2, i) for i in range(numero + 1)])