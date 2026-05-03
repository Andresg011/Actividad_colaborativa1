# Clase base
class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando")


# Clase Coche
class Coche(Vehiculo):
    def acelerar(self):
        print("El coche acelera al pisar el pedal")


# Clase Bicicleta 
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta acelera al usar los pedales")


# Lista de objetos 
vehiculos = [Coche(), Bicicleta()]

for v in vehiculos:
    v.acelerar()