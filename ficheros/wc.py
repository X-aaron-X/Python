# ****************
# CONTANDO COMO WC
# ****************
"""
"wc" es una utilidad super conocida en sistemas Linux. Nos permite contar el número de líneas, palabras y bytes que hay en un fichero.
Escriba un programa en Python que simule el mismo comportamiento, recibiendo una ruta a un fichero y devolviendo esas tres variables.
• Considerar únicamente el espacio en blanco como delimitador de palabras.
• El número de bytes que ocupa un string "s" se puede calcular con: len(s.encode('utf-8'))
• Ojo con las líneas en blanco, pueden llevarle a un resultado incorrecto.
"""

from pathlib import Path

def run(input_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    num_lines = num_words = num_bytes = 'output'
    
    fichero = open(input_path, 'r', encoding='utf-8')
    contenido = fichero.read()

    num_lines = contenido.count('\n')
    num_words = len(contenido.split())
    num_bytes = len(contenido.encode('utf-8'))

    return num_lines, num_words, num_bytes

if __name__ == '__main__':
    run('data/wc/lorem.txt')
    #run('data/wc/emojis.txt')