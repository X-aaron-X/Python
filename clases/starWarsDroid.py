class Droid:
    def __init__(self, name='John'):
        self.name = name
        self.encendido = False
    
    def __init__(self, name: str):
        self.name = name
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print(f"Hola, soy un androide. {self.name}. ¿Puedo ayudarte?")
    
    def apagar(self):
        self.encendido = False
        print("Adios! Me voy a dormir")

k2so = Droid('C-3PO')

print(k2so.encender())
print(k2so.encendido)

print(k2so.apagar())
print(k2so.encendido)