class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir_motor(self):
        print(f"Motor de {self.potencia} HP, tipo {self.tipo}")

class Coche:
    def __init__(self, marca, modelo, año, motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = motor

    def describir(self):
        print(f"El coche es un {self.marca} {self.modelo} del año {self.año}")
        self.motor.describir_motor()

motor1 = Motor(250, "Gasolina")
motor2 = Motor(300, "Diésel")
motor3 = Motor(450, "Eléctrico")

coches = [
    Coche("Ford", "Mustang", 2022, motor1),
    Coche("Toyota", "Corolla", 2021, motor2),
    Coche("Tesla", "Model S", 2023, motor3)
]

print("---Demostracion de Composicion---\n")
print("Mostrando detalles de los coches y sus motores:\n")
for coche in coches:
    coche.describir()
    print()
    