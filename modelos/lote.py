# Este archivo va en modelos, y si es agregado, una FK para lote debe ser agregada a transacciones
#  y el archivo transacciones.py debe ser modificado

from modelos.base_model import BaseModel

class Lote(BaseModel):
    table_name = "lote"
    update_fields = "nombre = ?, circunscripcion = ?, seccion = ?, manzana = ?, parcela = ?"
    get_fields = "nombre, circunscripcion, seccion, manzana, parcela, id"
    order = "LOWER(nombre)"

    def __init__(self, nombre:str, circunscripcion:int, seccion:str, manzana:int, parcela:str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.circun = circunscripcion
        self.seccion = seccion
        self.manzana = manzana
        self.parcela = parcela

    def crear(self):
        """Guardar datos de la instancia en la BD"""

        # Busco al lote en la bd
        sql_lote = """SELECT * FROM lote WHERE nombre LIKE ?"""
        lote = self.bd.cur.execute(sql_lote, (self.nombre,)).fetchone()

        # Si el lote no existe lo creo
        if lote is None:
            sql = "INSERT INTO lote (nombre, circunscripcion, seccion, manzana, parcela) VALUES (?, ?, ?, ?, ?)"
            self.bd.cur.execute(sql, (self.nombre, self.circun, self.seccion, self.manzana, self.parcela))
            self.id = self.bd.cur.lastrowid
            self.bd.con.commit()

            return True
        return False
    
    def update_values(self):
        return [self.nombre, self.circun, self.seccion, self.manzana, self.parcela]
    
if __name__ == "__main__":
    lote = Lote(4, "KK", 176, "23 y 24")
    lote.crear()