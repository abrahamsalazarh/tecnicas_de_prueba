import pytest
from matematicas.operaciones import promedio

def test_promedio_lista_simple():
    resultado_esperado = 2.0

    assert promedio([1,2,3]) == resultado_esperado

def test_promedio_un_elemento():
    resultado_esperado = 7.0

    assert promedio([7]) == resultado_esperado

def test_promedio_flotantes():
    resultado_esperado = pytest.approx(2.0, rel=1e-2)

    assert promedio([1.5, 2.5]) == resultado_esperado

def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        promedio([])