# Usted es encargado de una empresa de merchandising y dispone de un cierto stock para los artículos. 
# El cliente hace un pedido especificando el artículo y la cantidad requerida.
# Usted debe comprobar si existe stock para la cantidad solicitada del artículo indicando True o False.

stock = {'pen': 20, 'cup': 11, 'keyring': 40}
merch = 'pen'
amount = 21
disponible = False

if stock[merch] >= amount:
    disponible = True
    

print(disponible)


