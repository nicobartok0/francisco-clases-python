# Polimorfismo

class Animal:
    def __init__(self, nombre_animal:str, id_animal:int, sexo:str) -> None:
        self.nombre_animal = nombre_animal 
        self.id_animal = id_animal
        self.sexo = sexo

    def __del__(self):
        print('AHH ME ESTÁN MATANDO! RECUERDEN MI NOMBRE: ', self.nombre_animal)
        
    # Método que será sobreescrito
    def moverse(self, velocidad):
        return f'Caminé a {velocidad} km/h!'
    
class Serpiente(Animal):
    def __init__(self, nombre_animal: str, id_animal: int, sexo: str) -> None:
        super().__init__(nombre_animal, id_animal, sexo)
        
    # Método sobreescrito
    def moverse(self, velocidad):
        return f'Me deslicé a {velocidad} km/h!'
    
class Delfin(Animal):
    def __init__(self, nombre_animal: str, id_animal: int, sexo: str) -> None:
        super().__init__(nombre_animal, id_animal, sexo)

    def __conquistar_mundo(self):
        print('Voy a conquistar el mundo')

    # Método sobreescrito
    def moverse(self, velocidad):
        return f'Nadé a {velocidad} km/h!'
    
class Koala(Animal):
    def __init__(self, nombre_animal: str, id_animal: int, sexo: str) -> None:
        super().__init__(nombre_animal, id_animal, sexo)

    # Método sobreescrito
    def moverse(self, velocidad):
        return super().moverse(velocidad)
    
# Definir nuestros objetos
serpy = Serpiente('Serpy', 1, 'M')
juan = Delfin('Juan', 2, 'M')
rosa = Koala('Rosa', 3, 'H')

# Función polimórfica: Una sola función trabaja con tres objetos distintos y devuelve outputs distintos.
def movimiento(animal:Animal, velocidad):
    print(animal.moverse(velocidad))


velocidad = int(input('Decime a qué velocidad va Serpy '))
movimiento(serpy, velocidad)
velocidad = int(input('Decime a qué velocidad va Rosa '))
movimiento(rosa, velocidad)
velocidad = int(input('Decime a qué velocidad va Juan '))
movimiento(juan, velocidad)
