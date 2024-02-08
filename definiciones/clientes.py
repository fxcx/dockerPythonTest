
class Clientes : 
    def __init__(self, name, age, dni, email, address):
        self.name = name
        self.age = age
        self.dni = dni
        self.email = email
        self.address = address

    def __str__(self):
        return f"Nombre: {self.name} \nEdad: {self.age} \nDNI: {self.dni} \nEmail: {self.email}"
    
    

    