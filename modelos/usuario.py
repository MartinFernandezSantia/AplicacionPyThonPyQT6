from modelos.base_model import BaseModel
from utils.auth import Auth

class Usuario(BaseModel):
    update_fields = "nombre = ?, password = ?"
    table_name = "usuario"
    get_fields = "nombre, password, id"

    def __init__(self, nombre: str, password: str, id: int=None):
        self.id = id
        self.nombre = nombre

        if isinstance(password, str):
            self.contraseña = Auth.hash_contraseña(password)
        else:
            self.contraseña = password

    def crear(self):
        """Agregar la instancia de Usuario a la tabla 'usuario' como una nueva fila"""

        # Busco al usuario en la bd
        sql_usuario = "SELECT * FROM usuario WHERE nombre LIKE ?"
        usuario = self.bd.cur.execute(sql_usuario, (self.nombre,)).fetchone()

        # Si el usuario no existe lo creo
        if usuario is None:
            sql = "INSERT INTO usuario (nombre, password) VALUES (?, ?)"
            self.bd.cur.execute(sql, (self.nombre, self.contraseña))
            self.id = self.bd.cur.lastrowid
            self.bd.con.commit()
            
            return True
        
        return False
    
    def update_values(self):
        return [self.nombre, self.contraseña]
    
    @classmethod
    def login(cls, nombre:str, contraseña:str):
        """Retorna una instancia de Usuario si la autentificacion en correcta"""
        sql = "SELECT * FROM usuario WHERE nombre LIKE ?"
        usuario = cls.bd.cur.execute(sql, (nombre,)).fetchone()

    
        if usuario != None and Auth.check_contraseña(contraseña, usuario["password"]):
            return Usuario(usuario["nombre"], usuario["password"], usuario["id"])
        
        return False
    
    @classmethod
    def modificar(cls, instance):
        # Hash contraseña antes de actualizarla si se a cambiado
        if isinstance(instance.contraseña, str):
            instance.contraseña = Auth.hash_contraseña(instance.contraseña)
        return super().modificar(instance)
    

if __name__ == "__main__":
    usuario = Usuario("Martin", "asdASD123")
    usuario.crear()