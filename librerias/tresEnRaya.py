import tkinter as tk
from tkinter import messagebox
from tkinter import font
class TresEnRaya:
    """
        Inicializa la clase del juego Tres en Raya.
        
        Args:
            root: La ventana principal de la aplicación.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")  # Establece el título de la ventana
        self.turno = "X"  # Establece que el primer turno es del jugador "X"
        self.font = font.Font(size=32, weight='bold')  # Define la fuente para los botones del juego
        self.label_font = font.Font(size=16, weight='bold')  # Define la fuente para las etiquetas de los contadores
        self.botones = [[None for _ in range(3)] for _ in range(3)]  # Crea una matriz 3x3 para los botones del juego
        self.ganador_x = 0  # Inicializa el contador de victorias del jugador "X"
        self.ganador_o = 0  # Inicializa el contador de victorias del jugador "O"
        self.crear_widgets()  # Llama a la función para crear los widgets de la interfaz
        self.root.configure(bg='#D4F1F4')  # Establece el color de fondo de la ventana

    """
        Crea y configura los widgets de la interfaz gráfica del juego.
    """
    def crear_widgets(self):
        # Crea y configura la etiqueta para el contador del jugador "X"
        self.contador_x = tk.Label(self.root, text=f"Jugador X: {self.ganador_x}", font=self.label_font, bg='#D4F1F4', fg='#FF6F61', pady=10)
        self.contador_x.grid(row=0, column=0, columnspan=3)
        
        # Crea y configura la etiqueta para el contador del jugador "O"
        self.contador_o = tk.Label(self.root, text=f"Jugador O: {self.ganador_o}", font=self.label_font, bg='#D4F1F4', fg='#6B5B95', pady=10)
        self.contador_o.grid(row=1, column=0, columnspan=3)
        
        self.inicializar_botones()  # Llama a la función para inicializar los botones del tablero de juego

    """
        Crea y configura los botones del tablero de juego.
    """
    def inicializar_botones(self):
        # Crea y configura los botones del tablero de juego
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.root, text="", width=5, height=2, font=self.font, command=lambda i=i, j=j: self.pulsar_boton(i, j), bg='#F9F9F9', fg='black', activebackground='#A8D5E2', relief='flat', bd=5)
                boton.grid(row=i + 2, column=j, padx=5, pady=5)
                self.botones[i][j] = boton

    """
        Maneja el evento de clic en un botón del tablero.
        
        Args:
            i: Índice de fila del botón.
            j: Índice de columna del botón.
    """
    def pulsar_boton(self, i, j):
        # Maneja el evento de pulsar un botón del tablero
        if self.botones[i][j]['text'] == "":
            self.botones[i][j]['text'] = self.turno  # Establece el texto del botón como el símbolo del turno actual
            if self.turno == "X":
                self.botones[i][j].config(fg='#FF6F61')  # Cambia el color del texto del botón si es el turno de "X"
            else:
                self.botones[i][j].config(fg='#6B5B95')  # Cambia el color del texto del botón si es el turno de "O"
                
            ganadoras = self.verificar_ganador(i, j)  # Verifica si hay un ganador después de esta jugada
            if ganadoras:
                for (x, y) in ganadoras:
                    self.botones[x][y].config(bg='#88B04B')  # Cambia el fondo de los botones ganadores
                self.actualizar_contador()  # Actualiza el contador del jugador ganador
                
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turno} ha ganado!")  # Muestra un mensaje indicando el ganador
                self.fin_del_juego()  # Maneja el final del juego
            elif self.tablero_lleno():
                messagebox.showinfo("Fin del juego", "¡Empate!")  # Muestra un mensaje indicando un empate
                self.fin_del_juego()  # Maneja el final del juego
            else:
                self.turno = "O" if self.turno == "X" else "X"  # Cambia el turno al otro jugador
    
    """
        Verifica si todos los botones del tablero están llenos.
        
        Returns:
            True si el tablero está lleno, False de lo contrario.
    """
    def tablero_lleno(self):
        # Verifica si todos los botones del tablero están llenos
        return all(self.botones[i][j]['text'] != "" for i in range(3) for j in range(3))

    """
        Verifica si hay una línea ganadora después de la última jugada.
        
        Args:
            i: Índice de fila de la última jugada.
            j: Índice de columna de la última jugada.
        
        Returns:
            La línea ganadora si existe, None de lo contrario.
    """
    def verificar_ganador(self, i, j):
        # Verifica si hay una línea ganadora
        lineas = [
            [(i, col) for col in range(3)],  # Fila
            [(row, j) for row in range(3)],  # Columna
            [(idx, idx) for idx in range(3)],  # Diagonal principal
            [(idx, 2 - idx) for idx in range(3)]  # Diagonal secundaria
        ]
        
        for linea in lineas:
            if all(self.botones[x][y]['text'] == self.turno for x, y in linea):
                return linea  # Retorna la línea ganadora si existe
        return None

    """
        Actualiza el contador de victorias del jugador ganador y actualiza la etiqueta correspondiente en la interfaz.
    """
    def actualizar_contador(self):
        # Actualiza el contador del jugador ganador
        if self.turno == "X":
            self.ganador_x += 1
            self.contador_x.config(text=f"Jugador X: {self.ganador_x}")
        else:
            self.ganador_o += 1
            self.contador_o.config(text=f"Jugador O: {self.ganador_o}")

    """
        Maneja el final del juego, preguntando al usuario si desea jugar otra vez.
    """
    def fin_del_juego(self):
        # Pregunta al usuario si quiere jugar otra vez y maneja la respuesta
        if messagebox.askyesno("Fin del juego", "¿Quieres jugar otra vez?"):
            self.reiniciar_juego()
        else:
            self.root.quit()

    """
        Reinicia el tablero y los contadores para un nuevo juego.
    """
    def reiniciar_juego(self):
        # Reinicia el tablero para un nuevo juego
        self.turno = "X"
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text="", fg='black', bg='#F9F9F9')

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de la aplicación
    app = TresEnRaya(root)  # Crea una instancia del juego TresEnRaya
    root.mainloop()  # Inicia el bucle principal de eventos de Tkinter
