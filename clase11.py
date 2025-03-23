import webbrowser

# Definimos las clases para hacer el try / except


class Celular:
    def __init__(self, numero):
        self.numero = numero

    def llamar(self, nombre):
        print(f'El teléfono {self.numero} está llamando a {nombre}')

    

class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.celular = None

    def dar_celular(self, celular:Celular):
        self.celular = celular
    
    def llamar_contacto(self, contacto):
        try:
            self.celular.llamar(contacto.nombre)
        except:
            print('Error: No se pudo llamar contacto.')


motorola = Celular('2613336666')
juan = Persona('Juan')
pedro = Persona('Pedro')
juan.llamar_contacto(pedro)
print('Dándole un celular a Juan...')
juan.dar_celular(motorola)
juan.llamar_contacto(pedro)

webbrowser.open('Google.com')