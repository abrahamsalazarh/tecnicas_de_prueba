import pytest
from validacion.validar_ticket import validar_ticket


def test_ticket_longitud_incorrecta():           
    resultado_esperado = ValueError
    with pytest.raises(resultado_esperado) as error:
        validar_ticket("AB12")
    assert isinstance(error.value, resultado_esperado)


def test_ticket_letras_minusculas():             
    resultado_esperado = ValueError
    with pytest.raises(resultado_esperado) as error:
        validar_ticket("abcd1234")
    assert isinstance(error.value, resultado_esperado)


def test_ticket_digitos_en_lugar_de_letras():   
    resultado_esperado = ValueError
    with pytest.raises(resultado_esperado) as error:
        validar_ticket("12341234")
    assert isinstance(error.value, resultado_esperado)


def test_ticket_letras_en_lugar_de_digitos():  
    resultado_esperado = ValueError
    with pytest.raises(resultado_esperado) as error:
        validar_ticket("ABCDabcd")
    assert isinstance(error.value, resultado_esperado)


def test_ticket_valido():                        
    resultado_esperado = True
    assert validar_ticket("ABCD1234") == resultado_esperado


def test_ticket_tipo_incorrecto():              
    resultado_esperado = TypeError
    with pytest.raises(resultado_esperado) as error:
        validar_ticket(12341234)
    assert isinstance(error.value, resultado_esperado)
