import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar comandos SQL
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos de ejemplo
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 25))

# Guardar los cambios
conn.commit()

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

# Cerrar la conexión
conn.close()
