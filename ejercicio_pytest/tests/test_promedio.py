import pytest
from matematicas.operaciones import promedio

def test_promedio_lista_vacia():
    resultado_esperado = ValueError

    with pytest.raises(ValueError) as error:
        promedio([])
    assert isinstance(error.value, resultado_esperado)

def test_promedio_lista_simple():       
    resultado_esperado = 2.0
    assert promedio([1, 2, 3]) == resultado_esperado

def test_promedio_un_elemento():        
    resultado_esperado = 7.0
    assert promedio([7]) == resultado_esperado

def test_promedio_flotantes():          
    resultado_esperado = pytest.approx(2.0, rel=1e-2)
    assert promedio([1.5, 2.5]) == resultado_esperado

def test_promedio_mas_de_10():
    resultado_esperado = ValueError

    with pytest.raises(resultado_esperado) as error:
        promedio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    assert isinstance(error.value, resultado_esperado)

def test_promedio_elemento_no_numerico():
    resultado_esperado = TypeError

    with pytest.raises(resultado_esperado) as error:
        promedio([1, "a", 3])
    assert isinstance(error.value, resultado_esperado)

def test_promedio_no_es_lista():
    resultado_esperado = TypeError

    with pytest.raises(resultado_esperado) as error:
        promedio("hola")
    assert isinstance(error.value, resultado_esperado)