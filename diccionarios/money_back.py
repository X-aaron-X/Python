# Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. 
# Por lo tanto hay que devolver el cambio. La tienda dispone de una serie concreta de monedas/billetes. El objetivo del ejercicio 
# es devolver el cambio al cliente empezando por la moneda/billete más grande y llegando hasta la más pequeña.
# • Si el dinero es justo hay que devolver un diccionario vacío.
# • Si el cambio no es posible hay que devolver None
aDevolver = 0
monedasDisponibles = [5, 2, 0.5]
cambio = {}

i = 0
while i < len(monedasDisponibles) and cambio != None:
    moneda = sorted(monedasDisponibles, reverse=True)[i]

    if aDevolver >= moneda:
        cambio[moneda] = aDevolver // moneda
        aDevolver %= moneda
    elif aDevolver >= 0:
        cambio = None
        
    i += 1

print(cambio)

