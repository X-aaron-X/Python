"""
Dadas dos cadenas de texto, obtenga una nueva cadena de texto con las letras consonantes que se repiten en ambas
frases. Ignore los espacios en blanco y muestre la cadena de salida con sus letras ordenadas.
Este ejercicio también se puede resolver mediante conjuntos por comprensión.
• Las vocales pueden estar en minúsculas o en mayúsculas.
• Una consonante minúscula es equivalente a una consonante mayúscula.
"""

text1 = 'Now is better thAn never'
text2 = 'Beautiful is better than ugly'
vocales = ' aeiou'
nuevaCadena = ''

letrasIguales = sorted(set(text1.lower()) & set(text2.lower()))

for letra in letrasIguales:
    if letra not in vocales:
        nuevaCadena += letra

print(nuevaCadena)