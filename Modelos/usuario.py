from base_de_datos import BD
from utils.auth import Auth
import sqlite3

class Usuario:
    bd = BD()

    def __init__(self, nombre: str, contraseña: str, id: int=None):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña    

    def crear(self):
        """Agregar la instancia de Usuario a la tabla 'usuario' como una nueva fila"""

        # Busco al usuario en la bd
        sql_usuario = "SELECT * FROM usuario WHERE nombre LIKE ?"
        usuario = self.bd.cur.execute(sql_usuario, (self.nombre,)).fetchone()

        # Si el usuario no existe lo creo
        if usuario is None:
            sql = "INSERT INTO usuario (nombre, password) VALUES (?, ?)"
            self.bd.cur.execute(sql, (self.nombre, Auth.hash_contraseña(self.contraseña)))
            self.bd.con.commit()
            return True
        
        return False
    
    @classmethod
    def modificar(cls, usuario:'Usuario'):
        """Modifica todos los atributos de un usuario en la tabla\n
            Requiere que la instancia posea 'id'
        """

        if isinstance(usuario, Usuario):
            try:
                sql = """
                    UPDATE usuario 
                    SET nombre = ?, password = ? 
                    WHERE id = ?;
                """
                cls.bd.cur.execute(sql, (usuario.nombre, usuario.contraseña, usuario.id))
                cls.bd.con.commit()
                return True
            except(sqlite3.Error):
                return False
        else:
            raise ValueError("El argumento 'usuario' debe ser una instancia de tipo Usuario")

    @classmethod
    def eliminar(cls, id):
        """Eliminar una fila de la tabla usuario"""

        try:
            sql = "DELETE FROM usuario WHERE id = ?"
            cls.bd.cur.execute(sql, (id,))
            return True
        except(sqlite3.Error):
            return False
        
    @classmethod
    def get(cls, id=None):
        """
            get() -> Devuelve todos los usuarios\n
            get(id) -> Devuelve el usuario del id
        """

        if id != None:
            try:
                usuario = cls.bd.cur.execute("SELECT * FROM usuario WHERE id = ?", id).fetchone()
                return Usuario(usuario["id"], usuario["nombre"], usuario["password"])
            except(sqlite3.Error):
                return None
        else:
            cls.bd.cur.execute("SELECT * FROM usuario")
            return cls.bd.cur.fetchall()