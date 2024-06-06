from base_de_datos import BD
import sqlite3

class Cliente:
    bd = BD()

    def __init__(self, nombre:str, apellido:str, cuit:int, telefono:str=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        self.telefono = telefono

    def crear(self):
        """Agregar la instancia de Cliente a la tabla 'cliente' como una nueva fila"""

        # Busco al cliente en la bd
        sql_cliente = "SELECT * FROM clientes WHERE cuit = ?"
        cliente = self.bd.cur.execute(sql_cliente, (self.cuit,)).fetchone()

        # Si el cliente no existe lo creo
        if cliente is None:
            sql = "INSERT INTO cliente (nombre, apellido, telefono, cuit) VALUES (?, ?, ?, ?)"
            self.bd.cur.execute(sql, (self.nombre, self.apellido, self.telefono, self.cuit))
            self.bd.con.commit()
            return True
        
        return False
    
    @classmethod
    def modificar(cls, cliente:'Cliente'):
        """Modifica todos los atributos de un cliente en la tabla\n
            Requiere que la instancia posea 'id'
        """

        if isinstance(cliente, Cliente):
            try:
                sql = """
                    UPDATE cliente 
                    SET nombre = ?, apellido = ?, telefono = ?, cuit = ? 
                    WHERE id = ?;
                """
                cls.bd.cur.execute(
                    sql, 
                    (cliente.nombre, cliente.apellido, cliente.telefono, cliente.cuit, cliente.id)
                    )
                cls.bd.con.commit()
                return True
            except(sqlite3.Error):
                return False
        else:
            raise ValueError("El argumento 'cliente' debe ser una instancia de tipo Cliente")

    @classmethod
    def eliminar(cls, id):
        """Eliminar una fila de la tabla cliente"""

        try:
            sql = "DELETE FROM cliente WHERE id = ?"
            cls.bd.cur.execute(sql, (id,))
            return True
        except(sqlite3.Error):
            return False
        
    @classmethod
    def get(cls, id=None):
        """
            get() -> Devuelve todos los clientes\n
            get(id) -> Devuelve el cliente del id
        """

        if id != None:
            try:
                cliente = cls.bd.cur.execute("SELECT * FROM cliente WHERE id = ?", id).fetchone()
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
            cls.bd.cur.execute("SELECT * FROM cliente")
            return cls.bd.cur.fetchall()