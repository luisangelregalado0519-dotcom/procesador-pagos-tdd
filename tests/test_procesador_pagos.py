"""Pruebas del ProcesadorPagos escritas ANTES del código (Fase Roja).

Se usa unittest.mock para aislar las dependencias externas:
- La pasarela de pago se sustituye por un Mock.
- La base de datos se sustituye por un Stub (RepositorioEnMemoria).
"""

import unittest
from unittest.mock import Mock

from pagos.procesador import ProcesadorPagos
from pagos.repositorio import RepositorioEnMemoria


class TestProcesadorPagos(unittest.TestCase):

    def setUp(self):
        self.pasarela = Mock()               # Mock de la pasarela externa
        self.repo = RepositorioEnMemoria()   # Stub de la base de datos
        self.procesador = ProcesadorPagos(self.pasarela, self.repo)

    def test_pago_aprobado_se_registra(self):
        self.pasarela.cobrar.return_value = {"estado": "aprobado", "id_pasarela": "P-001"}
        recibo = self.procesador.pagar(monto=500, tarjeta="4111")
        self.assertEqual(recibo.estado, "aprobado")
        self.assertEqual(len(self.repo.transacciones), 1)
        self.pasarela.cobrar.assert_called_once_with(500, "4111")

    def test_pago_rechazado_no_se_registra(self):
        self.pasarela.cobrar.return_value = {"estado": "rechazado", "motivo": "fondos insuficientes"}
        recibo = self.procesador.pagar(monto=500, tarjeta="4111")
        self.assertEqual(recibo.estado, "rechazado")
        self.assertEqual(len(self.repo.transacciones), 0)

    def test_monto_cero_lanza_error(self):
        with self.assertRaises(ValueError):
            self.procesador.pagar(monto=0, tarjeta="4111")
        self.pasarela.cobrar.assert_not_called()

    def test_monto_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            self.procesador.pagar(monto=-100, tarjeta="4111")
        self.pasarela.cobrar.assert_not_called()



if __name__ == "__main__":
    unittest.main()
