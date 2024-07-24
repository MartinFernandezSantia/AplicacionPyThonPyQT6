import os
import pathlib
import sys
import locale
import datetime

from modelos.transaccion import Transaccion
from modelos.cliente import Cliente
from modelos.lote import Lote
from bd.base_de_datos import BD

from fpdf import FPDF, XPos, YPos


def pdf_cuotas(transaccion: Transaccion):
    bd = BD()
    cur = bd.cur

    # Determine the base directory
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable sys._MEIPASS'.
        base_dir = pathlib.Path(sys._MEIPASS).resolve()
    else:
        base_dir = pathlib.Path(__file__).parent.parent.resolve()

    # Ruta del directorio actual
    DIR = base_dir

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
            row = table.row() # Header
            for mes in MESES:
                row.cell(mes, align="C")

            row2 = table.row() # N° de cuota
            row3 = table.row() # Valor cuota
            row4 = table.row() # Fecha de pago

            for mes in range(1, len(MESES) + 1):
                fecha = cuotas[n_cuota]["fecha"]
                n = cuotas[n_cuota]["cuota"]
                valor = cuotas[n_cuota]["valor"]
                fecha_pago = cuotas[n_cuota]["fecha_pago"]

                # Si la cuota actual tiene fecha de pago igual a la fecha sobre la que se esta iterando
                if fecha.month == mes and fecha.year == año_cuota:
                    row2.cell(text=f"CUOTA N° {n}", align="C")
                    row3.cell(text=f"${valor}", align="C")
                    row4.cell(text=f"{fecha_pago if fecha_pago != None else "Sin pagar"}", align="C")

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

    # Crear carpeta para PDF
    # if not os.path.exists(os.path.join(DIR, "PDFs")):
    #     os.makedirs(os.path.join(DIR, "PDFs"))

    output_folder = os.path.join("PDFs", "Cuotas")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar el PDF
    pdf.output(os.path.join(output_folder, f"{año_cuota}-{mes}-{nombre_completo}.pdf"))

def pdf_recibo(transaccion: Transaccion):
    bd = BD()
    cur = bd.cur

    # Esta linea permite que el nombre de los dias/meses/años retornados por datetime esten en español
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

    # Determine the base directory
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable sys._MEIPASS'.
        base_dir = pathlib.Path(sys._MEIPASS).resolve()
    else:
        base_dir = pathlib.Path(__file__).parent.parent.resolve()

    # Ruta del directorio actual
    DIR = base_dir

    lote = Lote.get(transaccion.id_lote)
    cliente = Cliente.get(transaccion.id_cliente)
    fecha_actual = datetime.date(2025, 9, 10)
    cuotas_atrasadas = []
    año = 0

    # Obtengo todas las cuotas atrasadas
    for cuota in transaccion.get_cuotas():

        if cuota["estado"] == 0 and cuota["fecha"] < fecha_actual:

            # Cada vez que cambia el año hago una separación
            if año != cuota["fecha"].year and cuotas_atrasadas != []:
                cuotas_atrasadas.append("|")

            cuotas_atrasadas.append(cuota)
            año = cuota["fecha"].year

    # Genero la parte del recibo correspondiente a los periodos a pagar
    periodos = "al periodo" if len(cuotas_atrasadas) == 1 else "a los periodos"
    for i in range(len(cuotas_atrasadas)):
        # Cada vez que halla una separación anual, redactar el año y seguir con el siguiente
        if cuotas_atrasadas[i] == "|" and i != 0:
            periodos += f" de {cuotas_atrasadas[i-1]["fecha"].year} y"
            continue

        mes = cuotas_atrasadas[i]["fecha"].month
        if i == len(cuotas_atrasadas) - 1: 
            periodos += f" {mes}"
            continue
        periodos += f" {mes},"
    else:
        periodos += f" de {cuotas_atrasadas[i]["fecha"].year}"
        

    dia_pago = datetime.datetime.now().day
    mes_pago = datetime.datetime.now().strftime("%B").capitalize()
    punitorio = sum(cuota["valor"] if cuota != "|" else 0 for cuota in cuotas_atrasadas) / 100 * transaccion.punitorio


    cuerpo = (
        f"En la ciudad de Mar del Plata recibí de {cliente.apellido} {cliente.nombre}, el día {dia_pago} de {mes_pago}, la suma de "
        f"${punitorio} en concepto del {transaccion.punitorio}% por punitorio, correspondiente {periodos} "
        f"por el lote identificado según la nomenclatura {cliente.nomenclatura}, Circunscripción: {lote.circun} Sección: {lote.seccion} "
        f"Manzana: {lote.manzana} Parcela: {lote.parcela}."
    )

    # Crear objeto FPDF y configurarlo
    pdf = FPDF(orientation="L", unit="pt", format="A4")

    # Añadir una página
    pdf.add_page()

    pdf.set_font("Times", "B", size=20)
    pdf.cell(text=f"{lote.nombre.upper()}  :  CUIT {cliente.cuit}", new_x="LMARGIN", new_y="NEXT", h=80)
    pdf.cell(text="Recibo de Pago", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(text=" ", new_x="LMARGIN", new_y="NEXT", h=30)

    pdf.set_font("Times", "", size=18)
    pdf.multi_cell(0, 30, cuerpo)


    output_folder = os.path.join("PDFs", "Recibos")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar el PDF
    pdf.output(os.path.join(output_folder, f"{lote.nombre}.pdf"))

if __name__ == "__main__":
    # tran = Transaccion(1, 256000, 81, 3000, 300, datetime.datetime.now(), datetime.datetime.now(), 1)
    # pdf_cuotas(tran)

    tran = Transaccion.get(1)
    tran.modificar_estado_cuota(1, False)
    pdf_recibo(tran)