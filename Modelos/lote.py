from base_de_datos import BD
import sqlite3

class Lote:
    bd = BD()

    def __init__(self, id: int, circunscripcion:int, seccion:str, manzana:int, parcela:str):
        self.id = id
        self.circun = circunscripcion
        self.seccion = seccion
        self.manzana = manzana
        self.parcela = parcela

    def crear(self):
        """Guardar datos de la instancia en la BD"""

        # Busco al lote en la bd
        sql_lote = """
                    SELECT * FROM lote 
                    WHERE circunscripcion = ? 
                    AND seccion LIKE ?
                    AND manzana = ?
                    AND parcela LIKE ?
                    """
        lote = self.bd.cur.execute(sql_lote, (self.nombre,)).fetchone()

        # Si el lote no existe lo creo
        if lote is None:
            sql = "INSERT INTO lote (circunscripcion, seccion, manzana, parecela) VALUES (?, ?, ?, ?)"
            self.bd.cur.execute(sql, (self.circun, self.seccion, self.manzana, self.parcela))
            self.bd.con.commit()
            return True
        
        return False
    
    @classmethod
    def modificar(cls, lote:'Lote'):
        """Modifica todos los atributos de un usuario en la tabla"""

        if isinstance(lote, Lote):
            try:
                sql = """
                    UPDATE lote 
                    SET circunscripcion = ?, seccion = ?, manzana = ?, parecela = ? 
                    WHERE id = ?;
                """
                cls.bd.cur.execute(sql, (lote.circun, lote.seccion, lote.manzana, lote.parcela, lote.id))
                cls.bd.con.commit()
                return True
            except(sqlite3.Error):
                return False
        else:
            raise ValueError("El argumento 'lote' debe ser una instancia de tipo Lote")

    @classmethod
    def eliminar(cls, id):
        """Eliminar una fila de la tabla lote"""

        try:
            sql = "DELETE FROM lote WHERE id = ?"
            cls.bd.cur.execute(sql, (id,))
            return True
        except(sqlite3.Error):
            return False
        
    @classmethod
    def get(cls, id=None):
        """
            get() -> Devuelve todos los lotes\n
            get(id) -> Devuelve el lote del id
        """

        if id != None:
            try:
                lote = cls.bd.cur.execute("SELECT * FROM lote WHERE id = ?", id).fetchone()
                return Lote(lote["id"], lote["nombre"], lote["password"])
            except(sqlite3.Error):
                return None
        else:
            cls.bd.cur.execute("SELECT * FROM lote")
            return cls.bd.cur.fetchall()