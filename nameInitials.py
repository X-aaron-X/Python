# Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha persona pasadas a mayúsculas y con punto al final.
# Notas:
# • El nombre puede tener uno o dos elementos.
# • El apellido puede tener uno o dos elementos.

nombreCompleto = "sánchez, María"
apellidos, nombre = nombreCompleto.split(", ")


if len(apellidos.split()) == 2:
    print(apellidos[0].upper() + "." + apellidos.split()[1][0].upper() + "." + nombre[0].upper() + ".")
else:
    print(nombre[0].upper() + "." + apellidos[0].upper() + ".")