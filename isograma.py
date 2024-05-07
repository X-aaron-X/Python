# Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
# • lumberjacks
# • background
# • downstream
# • six-year-old

palabra = "aaron"

isograma = len(set(palabra)) == len(palabra)

print("Es un isograma") if isograma else print("No es un isograma")