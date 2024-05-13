# ********************
# LEYENDO FICHEROS CSV
# ********************

"""
Dado un fichero de entrada en formato CSV, escriba un programa en Python que sea capaz de convertirlo a una lista de diccionarios.
• Si no hay valor para una determinada columna habrá que convertir a None.
• Si se encuentra un "True" o un "False" habrá que convertirlo al tipo booleano de Python.
• Si se encuentra un número habrá que convertirlo a tipo numérico de Python.
• Se puede asegurar que los números que aparezcan siempre van a ser enteros.
• Se puede asegurar que los ficheros de entrada siempre tendrán el nombre de las columnas en la primera fila.
"""
from pathlib import Path

def run(datafile: Path) -> list:
    # TU CÓDIGO AQUÍ
    data = 'output'
    
    fichero = open(datafile, 'r', encoding='utf-8')
    contenido = [item.rstrip('\n') for item in fichero.readlines()]    
    
    tipos = contenido[0].split(',')
    
    pokemons = []
    for indice in range(1, len(contenido)):
        pokemon = contenido[indice].split(',')
        
        for i in range(len(pokemon)):
            if pokemon[i] == 'True':
                pokemon[i] = True
            elif pokemon[i] == 'False':
                pokemon[i] = False
            elif pokemon[i].isdigit():
                pokemon[i] = int(pokemon[i])
            elif pokemon[i] == '':
                pokemon[i] = None
            else:
                pokemon[i] = pokemon[i]
        
        pokemons += [dict(zip(tipos, pokemon))]
    
    return pokemons

if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')