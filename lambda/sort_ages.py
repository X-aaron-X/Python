# ********************
# ORDENANDO POR EDADES
# ********************
"""
Dada una lista que representa a personas y cuyos elementos son diccionarios, se pide ordenar la lista por el campo age de cada diccionario.
Utilice la función predefinida sorted()
"""

def run(people: list) -> list:
    # TU CÓDIGO AQUÍ
    speople = sorted(people, key = lambda yearOrdenado: yearOrdenado['age'])

    return speople

if __name__ == '__main__':
    run([{'name': 'DeRozan', 'age': 33}, {'name': 'Lonzo', 'age': 25}, {'name': 'Beverly', 'age': 34}, {'name': 'Dragic', 'age': 36}, {'name': 'Williams', 'age': 21}])