def factorial(n: int) -> int: 

    if n < 0:
        raise ValueError(f"El factorial no está definido para negativos: {n}")
    
    resultado = 1

    for i in range (1, n + 1):
        resultado *= i

    return resultado

# --------------------------------------------------------------------------------------------------

def promedio(numeros: list) -> float:
    if not isinstance(numeros, list):
        raise TypeError(f"Se esperaba una lista, se recibió: {type(numeros).__name__}")
    if len(numeros) == 0:
        raise ValueError("No se puede calcular el promedio de una lista vacía")
    if len(numeros) > 10:
        raise ValueError(f"La lista no puede tener más de 10 elementos, tiene: {len(numeros)}")
    for i, elemento in enumerate(numeros):
        if not isinstance(elemento, (int, float)) or isinstance(elemento, bool):
            raise TypeError(f"Elemento en posición {i} no es numérico: {repr(elemento)}")
    return sum(numeros) / len(numeros)