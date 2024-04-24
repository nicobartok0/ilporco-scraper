import cryptocode

class Proveedor:
    def __init__(self, nombre, usuario, password) -> None:
        self.nombre = nombre
        self.username = usuario
        self.password = password

    def __str__(self) -> str:
        return(self.nombre)