# Procesador de Pagos con TDD, Mocks y Stubs

Proyecto de la asignatura **TDD (IRS-023-01)** — UTECO.
Autor: Luis Angel Regalado (2022-0804).

Módulo orientado a objetos que procesa pagos usando una pasarela
de pago externa. Las dependencias externas se aíslan con dobles
de prueba de `unittest.mock`:

- **Mock**: la pasarela de pago (`PasarelaPago`) se sustituye por
  un Mock para no llamar al servicio real y poder verificar las
  llamadas que recibe.
- **Stub**: la base de datos se sustituye por `RepositorioEnMemoria`,
  una versión falsa y sencilla que guarda en una lista.

## Cómo correr las pruebas

```
pip install pytest
python -m pytest tests/ -v
```

## Ciclo TDD seguido

1. **Fase Roja**: se escribieron primero las pruebas; al correrlas
   fallaban porque el módulo no existía.
2. **Fase Verde**: se escribió el código mínimo para pasarlas (4 pruebas).
3. **Refactor**: se ordenó el código (dataclass, métodos cortos)
   sin cambiar el comportamiento; las 4 pruebas siguieron pasando.
4. **Regresión**: se agregó un requisito nuevo (monto mínimo de
   RD$50) con su prueba, y se corrió la batería completa:
   las 5 pruebas pasan, sin efectos secundarios.
