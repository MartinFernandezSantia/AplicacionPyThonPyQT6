import bcrypt

class Auth:

    def hash_contraseña(contraseña: str):
        # Pasar contraseña a bytes
        contraseña = bytes(contraseña, "utf-8")

        # Generar salt para la contraseña
        salt = bcrypt.gensalt()
        # Hashear contraseña
        hashed = bcrypt.hashpw(contraseña, salt)

        return hashed
    
    def check_contraseña(contraseña: str, hashed:bytes):
        contraseña = bytes(contraseña)
        return bcrypt.checkpw(contraseña, hashed)

if __name__ == "__main__":
    pass

    
    

