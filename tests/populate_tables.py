from faker import Faker

from modelos.cliente import Cliente
from modelos.lote import Lote
from modelos.transaccion import Transaccion

import random
from datetime import datetime, timedelta

fake = Faker()

def populate_clientes():
    for i in range(20):
        nombre = fake.first_name()
        apellido = fake.last_name()
        telefono = fake.phone_number()
        cuit = random.randint(10000000000, 99999999999)

        cliente = Cliente(nombre, apellido, cuit, telefono, "Catastral")
        cliente.crear()

def populate_lotes():
    for i in range(10):
        nombre = fake.street_name()
        cicun = random.randint(1, 99)
        manzana = random.randint(1, 999)
        seccion = (fake.random_letter() + fake.random_letter()).upper()
        parcela = random.randint(1, 99)

        lote = Lote(nombre, cicun, seccion, manzana, parcela)
        lote.crear()

def populate_transaccion():
    lotes = Lote.get()
    clientes = Cliente.get()

    for i, lote in enumerate(lotes):
        valor_final = random.randint(99999, 9999999)
        cuotas = random.randint(1, 72)
        valor_cuota = round(valor_final / cuotas)
        aumento = random.randint(100, 9999)
        punitorio = random.randint(1, 10)
        fecha_boleto = datetime(2023, 7, 29) + timedelta(days=random.randint(0, 365))
        fecha_primera_cuota = fecha_boleto + timedelta(days=random.randint(0, 30))

        transaccion = Transaccion(
            clientes[i].id,
            lote.id,
            valor_final,
            cuotas,
            valor_cuota,
            aumento,
            punitorio,
            fecha_boleto.date(),
            fecha_primera_cuota.date()
            )

        transaccion.crear()

if __name__ == "__main__":
    populate_transaccion()