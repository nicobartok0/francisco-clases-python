# -- Acá se importan los módulos --



# -- Acá va el código --


# Formateo de string

numero = 4
saludo = f'Mi número es {numero}' 
print(saludo)

saludo2 = "Mi número es " + str(numero)
print(saludo2)

# Ingreso de datos
dato = int(input("Ingrese un dato "))
print(type(dato))


# Comparaciones
# ==
# !=
# >
# <
# >=
# <=

# Símbolos matemáticos
# +
# -
# *
# /
# %

# Condicionales básicos

if dato == 4:
    print('Tu número es igual a 4!! :D')
elif dato == 6:
    print('Tu número es igual a 6!! :D')
else:
    print('Tu número no es igual ni a 4 ni a 6 :(')
    
