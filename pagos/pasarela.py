"""Pasarela de pago externa (servicio de terceros).

Esta clase representa la comunicación con la pasarela real.
En las pruebas NUNCA se usa esta clase de verdad: se sustituye
por un Mock de unittest.mock para no depender del servicio externo.
"""


class PasarelaPago:
    def cobrar(self, monto, tarjeta):
        # En un sistema real aquí iría la llamada a la API de la pasarela.
        # Se deja una respuesta simulada simple.
        return {"estado": "aprobado", "id_pasarela": "SIM-000"}
