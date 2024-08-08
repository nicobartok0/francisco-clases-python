# Definición de un diccionario
alumnos = {
    1: 'Pedro',
    2: 'Juan',
    3: 'Pepe'
}

# print(alumnos[1]) -- Buscar elementos específicos dentro de un diccionario

# Iterar en las claves de un diccionario
for key in alumnos.keys():
    print(alumnos[key])

# Iterar en los valores de un diccionario
for element in alumnos.values():
    print(element)

# Diccionario múltiple
multi_dict = {
    1: {
        1: 'Pedro',
        2: ['a', 'b', {
            1: 'Juan'
        }]
    },
    2: {
        1: 'José',
        2: ['c', 'd', {
            2: 'Tito'
        }]
    }
}

# print(multi_dict[2][2][2][2]) -- Acceder a un valor, dentro de un diccionario, 
# dentro de otro diccionario, dentro de otro, y otro más.

