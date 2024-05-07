"""
Ejercicio Python
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán 
en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos 
del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente
(2) Eliminar cliente
(3) Mostrar cliente
(4) Listar todos los clientes
(5) Listar clientes preferentes
(6) Terminar.

En función de la opción elegida el programa tendrá que hacer lo siguiente:
1.	Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2.	Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3.	Preguntar por el NIF del cliente y mostrar sus datos.
4.	Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5.	Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6.	Terminar el programa.
"""
clientes = {}
opciones = ""

while opciones != "6":
    opciones = input("Introduce una opción (1-6):\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar.\n")
    
    match opciones:
        case "1":
            nif = input("\nIntroduce el NIF del cliente: ")
            clientes[nif] = {}
            
            nombre = input("\nIntroduce el nombre del cliente: ")
            clientes[nif]["nombre"] = nombre
            
            direccion = input("\nIntroduce la dirección del cliente: ")
            clientes[nif]["direccion"] = direccion
            
            telefono = input("\nIntroduce el telefono del cliente: ")
            clientes[nif]["telefono"] = telefono
            
            correo = input("\nIntroduce el correo del cliente: ")
            clientes[nif]["correo"] = correo
            
            preferente = ""
            while preferente != "s" and preferente != "n":
                preferente = input("\n¿Es un cliente preferente? (s/n): ")
            
                if preferente == "s":
                    clientes[nif]["preferente"] = True
                elif preferente == "n":
                    clientes[nif]["preferente"] = False
                else:
                    print("\nOpción incorrecta\n")
        case "2":
            nif = input("\nIntroduce el NIF del cliente: ")
            
            if nif in clientes:
                del clientes[nif]
            else:
                print("\nEl cliente no existe\n")
        case "3":
            nif = input("\nIntroduce el NIF del cliente: ")
            
            if nif in clientes:
                print(f"\n{clientes[nif]}\n")
            else:
                print("\nEl cliente no existe\n")
        case "4":
            if len(clientes) == 0:
                print("\nNo hay clientes\n")
            else:
                print(f"\n{clientes}\n")
        case "5":
            if len(clientes) == 0:
                print("\nNo hay clientes\n")
            else:
                for cliente in clientes:
                    if clientes[cliente]['preferente']:
                        print(f"\n{clientes[cliente]}\n")
        case "6":
            print("Adios")
        case _:
            print("\nOpción incorrecta\n")
            


