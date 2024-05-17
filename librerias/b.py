#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Librerías Tkinter")

canvas = Canvas(root,height=500,width=500)

canvas.create_oval(50,50,100,100,fill="red",width=5)
canvas.create_oval(50,50,100,100,fill="white",width=5)

canvas.create_oval(100,100,200,200,fill="red",width=5)
canvas.create_oval(200,200,300,300,fill="red",width=5)
# canvas.create_rectangle(150,150,250,250,fill="blue")
canvas.pack()

#Bucle de ejecución
root.mainloop()