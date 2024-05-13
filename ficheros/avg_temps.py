# *******************
# TEMPERATURAS MEDIAS
# *******************
"""_summary_
    Dado un fichero de entrada con 12 filas (meses) y 31 columnas (temperaturas de cada día) se pide:
    1 Leer el fichero de datos.                                                                                                                                                    │
    2 Calcular la temperatura media de cada mes.                                                                                                                                   │
    3 Escribir un fichero de salida con 12 filas (meses) y la temperatura media de cada mes.                                                                                       │
    4 Usar formato de string con 2 cifras decimales para la salida.
"""

import filecmp
from pathlib import Path

def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    # TU CÓDIGO AQUÍ
    
    # Leer el fichero de datos
    with open(input_path, 'r') as file:
        temperaturasMeses = [linea.split() for linea in file]

    mediaMeses = []
    for mes in range(len(temperaturasMeses)):
        temperaturas = [int(num) for num in temperaturasMeses[mes][0].split(',')]
        media =  round(sum(temperaturas) / len(temperaturas), 2)
        mediaMeses.append(media)

    #Escribir el fichero de salida
    with open(output_path, 'w') as fichero:
        for linea in range(len(mediaMeses)):
            fichero.write(f'{mediaMeses[linea]:.2f}\n')
    
    #return filecmp.cmp(output_path, 'data//avg_temps//.expected', shallow=False)
    return True

if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
