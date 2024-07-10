import sqlite3
from bd.base_de_datos import BD

class BaseModel:
    bd = BD()

    def crear(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def update_values(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    @classmethod
    def modificar(cls, instance):
        """Modifica todos los atributos de una fila en la tabla para que igualen a los de la instancia.\n
            Requiere que la instancia posea 'id'.
        """
        if isinstance(instance, cls):
            try:
                sql = f"""
                    UPDATE {cls.table_name} 
                    SET {cls.update_fields}
                    WHERE id = ?;
                """
                cls.bd.cur.execute(sql, instance.update_values() + [instance.id])
                cls.bd.con.commit()
                return True
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return False
        else:
            raise ValueError(f"El argumento debe ser una instancia de tipo {cls.__name__}")

    @classmethod
    def eliminar(cls, id):
        """Eliminar una fila de la tabla usuario con id=id."""
        try:
            sql = f"DELETE FROM {cls.table_name} WHERE id = ?"
            cls.bd.cur.execute(sql, (id,))
            cls.bd.con.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    @classmethod
    def get(cls, id=None):
        """
            get() -> Retorna una lista de instancias de todas las filas.\n
            get(id) -> Retorna una instancias de la fila con id = id.
        """
        if id is not None:
            try:
                row = cls.bd.cur.execute(f"SELECT {cls.get_fields} FROM {cls.table_name} WHERE id = ?", (id,)).fetchone()
                if row:
                    return cls(**row)
                return None
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return None
        else:
            cls.bd.cur.execute(f"SELECT * FROM {cls.table_name} ORDER BY {cls.order}")
            rows = cls.bd.cur.fetchall()
            return [cls(**row) for row in rows]
