# Tenemos almacenadas las notas de un examen en un diccionario. Es necesario separar al alumnado que aprobó y al 
# que suspendió en dos diccionarios. Igualmente habrá que pasar a mayúsculas el nombre del alumnado que aprobó y 
# a minúsculas el nombre del alumnado que suspendió. Escriba un programa en Python que realice esta operación usando diccionarios
# por comprensión.

notasExamen = {'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1}
aprobados = {}
suspensos = {}

for alumno, nota in notasExamen.items():
    if nota >= 5:
        aprobados[alumno.upper()] = nota
    else:
        suspensos[alumno.lower()] = nota

print(aprobados)
print(suspensos)