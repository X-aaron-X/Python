# Dada una lista de valores numéricos enteros, obtenga su máximo valor.                                               │                                                                                                                   │
# Prohibido utilizar:                                                                                                 │                                                                                                                     │
#  • La función "built-in" min().                                                                                     │
#  • La función "built-in" max().                                                                                     │
#  • La función "built-in" sorted().

listado = [-7, -5, -5, -8, -3]
mayor = listado[0]

for i in listado:
    if i > mayor:
        mayor = i
        
print(mayor)