#HERENCIA VEHICULOS
# CLASE PADRE: Lo que todos los vehículos tienen en común
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 20
        print(f"El {self.marca} ahora va a {self.velocidad} km/h.")

# CLASE HIJA 1: Un Coche es un Vehículo
class Coche(Vehiculo):
    def __init__(self, marca, diesel):
        # Con super() le pedimos al padre que guarde la marca
        super().__init__(marca)
        self.tipo_diesel = diesel

    def usar_pito(self):
        print("¡piii pii! El coche está pitando.")

# CLASE HIJA 2: Una Bicicleta también es un Vehículo
class Bicicleta(Vehiculo):
    def __init__(self, marca, tiene_canasta):
        super().__init__(marca)
        self.tiene_canasta = tiene_canasta

    def usar_timbre(self):
        print("¡Ring ring! Cuidado con la bici.")

# Probando la Herencia 

mi_auto = Coche("toyota fortuner", "Diesel")
mi_auto.acelerar()  # Heredado del padre
mi_auto.usar_pito() # Propio de la hija

mi_bici = Bicicleta("Specialized", True)
mi_bici.acelerar()    # Heredado del padre
mi_bici.usar_timbre() # Propio de la hija
