from modelos.transaccion import Transaccion
from modelos.cliente import Cliente

estado = 0
mes = 5
año = 2024

transacciones = Transaccion.get()

row_counter = 0

for transaccion in transacciones:
    cuotas = transaccion.get_cuotas()

    # Por cada cuota actualizo de una en una las filas de la tabla
    for cuota in cuotas:
        estado_cuota = cuota["estado"]
        fecha = cuota["fecha"]

        # Si la cuota coincide con los filtros
        if estado == estado_cuota and mes == fecha.month and int(año) == fecha.year:

            cliente = Cliente.get(transaccion.id_cliente)
            nombre_completo = f"{cliente.nombre} {cliente.apellido}"
            fecha_pago = cuota["fecha_pago"] if cuota["fecha_pago"] != None else "-"

            data = [nombre_completo, cuota["cuota"], cuota["valor"], fecha_pago]

            print(data)