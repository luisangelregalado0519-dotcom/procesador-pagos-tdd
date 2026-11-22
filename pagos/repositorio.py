"""Repositorio de transacciones (base de datos).

RepositorioEnMemoria es un STUB: una versión falsa y sencilla
de la base de datos que guarda en una lista. Sirve para aislar
las pruebas de la base de datos real.
"""


class RepositorioEnMemoria:
    def __init__(self):
        self.transacciones = []

    def guardar(self, transaccion):
        self.transacciones.append(transaccion)
