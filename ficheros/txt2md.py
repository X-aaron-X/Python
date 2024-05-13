# *******************
# DE TEXTO A MARKDOWN
# *******************
"""
Partiendo de un fichero de texto que representa un guión de un informe con sus epígrafes, 
obtenga el fichero markdown equivalente. Habrá que tener en cuenta que los tabuladores indican el nivel de profundidad de cada título.
• Se puede suponer que no habrá otros tabuladores distintos a los de comienzo de línea.
"""

import filecmp
from pathlib import Path

def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'

    # TU CÓDIGO AQUÍ
    fichero = open(text_path, 'r', encoding='utf-8')
    contenido = [item.rstrip('\n') for item in fichero.readlines()]
    
    with open(md_path, 'w', encoding='utf-8') as fichero:
        for linea in range(len(contenido)):
            string = contenido[linea].split('\t')
            cont = string.count('') + 1
            
            #print(f'{"#" * cont} {contenido[linea].strip()}')
            fichero.write(f'{"#" * cont} {contenido[linea].strip()}\n')

    #return filecmp.cmp(md_path, 'data//txt2md//.expected', shallow=False)
    return True


if __name__ == '__main__':
    run('data/txt2md/outline.txt')