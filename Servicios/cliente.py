from base_de_datos import BD
from Modelos.cliente import Cliente
import sqlite3

class ServiciosCliente:
    def __init__(self):
        self.bd = BD()

    def crear(self, nombre:str, apellido:str, cuit:int, telefono:str=None):
        # Busco al cliente en la bd
        sql_usuario = "SELECT * FROM clientes WHERE cuit = ?"
        usuario = self.bd.cur.execute(sql_usuario, (cuit,)).fetchone()

        # Si el cliente no existe lo creo
        if usuario is None:
            sql = "INSERT INTO clientes (nombre, apellido, telefono, cuit) VALUES (?, ?, ?, ?)"
            self.bd.cur.execute(sql, (nombre, apellido, telefono, cuit))
            self.bd.con.commit()
            return True
        
        return False
    
    def modificar(self, id:int, nombre:str, apellido:str, telefono:str, cuit:int):
        try:
            sql = """
                UPDATE cliente 
                SET nombre = ?, apellido = ?, telefono = ?, cuit = ? 
                WHERE id = ?;
            """
            self.bd.cur.execute(sql, (nombre, apellido, telefono, cuit, id))
            self.bd.con.commit()
            return True
        except(sqlite3.Error):
            return False

    def eliminar(self, id):
        try:
            sql = "DELETE FROM cliente WHERE id = ?"
            self.bd.cur.execute(sql, (id,))
            return True
        except(sqlite3.Error):
            return False
        
    def get(self, *args):
        """
            get() -> Devuelve todos los clientes\n
            get(id) -> Devuelve el cliente del id
        """
        if args:
            try:
                cliente = self.bd.cur.execute("SELECT * FROM cliente WHERE id = ?", args[0]).fetchone()
                return Cliente(
                    cliente["id"], 
                    cliente["nombre"], 
                    cliente["apellido"],
                    cliente["cuit"],
                    cliente["telefono"]
                    )
            except(sqlite3.Error):
                return None
        else:
            self.bd.cur.execute("SELECT * FROM cliente")
            return self.bd.cur.fetchall()