"""
Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. Por lo tanto hay que devolver el cambio. 
La tienda dispone de una serie concreta de monedas/billetes con un máximo de unidades de cada moneda/billete.
El objetivo del ejercicio es devolver el cambio al cliente empezando por la moneda/billete más grande y llegando hasta la más pequeña.

• Si el dinero es justo hay que devolver un diccionario vacío.                                                                                                                 │
• Si el cambio no es posible hay que devolver None
"""

aDevolver = 20
modendasDisponibles = {5: 3, 2: 7, 1: 3}
cambio = {}
monedaBillete = sorted(modendasDisponibles.keys(), reverse=True)

if aDevolver == 0:
    cambio = {}
else:
    i = 0
    
    while i < len(monedaBillete) and cambio != None:
        moneda = monedaBillete[i]
        
        if aDevolver >= moneda:
            cantidadMaxima = aDevolver // moneda
            
            cantidad = min(cantidadMaxima, modendasDisponibles[moneda])
            aDevolver -= cantidad * moneda
            
            cambio[moneda] = cantidad
        else:
            cambio = None
        
        i += 1
    
    if aDevolver != 0:
        cambio = None

print(cambio)



