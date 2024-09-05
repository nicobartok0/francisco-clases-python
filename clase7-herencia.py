# Definimos una clase

class Vehiculo:
    def __init__(self, nombre, velocidad, color) -> None:
        self.nombre = nombre
        self.velocidad = velocidad
        self.color = color
        self.movimiento = False

    def arrancar(self):
        print(f'El vehículo va a {self.velocidad} kilómetros por hora')
        self.movimiento = True

    def frenar(self):
        if self.movimiento == True:
            print('El vehículo ha sido frenado')
            self.movimiento = False
        else:
            print('El vehículo ha arrancado')
            self.movimiento = True

# Definimos sus hijos (herencia)

class Auto(Vehiculo):
    def __init__(self, nombre, velocidad, color):
        super().__init__(nombre, velocidad, color)
        self.cant_ruedas = 4

    def arrancar(self):
        super().arrancar()
        print('Wiiii')

class Moto(Vehiculo):
    def __init__(self, nombre, velocidad, color) -> None:
        super().__init__(nombre, velocidad, color)
        self.cant_ruedas = 2

    def arrancar(self):
        super().arrancar()
        print('WOOOOO')
    


auto1 = Auto('auto1', 20, 'rojo')
moto1 = Moto('moto1', 120, 'negra')
auto1.arrancar()
moto1.arrancar()

    