# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************

"""
Dado un fichero de texto y una palabra objetivo se pide indicar el número de línea y el número de columna en la que se encuentran 
todas las ocurrencias de dicha palabra en el fichero de entrada.
• La salida del programa será una lista de tuplas. Cada tupla contiene dos valores: el número de línea y el número de columna.
• Se puede suponer que las palabras se separan por un único espacio, pero hay que tener en cuenta la 
    posible existencia de lossiguientes caracteres como frontera de palabras: .,:;()'¡!-
• La búsqueda debe funcionar aunque no coincidan mayúsculas y minúsculas.
"""

from pathlib import Path

def run(data_path: Path, target_word: str) -> list:
    # TU CÓDIGO AQUÍ
    matches = []
    buscar = target_word.lower()
    
    fichero = open(data_path, 'r', encoding='utf-8')
    contenido = [item.rstrip('\n').lower() for item in fichero.readlines()]
    palabraTamano = len(buscar)
    
    for num_linea, linea in enumerate(contenido, start=1):
        if buscar in linea:
            palabras = linea.split()
            
            cont = 0
            for palabra in palabras:
                limpiando = palabra.strip(".,:;()'¡!-")
                
                cont += len(palabra) + 1
                parentesis = buscar + ')'
                coma = buscar + ','
                comillas = "'" +buscar

                if palabra == buscar or palabra == comillas:
                    matches.append((num_linea, cont - (palabraTamano - 1) - 1))
                elif palabra == parentesis or palabra == coma:
                    matches.append((num_linea, cont - (palabraTamano - 1) - 2))
            
    print(matches)
    
    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'tú')