from tkinter import *

window = Tk()
window.geometry('350x200')
window.configure(bg='lightblue')
window.title('Canvas - Dibujando Formas')
window.resizable(0,0)

canvas = Canvas(window, width=200, height=100, bg='white')
canvas.pack(pady = 30)

canvas.create_text(100, 50, text='Hola Mundo', fill='red')
canvas.create_oval(50, 25, 150, 75, fill='blue')

window.mainloop()





