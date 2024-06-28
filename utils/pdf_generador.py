from fpdf import FPDF, XPos, YPos
import os
import pathlib
from modelos.transaccion import Transaccion
from modelos.cliente import Cliente
from bd.base_de_datos import BD
import datetime

def generar_pdf(transaccion: Transaccion):
    bd = BD()
    cur = bd.cur

    # Ruta del directorio actual
    DIR = pathlib.Path(__file__).parent.resolve()

    # Obtener información del cliente
    cliente = Cliente.get(transaccion.id_cliente)
    nombre_completo = cliente.apellido + " " + cliente.nombre
    año = transaccion.fecha_boleto.year

    # Crear objeto FPDF y configurarlo
    pdf = FPDF(orientation="L", unit="pt", format="A4")

    # Añadir una página
    pdf.add_page()

    # Datos de la transacción
    transaction_data = {
        "Cliente": nombre_completo,
        "Celular": cliente.telefono if cliente.telefono is not None else "",
        "Valor final": f"${transaccion.valor_final}",
        "Cuotas": str(transaccion.cuotas),
        "Aumento": f"${transaccion.aumento}",
        "Fecha de boleto": transaccion.fecha_boleto.strftime("%d/%m/%Y")
    }

    # Crear primera tabla con los datos de la transacción
    with pdf.table(width=300, align="LEFT", col_widths=(100, 200)) as table:
        for key, value in transaction_data.items():
            row = table.row()
            pdf.set_font("Times", "B", size=12)
            row.cell(str(key))
            pdf.set_font("Times", "", size=12)
            row.cell(str(value))

    # Obtener las cuotas de la transacción
    cuotas_sql = "SELECT cuota, estado, fecha, valor, fecha_pago FROM pago_cuotas WHERE id_transaccion = ?"
    cuotas = cur.execute(cuotas_sql, (transaccion.id,)).fetchall()
    MESES = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")
    año_cuota = cuotas[0]["fecha"].year
    n_cuota = 0

    # Procesar cada cuota
    while n_cuota < len(cuotas):
        # Aplicar año como título de tabla
        if año_cuota != cuotas[n_cuota]["fecha"].year:
            año_cuota = cuotas[n_cuota]["fecha"].year

        pdf.set_font("Times", "B", 16)
        pdf.cell(text=f"{año_cuota}", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT, h=50, w=0)

        with pdf.table() as table:
            # Font para las tablas
            pdf.set_font("Times", "", 9)

            # Crear filas de la tabla
            row = table.row()
            for mes in MESES:
                row.cell(mes, align="C")

            row2 = table.row()
            row3 = table.row()
            row4 = table.row()

            for mes in range(1, len(MESES) + 1):
                fecha = cuotas[n_cuota]["fecha"]
                n = cuotas[n_cuota]["cuota"]
                valor = cuotas[n_cuota]["valor"]
                fecha_pago = cuotas[n_cuota]["fecha_pago"]

                # Si la cuota actual tiene fecha de pago igual a la fecha sobre la que se esta iterando
                if fecha.month == mes and fecha.year == año_cuota:
                    row2.cell(text=f"CUOTA N° {n}", align="C")
                    row3.cell(text=f"${valor}", align="C")
                    row4.cell(text=f"{fecha_pago}", align="C")

                    n_cuota += 1

                    # Si ya no hay más cuotas pero la tabla todavia no esta llena o no hay más cuotas pagas
                    if n_cuota >= len(cuotas) or cuotas[n_cuota]["estado"] == 0:
                        for i in range(mes, len(MESES)):
                            row2.cell("", align="C")
                            row3.cell("", align="C")
                            row4.cell("", align="C")

                        n_cuota = len(cuotas)
                        break  # Salir del bucle si se han procesado todas las cuotas
                else:
                    row2.cell("", align="C")
                    row3.cell("", align="C")
                    row4.cell("", align="C")

    # Guardar el PDF
    pdf.output(os.path.join(DIR, "test.pdf"))

if __name__ == "__main__":
    tran = Transaccion(1, 256000, 81, 3000, 300, datetime.datetime.now(), datetime.datetime.now(), 1)
    generar_pdf(tran)
