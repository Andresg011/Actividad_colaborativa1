#CONSTRUCTORES
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}")


# Crear objetos
coche1 = Coche("Kia", "Picanto", 2020)
coche2 = Coche("Toyota", "Fortuner", 2025)


# Mostrar información
coche1.describir()
coche2.describir()
