
class Cliente:
    def __init__(self, id:int, nombre:str, apellido:str, cuit:int, telefono:str=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        self.telefono = telefono