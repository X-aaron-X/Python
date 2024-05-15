class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False
    
    def power_on(self):
        self.status = True
    
    def power_off(self):
        self.status = False
    
    def install_app(self, *apps):
        self.apps.extend(apps)
    
    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
        else:
            print(f"{app} no esta instalado")
        
    def __str__(self):
        return f'manufacturer: {self.manufacturer}\nscreen_size: {self.screen_size}\nnum_cores: {self.num_cores}\nstatus: {self.status}\napps: {self.apps}\n'
        
movil = MobilePhone('Samsung', 6.5, 8)
print(movil)

print(movil.status)
movil.power_on()
print(movil.status)

movil.install_app('Telegram', 'Whatsapp')
print(movil.apps)

movil.uninstall_app('Whatsapp')

print('\n', movil)