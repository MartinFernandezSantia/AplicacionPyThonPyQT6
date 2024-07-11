from modelos.base_model import BaseModel
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sqlite3

class Transaccion(BaseModel):
    table_name = "transaccion"
    update_fields = "id_cliente = ?, valor_final = ?, cuotas = ?, valor_cuota = ?, aumento = ?, fecha_boleto = ?, fecha_primera_cuota = ?"
    get_fields = "id_cliente, valor_final, cuotas, valor_cuota, aumento, fecha_boleto, fecha_primera_cuota, id"
    order = "fecha_boleto"

    def __init__(
            self, 
            id_cliente:int, 
            # id_lote:int,
            valor_final:float, 
            cuotas:int, 
            valor_cuota:float,
            aumento:float,
            fecha_boleto,
            fecha_primera_cuota,
            id: int = None
            ):
        """fecha_boleto y fecha_primera_cuota deben ser datetime.datetime.date()."""
        self.id = id
        self.id_cliente = id_cliente
        # self.id_lote = id_lote
        self.valor_final = valor_final
        self.valor_cuota = valor_cuota
        self.cuotas = cuotas
        self.aumento = aumento
        self.fecha_boleto = fecha_boleto
        self.fecha_primera_cuota = fecha_primera_cuota

    def crear(self):
        """Guardar datos de la instancia en la BD"""

        cliente = self.bd.cur.execute("SELECT * FROM cliente WHERE id = ?", (self.id_cliente,)).fetchone()
        # lote = self.bd.cur.execute("SELECT * FROM lote WHERE id = ?", (self.id_lote,)).fetchone()

        # Chequeo si el cliente y lote asignados a la transaccion existen
        if cliente is None: # or lote is None:
            raise ValueError("El cliente seleccionado no existen.")

        if self.id == None:
            sql = """INSERT INTO transaccion (
                        id_cliente, 
                        valor_final, 
                        cuotas, 
                        valor_cuota, 
                        aumento, 
                        fecha_boleto, 
                        fecha_primera_cuota
                        ) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
            self.bd.cur.execute(
                sql, 
                (self.id_cliente, self.valor_final, self.cuotas, self. valor_cuota, self.aumento, self.fecha_boleto, self.fecha_primera_cuota)
                )
            self.id = self.bd.cur.lastrowid
            self.bd.con.commit()

            self.agregar_cuotas()

            return True
        
        return False
    
    def update_values(self):
        return [self.id_cliente, self.valor_final, self.cuotas, self.valor_cuota, self.aumento, self.fecha_boleto, self.fecha_primera_cuota]
    
    def agregar_cuotas(self):
        transaccion = self.bd.cur.execute("SELECT * FROM transaccion WHERE id = ?", (self.id,)).fetchone()
        # Si la transaccion existe en la BD
        if transaccion is not None:
            valor_couta = self.valor_cuota
            primera_cuota = self.fecha_primera_cuota

            for i in range(1, self.cuotas + 1):
                fecha = primera_cuota + relativedelta(months=i-1) #Aqui esta el problema caballero
                sql = "INSERT INTO pago_cuotas (id_transaccion, cuota, estado, fecha, valor) VALUES (?, ?, ?, ?, ?)"

                self.bd.cur.execute(sql, (self.id, i, 0, fecha, valor_couta))
                self.bd.con.commit()

                # Por cada semestre que pasa aumento el valor de las cuotas
                if i%6 == 0:
                    valor_couta += self.aumento

    def get_cuotas(self):
        """Retorna lista de diccionarios con la informacion de cada fila de pago_cuotas"""

        if self.id != None:
            cuotas_sql = "SELECT * FROM pago_cuotas WHERE id_transaccion == ?"
            cuotas = self.bd.cur.execute(cuotas_sql, (self.id,)).fetchall()

            return cuotas
        
        return None
    
    def modificar_estado_cuota(self, id_cuota:int, estado:bool):
        """Actualiza el estado de la cuota con id=id_cuota y si el estado=True\n
        entonces se actualiza la fecha de pago al día de hoy.
        """
        fecha = None
        if estado is True:
            fecha = datetime.date(datetime.now())

        try:
            sql = f"""
                    UPDATE pago_cuotas 
                    SET estado = ?, fecha_pago = ?
                    WHERE id = ?;
                """
            self.bd.cur.execute(sql, (estado, fecha, id_cuota))
            self.bd.con.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    @classmethod
    def modificar(cls, instance):
        modificar = super().modificar(instance)

        # Luego de modificar una transaccion, las cuotas relacionadas en pago_cuotas se borran y 
        # se crean nuevas con los datos modificados
        if modificar == True:
            delete_sql = "DELETE FROM pago_cuotas WHERE id_transaccion = ?"
            cls.bd.cur.execute(delete_sql, (instance.id,))
            instance.agregar_cuotas()
        
        return modificar


if __name__ == "__main__":
    hoy = datetime.date(datetime.now())

    # Creamos transaccion
    tran = Transaccion(15, 256000, 12, 20000, 500, hoy, hoy, 1)
    # tran.crear()
    for i in range(2, 10):
        tran.modificar_estado_cuota(i, False)

    # # La modificamos
    # tran.aumento = 450
    # Transaccion.modificar(tran)

    # print(Transaccion.get(1).aumento)

    # # La eliminamos
    # tran.eliminar(tran.id)