import pytest


def validar_stock(stock_actual, cantidad_solicitada):
    if cantidad_solicitada <= 0 or cantidad_solicitada > stock_actual:
        return False
    return True


# Caso crítico: probar que no permite retirar más del stock actual
def test_validar_stock_insuficiente():
    assert validar_stock(10, 15) == False


def test_validar_stock_correcto():
    assert validar_stock(10, 5) == True