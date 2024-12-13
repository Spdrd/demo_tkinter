class Ciudad:
    def __init__(self, codigo=-1, nombre=""):
        self.codigo = codigo
        self.nombre = nombre
    
    def from_tuple(self, data):
        self.codigo = data[0]
        self.nombre = data[1]
    
    def to_tuple(self, data):
        return (self.codigo, self.nombre)