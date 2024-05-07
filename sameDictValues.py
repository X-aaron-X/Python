#  Acepte un diccionario como entrada y compruebe si todos sus valores son iguales o no.

diccionario = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
primerValor = ""
cont = 0

for valor in diccionario.values():
    if cont == 0:
        primerValor = valor
    else:
        if primerValor == valor:
            print(True)
            break
        else:
            print(False)
            break
    cont += 1