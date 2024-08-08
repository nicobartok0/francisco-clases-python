import random

# Lugar para importar las librerías

import math

# Definición de variables
wifi = True
registered = True
admin = True


# Función sin guard clauses

#def iniciar_sesion(wifi, registered, admin):
#    if wifi:
#        if registered:
#            if admin:
#                print('Hola, admin!')
#            print('Hola, usuario!')
#        print('Bienvenido a la página!')
#    else:
#        print('No tienes wifi!')

#iniciar_sesion(wifi, registered, admin)

# Función con guard clauses

def iniciar_sesion():
    if not wifi:
        return 'No tienes wi-fi'
    if not registered:
        return 'No estás registrado'
    if not admin:
        return 'No eres admin'
    
    return 'Hola admin!'



print(iniciar_sesion())



# Palabra clave pass / comparación de número
num = 5

if num == 5:
    pass
else:
    print('El número no es 5')

if num != 5:
    print('El número no es 5')
    

# random

print(random.randint(10, 20))


