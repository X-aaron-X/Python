# Dada una lista - que puede contener sublistas (con sólo en 1 nivel de anidamiento) - genere otra lista "aplanada".

lista = [[1], [2], [3], [4]]

aplanada = []

for i in lista:
    if isinstance(i, list):
        for j in i:
            aplanada.append(j)
    else:
        aplanada.append(i)

print(aplanada)
