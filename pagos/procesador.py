"""Procesador de pagos (después del Refactor).

Diseño orientado a objetos:
- El procesador depende de interfaces (la pasarela y el repositorio
  le llegan por el constructor: inyección de dependencias).
- Cada método hace una sola cosa (responsabilidad única).
- Recibo es un dataclass: código corto y claro.
"""

from dataclasses import dataclass


@dataclass
class Recibo:
    estado: str
    monto: float
    motivo: str = None


class ProcesadorPagos:
    def __init__(self, pasarela, repositorio):
        self._pasarela = pasarela
        self._repositorio = repositorio

    MONTO_MINIMO = 50

    def pagar(self, monto, tarjeta):
        self._validar_monto(monto)
        if monto < self.MONTO_MINIMO:
            return Recibo("rechazado", monto, "monto menor al mínimo")
        respuesta = self._pasarela.cobrar(monto, tarjeta)
        if respuesta["estado"] == "aprobado":
            return self._registrar_pago(monto, tarjeta)
        return Recibo("rechazado", monto, respuesta.get("motivo"))

    def _validar_monto(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")

    def _registrar_pago(self, monto, tarjeta):
        self._repositorio.guardar(
            {"monto": monto, "tarjeta": tarjeta, "estado": "aprobado"}
        )
        return Recibo("aprobado", monto)
