"""Procesador de pagos (Fase Verde: implementación mínima)."""


class Recibo:
    def __init__(self, estado, monto, motivo=None):
        self.estado = estado
        self.monto = monto
        self.motivo = motivo


class ProcesadorPagos:
    def __init__(self, pasarela, repositorio):
        self.pasarela = pasarela
        self.repositorio = repositorio

    def pagar(self, monto, tarjeta):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        respuesta = self.pasarela.cobrar(monto, tarjeta)
        if respuesta["estado"] == "aprobado":
            recibo = Recibo("aprobado", monto)
            self.repositorio.guardar({"monto": monto, "tarjeta": tarjeta, "estado": "aprobado"})
            return recibo
        else:
            return Recibo("rechazado", monto, respuesta.get("motivo"))
