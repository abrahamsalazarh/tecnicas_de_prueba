def factorial(n: int) -> int: 

    if n < 0:
        raise ValueError(f"El factorial no está definido para negativos: {n}")
    
    resultado = 1

    for i in range (1, n + 1):
        resultado *= i

    return resultado

def promedio(numeros: list) -> float:

    if len(numeros) == 0:
        raise ValueError(f"No se puede calcular el promedio de una lista vacia")
    
    return sum(numeros) / len(numeros)