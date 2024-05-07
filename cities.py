# El dato de entrada a su programa es una cadena de texto con el siguiente formato:                                                                                                        │
# <city>:<population>;<city>:<population>;<city>:<population>;....
# El objetivo es conseguir obtener un diccionario donde las claves sean las ciudadeses y los valores sean los 
# habitantes (como enteros).

ciudades = "Adeje:49_270;La Orotava:42_434;Los Silos:4644;Santa Úrsula:15_361;Tegueste:11_359"
diccionario = {}

for nombres in ciudades.split(";"):
    nombres = nombres.split(":")
    diccionario[nombres[0]] = int(nombres[1])
    
print(diccionario)