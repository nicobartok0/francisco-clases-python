# REPASO

# Creación de una clase
class Persona:
    def __init__(self, dni:int, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'La persona es {self.nombre} {self.apellido} '

    def caminar(self):
        print('Caminé 20km')

# Instanciamiento

persona1 = Persona(10,'José', 'Fernandez')
persona2 = Persona(25, 'Jorge', 'Pérez')
persona3 = Persona(30, 'Rudofelgio', 'Gómez')
persona4 = Persona(40, 'Diana', 'Perry')

personas = {
    10: persona1,
    25: persona2,
    30: persona3,
    40: persona4
}

# Acceder a una característica de un objeto dentro de un diccionario
print(personas[30].nombre)

# Iterar dentro de un diccionario

for key in personas.keys():
    print(f'La persona de DNI {key} es {personas[key].apellido}, {personas[key].nombre}')

#print('¿Qué persona quieres buscar?')
#dni_busqueda = int(input('Ingrese el DNI: '))
#print(personas[dni_busqueda])

# Añadido iterado de personas

print('¿Cuántas personas desea crear? ')
cant = int(input('')) 

personas = []

for i in range(cant):
    dni = int(input('Ingrese el DNI '))
    nombre = input('Ingrese el nombre ')
    apellido = input('Ingrese el apellido ')
    persona = Persona(dni, nombre, apellido)
    personas.append(persona)

for persona in personas:
    print(persona)