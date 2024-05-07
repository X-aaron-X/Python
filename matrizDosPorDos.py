# Escriba un programa que permita multiplicar únicamente matrices de 2 filas por 2 columnas.
# Veamos un ejemplo concreto:

# El producto P = 𝐴 × 𝐵 se calcula siguiendo la multiplicación de matrices

a = [[6, 4], [8, 9]]
b = [[3, 2], [1, 7]]

producto = []

for i in range(len(a)):
    fila = []
    
    for j in range(len(b[0])):
        suma = 0
        
        for e in range(len(b)):
            suma += a[i][e] * b[e][j]
            
        fila.append(suma)
        
    producto.append(fila)

print(producto)