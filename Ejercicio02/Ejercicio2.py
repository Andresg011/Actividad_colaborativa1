
class Coche:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

# Getters

    def getmarca(self):
        return self.__marca

    def getmodelo(self):
        return self.__modelo

    def getaño(self):
        return self.__año

# Setters

    def setmarca(self, marca):
        self.__marca = marca

    def setmodelo(self, modelo):
        self.__modelo = modelo

    def setaño(self, año):
        if año > 0: 
            self.__año = año
        else:
            print("Año no válido")
    
    def describir(self):
        print(f"Coche: {self.__marca} {self.__modelo} Año: {self.__año}")

# Objetos para prueba de acceso y modificación de atributos
# Vamos a suponer que nos equivocamos en la marca del Jetta (traemos las objetos creados del ejercicio anterior)
Coche2 = Coche("Toyota", "Jetta", 2022)

# acceder con getter
print(Coche2.getmarca())
print(Coche2.getmodelo())
print(Coche2.getaño())

Coche2.setmarca("Volkswagen")
Coche2.setmodelo("Jetta GLI")
Coche2.setaño(2026)

Coche2.describir()
