# Punteros de objetos

# Definimos las clases
class Auto:
    def __init__(self, color:str, patente:str, velocidad:int):
        self.color = color
        self.patente = patente
        self.velocidad = velocidad

    def arrancar_auto(self):
        print(f'El auto va a {self.velocidad} kilómetros por hora')


class Persona:
    def __init__(self, nombre:str, dni:int):
        self.nombre = nombre
        self.dni = dni
        self.autos = []

    def agregar_autos(self, auto:list):
        for auto in autos:
            self.autos.append(auto)

# Instanciamiento
ferrari = Auto('Rojo', 'ABC123', 270)
ram = Auto('Gris', 'DEF456', 180)
fitito = Auto('Azul', 'HIJ789', 20)

raul = Persona('Raúl', 123)

# Añadir autos
autos = [ferrari, ram, fitito]
raul.agregar_autos(autos)

print(raul)
print(raul.autos)
print(raul.autos[2].arrancar_auto())


