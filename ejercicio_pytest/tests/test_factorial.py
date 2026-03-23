import pytest
from matematicas.operaciones import factorial

def test_factorial_cero():
    resultado_esperado = 1

    assert factorial(0) == resultado_esperado

def test_factorial_uno():
    resultado_esperado = 1

    assert factorial(1) == resultado_esperado

def test_factorial_cinco():
    resultado_esperado = 120

    assert factorial(5) == resultado_esperado

def test_factorial_grande():
    resultado_esperado = 2432902008176640000

    assert factorial(20) == resultado_esperado

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-3)