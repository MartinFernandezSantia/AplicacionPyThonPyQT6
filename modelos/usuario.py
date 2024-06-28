from modelos.base_model import BaseModel
from utils.auth import Auth

class Usuario(BaseModel):
    update_fields = "nombre = ?, password = ?"
    table_name = "usuario"
    get_fields = "nombre, password, id"

    def __init__(self, nombre: str, contraseña: str, id: int=None):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña

    def crear(self):
        """Agregar la instancia de Usuario a la tabla 'usuario' como una nueva fila"""

        # Busco al usuario en la bd
        sql_usuario = "SELECT * FROM usuario WHERE nombre LIKE ?"
        usuario = self.bd.cur.execute(sql_usuario, (self.nombre,)).fetchone()

        print(usuario)
        # Si el usuario no existe lo creo
        if usuario is None:
            sql = "INSERT INTO usuario (nombre, password) VALUES (?, ?)"
            self.bd.cur.execute(sql, (self.nombre, Auth.hash_contraseña(self.contraseña)))
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
        # Hash contraseña antes de actualizarla
        instance.contraseña = Auth.hash_contraseña(instance.contraseña)
        return super().modificar(instance)
    

if __name__ == "__main__":
    nuevo = Usuario.login("Cesar", "asd123")
    print(nuevo.id, nuevo.nombre, nuevo.contraseña)
