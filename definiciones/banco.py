from datetime import datetime

class Banco :
    def __init__(self, name, tarjetas, sucursales):
        self.name = name
        self.tarjetas = tarjetas
        self.sucursales = sucursales
        self.date = datetime.now()
   

    def options(name):
        return f"bienbenido a tu banco {name}"
    
    def depositar_money(deposito,sucursales,date):
        return  f"se deposito la cantidad {deposito} en la sucursal {sucursales} a las {date}"
    
    
