# Convierta un número decimal entero a su representación binaria (como string).
# No está permitido:
# • Utilizar la función bin()
# • Utilizar f-strings con formato binario

numero = 1
binario = ""

while numero > 0:
    digito = numero % 2
    
    binario = str(digito) + binario
    numero = numero // 2

print(binario)