from faker import Faker
from modelos.cliente import Cliente
import random

fake = Faker()

def populate_clientes():
    for i in range(20):
        nombre = fake.first_name()
        apellido = fake.last_name()
        telefono = fake.phone_number()
        cuit = random.randint(10000000000, 99999999999)

        cliente = Cliente(nombre, apellido, cuit, telefono)
        cliente.crear()

if __name__ == "__main__":
    populate_clientes()