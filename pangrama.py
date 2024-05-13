palabra = "Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol."

# opcion 1
# if len(set(palabra.lower().replace(" ", ""))) == 27:  # 27 letras en el alfabeto español
#     print("Es un pangrama")
# else:
#     print("No es un pangrama")

# Opcion 2
faltantes = set("abcdefghijklmnopqrstuvwxyz") - set(palabra.lower())

if faltantes:
    print("No es un pangrama")
    print("Faltan las letras", ''.join(sorted(faltantes)))
else:
    print("Es un pangrama")