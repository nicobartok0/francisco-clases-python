

class Usuario:
    def __init__(self, dni, nombre, contraseña, id_user) -> None:
        self.id = id_user
        self.dni = dni
        self.nombre = nombre
        self.__contraseña = contraseña
        self.__id_admitidos = [2, 3, 4, 5]

    # Getter de contraseña
    def get_contraseña(self, id):
        if id in self.__id_admitidos:
            return self.__contraseña
        else:
            return 'Contraseña falsa'

class Hacker:
    def __init__(self) -> None:
        self.id = 7

    def obtener_contraseña(self, contraseña):
        print('Has sido hackeado!')
        print(contraseña)

usuario1 = Usuario(1, 'Juancito', '123lalala', 2)

usuario2 = Hacker()

#usuario2.obtener_contraseña(usuario=usuario1)

print(usuario2.obtener_contraseña(usuario1.get_contraseña(usuario2.id)))