class Persona:
    def __init__(
            self,
            nombre: str,
            apellido: str,
            ):
        self.nombre = nombre
        self.apellido = apellido

    def to_arr(self):
        return [self.nombre, self.apellido]
