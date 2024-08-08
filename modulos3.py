# importar módulos, como por ejemplo una función

import funciones3
run = True

def main():
    value = int(input('Ingrese un número: '))
    if value == 5:
        return False
    else:
        return True

while run:
    run = main()