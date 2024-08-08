class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    


class Auto:
    def __init__(self, color:str, cant_puertas:int, velocidad:int, cant_ruedas:int):
        self.color = color
        self.cant_puertas = cant_puertas
        self.velocidad = velocidad
        self.cant_ruedas = cant_ruedas
        self.a_bordo = []

    def __str__(self):
        return f'Este es un auto de color {self.color}, con {self.cant_puertas} puertas, va a {self.velocidad} km/h'

    def mostrar_color(self):
        print(f'Mi color es {self.color}')

    def avanzar(self):
        print(f'El auto avanza a {self.velocidad} km/h')

    def turbo(self):
        return self.velocidad**2
    
    def abordar(self, persona:Persona):
        self.a_bordo.append(persona)
