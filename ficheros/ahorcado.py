"""
    Crea un ahorcado leyendolo las apalabras a adivinar de un fichero de texto
"""

import random

"""
Recupera una palabra aleatoria del archivo "data/ahorcado/palabras.txt".

Returns:
    str: Una palabra seleccionada al azar del archivo "palabras.txt", o una cadena vacía si el archivo está vacío.
"""
def cogerPlabraAleatoria() -> str:
    with open("data/ahorcado/palabras.txt", "r") as fichero:
        palabras = [linea.strip() for linea in fichero]
        
        if len(palabras) > 0:
            return random.choice(palabras)
            
        return ''

"""
Genera una cadena de guiones con la misma longitud que la cadena de entrada.

Args:
    palabra (str): La cadena de entrada para la cual se genera la palabra secreta.
    
Returns:
    str: Una cadena de guiones con la misma longitud que la cadena de entrada.
"""
def palabraSecreta(palabra: str) -> str:
    return '- ' * len(palabra)

"""
Recibe una palabra y una letra, y devuelve si la letra está presente en la palabra.

:param palabra: Una cadena que representa la palabra a verificar.
:param letra: Una cadena que representa la letra a buscar en la palabra.
:return: Un valor booleano que indica si la letra está presente en la palabra.
"""
def buscarpalabra(palabra: str, letra: str) -> bool:
    return letra in palabra

"""
Recibe una palabra, una letra y una palabra oculta, y devuelve una nueva palabra oculta con la letra en la posición correcta revelada.

:param palabra: Una cadena que representa la palabra que se va a revelar.
:param letra: Una cadena que representa la letra que se va a revelar.
:param palabraSecreta: Una cadena que representa la palabra oculta.
:return: Una cadena que representa la palabra oculta con la letra(s) en la posición(es) correcta(s) revelada(s).
"""
def pintarLetra(palabra: str, letra: str, palabraSecreta: str) -> str:
    nuevaPalabraSecreta = ''
    
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nuevaPalabraSecreta += letra + ' '
        else:
            nuevaPalabraSecreta += palabraSecreta[i*2] + ' '
    return nuevaPalabraSecreta.strip()

# MAIN
palabraAdivinar = cogerPlabraAleatoria()
palabraSecreta = palabraSecreta(palabraAdivinar)
intentosRestantes = 6;
ganador = False
letraIntroducida = []

if len(palabraAdivinar) == 0:
    print('No hay palabras en el fichero')

else:
    print('Juego del Ahorcado')
    print(f'La palabra a advininar tiene {len(palabraAdivinar)} letras')
    print(f'\nLa palabra a adivinar es: {palabraSecreta}')
    print(palabraAdivinar)

    while not ganador and intentosRestantes > 0:
        letra = input('\nIntroduce una letra: ').lower()
        
        if len(letra) > 1:
            print('Solo puedes introducir una letra')
            continue
        
        if letra in letraIntroducida:
            print(f'Ya has introducido esta letra "{letra}"')
            continue
        
        letraIntroducida.append(letra)

        if letra in palabraAdivinar:       
            palabraSecreta = pintarLetra(palabraAdivinar, letra, palabraSecreta)
        else:
            intentosRestantes -= 1

        if palabraSecreta.replace(" ", "") == palabraAdivinar:
            ganador = True
        else :
            print(f'Palabra Secreta: {palabraSecreta}')
            print(f'Intentos restantes: {intentosRestantes}')

    if ganador:
        print("Has ganado")
    else:
        print("\nHas perdido. La palabra era:", palabraAdivinar)