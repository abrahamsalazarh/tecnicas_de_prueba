from mi_paquete.mis_funciones import func_cuadratica, func_sumatoria

def test_func_cuadratica():
    valor_esperado = 9
    assert func_cuadratica(3) == valor_esperado

def test_func_sumatoria():
    valor_esperado = 6
    assert func_sumatoria([1,2,3]) == valor_esperado