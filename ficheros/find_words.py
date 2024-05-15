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
    
    # Opcion 1
    with open(data_path, 'r', encoding='utf-8') as fichero:
        for numLinea, linea in enumerate(fichero, start = 1):         
            linea = linea.lower()
            palabras = linea.split()
            cont = 0
            
            for palabra in palabras:
                cont += len(palabra) + 1
                
                if palabra.rstrip(",)") == buscar:
                    matches.append((numLinea, cont - len(palabra)))
                elif palabra.startswith("'") and palabra[1:] == buscar:
                    matches.append((numLinea, cont - len(palabra) + 1))
            
    # Opcion 2            
    # fichero = open(data_path, 'r', encoding='utf-8')
    # contenido = [item.rstrip('\n').lower() for item in fichero.readlines()]
    # palabraTamano = len(buscar)
    
    # for numLinea, linea in enumerate(contenido, start=1):
    #     if buscar in linea:
    #         palabras = linea.split()
            
    #         cont = 0
    #         for palabra in palabras:
    #             cont += len(palabra) + 1
    #             parentesis = buscar + ')'
    #             coma = buscar + ','
    #             comillas = "'" +buscar
                
    #             if palabra == buscar or palabra == parentesis or palabra == coma:
    #                 matches.append((numLinea, cont - len(palabra)))
    #             elif palabra == comillas:
    #                 matches.append((numLinea, cont - (palabraTamano)))

    print(matches)

    return matches

if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'tás')