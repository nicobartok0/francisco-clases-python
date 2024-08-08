# Bucles FOR
variable = True
lista = [4, "papa", 3, 5, 2]


print(range(5,10,2)) # -- Función RANGE devuelve objeto range (start, stop, step)

for i in range(5, 10, 2): # -- Función for con un rango RANGE
    print(i)

print('\n\n')

for element in lista: # -- Bucle for iterando elementos de una lista
    print(element)

while variable: # -- While variable booleana 
    print('Hola infinito')    
    for i in range(5, 10, 2): # -- Función for con un rango RANGE
        print(i)
        if i == 9:
            variable = False

print('\n\n')


# Listas y matrices

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
] # Matriz identidad

print(matriz) # Imprime la matriz
print(matriz[0]) # Imprime la primer fila de la matriz
print(matriz[0][0]) # Imprime el primer valor de la primer fila de la matriz

