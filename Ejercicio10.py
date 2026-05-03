class ExcesoVelocidadException(Exception):
    def __init__(self, velocidad, limite):
        self.velocidad = velocidad
        self.limite = limite
        super().__init__(f"¡Exceso de velocidad! Velocidad actual: {velocidad} km/h, límite permitido: {limite} km/h\n")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > 200:
            raise ExcesoVelocidadException(nueva_velocidad, 200)

        self.velocidad = nueva_velocidad
        print(f"El coche {self.marca} {self.modelo} aceleró a {self.velocidad} km/h")

    def describir(self):
        print(f"El coche es un {self.marca} {self.modelo} con velocidad actual de {self.velocidad} km/h\n")

print("---Demostración de Excepción Personalizada---\n")

coche = Coche("audi", "A4")
coche.describir()
try:
    print("\nIntentando acelerar 80 km/h...")
    coche.acelerar(80)

    print("\nIntentando acelerar otros 80 km/h...")
    coche.acelerar(80)

    print("\nIntentando acelerar otros 50 km/h...\n")
    coche.acelerar(50)  

except ExcesoVelocidadException as e:
    print(f"X {e}")
