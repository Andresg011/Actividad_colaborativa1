# Clase 
class Coche:
    def __init__(self,marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def describir(self):
        print(f"coche:{self.marca} {self.modelo} {self.año}")

# Objetos
Coche1 = Coche("Mazda", "3", 2021)
Coche2 = Coche("Volkswagen", "Jetta", 2022)
Coche3 = Coche("Kia", "Sportage", 2023)
Coche4 = Coche("Nissan", "Versa", 2020)
Coche5 = Coche("Hyundai", "Tucson", 2022)

# Descripción objetos
Coche1.describir()
Coche2.describir()
Coche3.describir()
Coche4.describir()
Coche5.describir()




