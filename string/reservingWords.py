# Dado un string que contiene palabras separadas por espacio, obtenga otro string donde las palabras estén en orden
# inverso. En la cadena de salida todo el texto debe quedar en minúsculas.

palabra = "último caso de comprobación"

palabras = palabra.split()
palabraInvertida = " ".join(palabras[::-1])

print(palabraInvertida.lower())