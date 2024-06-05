from base_de_datos import BD
from Modelos.usuario import Usuario
from utils.auth import Auth

import sqlite3

class ServiciosUsuario:
    def __init__(self):
        self.bd = BD()

    def crear_usuario(self, nombre:str, contraseña:str):
        # Busco al usuario en la bd
        usuario = self.bd.cur.execute("SELECT * FROM usuario WHERE nombre LIKE ?", (nombre,)).fetchone()

        # Si el usuario no existe lo creo
        if usuario is None:
            sql = "INSERT INTO usuario (nombre, password) VALUES (?, ?)"
            self.bd.cur.execute(sql, (nombre, Auth.hash_contraseña(contraseña)))
            self.bd.con.commit()
            return True
        
        return False
    
    def autentificar(self, nombre: str, contraseña: str):
        # Trae todos los datos de usuario donde el nombre coincida. Sino devuelve None
        self.bd.cur.execute("SELECT * FROM usuario WHERE nombre LIKE ? ", (nombre,))
        usuario = self.bd.cur.fetchone()

        # Si el usuario existe entonces compruebo la contraseña
        if usuario != None:
            if Auth.check_contraseña(bytes(contraseña, "utf-8"), usuario["password"]):
                return Usuario(usuario["id"], usuario["nombre"], usuario["password"])

        return None
    
    def modificar(self, id:int, nombre:str, contraseña:str):
        """Actualizar datos del usuario"""
        try:
            sql = """
                UPDATE usuario 
                SET nombre = ?, password = ? 
                WHERE id = ?;
            """
            self.bd.cur.execute(sql, (nombre, Auth.hash_contraseña(contraseña), id))
            self.bd.con.commit()
            return True
        except(sqlite3.Error):
            return False

    def eliminar(self, id):
        """Eliminar usuario"""
        try:
            sql = "DELETE FROM usuario WHERE id = ?"
            self.bd.cur.execute(sql, (id,))
            return True
        except(sqlite3.Error):
            return False
        
    def get(self, *args):
        """
            get() -> Devuelve todos los usuarios\n
            get(id) -> Devuelve el usuario del id
        """
        if args:
            try:
                usuario = self.bd.cur.execute("SELECT * FROM usuario WHERE id = ?", args[0]).fetchone()
                return Usuario(usuario["id"], usuario["nombre"], usuario["contraseña"])
            except(sqlite3.Error):
                return None
        else:
            self.bd.cur.execute("SELECT * FROM usuario")
            return self.bd.cur.fetchall()            