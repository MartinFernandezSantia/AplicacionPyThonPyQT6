from modelos.base_model import BaseModel
import sqlite3

class Cliente(BaseModel):
    table_name = "cliente"
    update_fields = "nombre = ?, apellido = ?, cuit = ?, telefono = ?"
    get_fields = "nombre, apellido, cuit, telefono, id"

    def __init__(self, nombre:str, apellido:str, cuit:int, telefono:str=None, id:int=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        self.telefono = telefono

    def crear(self):
        """Agregar la instancia de Cliente a la tabla 'cliente' como una nueva fila"""

        # Busco al cliente en la bd
        sql_cliente = "SELECT * FROM cliente WHERE cuit = ?"
        cliente = self.bd.cur.execute(sql_cliente, (self.cuit,)).fetchone()

        # Si el cliente no existe lo creo y le agrego id a la instancia
        if cliente is None:
            sql = "INSERT INTO cliente (nombre, apellido, telefono, cuit) VALUES (?, ?, ?, ?)"
            self.bd.cur.execute(sql, (self.nombre, self.apellido, self.telefono, self.cuit))
            self.id = self.bd.cur.lastrowid
            self.bd.con.commit()
            
            return True
        
        return False
    
    def update_values(self):
        return [self.nombre, self.apellido, self.cuit, self.telefono]

if __name__ == "__main__":
    # cliente = Cliente("Mariela", "Romero", 30716963159, 2236805914, 1)
    # Cliente.modificar(cliente)
    # cliente.crear()
    pass