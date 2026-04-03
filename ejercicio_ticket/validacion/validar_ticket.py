import re

def validar_ticket(codigo: str) -> bool:
    if not isinstance(codigo, str):
        raise TypeError(
            f"Se esperaba un string, se recibió: {type(codigo).__name__}"
        )
    patron = r'^[A-Z]{4}[0-9]{4}$'
    if not re.fullmatch(patron, codigo):
        raise ValueError(
            f"Formato de ticket inválido: '{codigo}'. "
            f"Se esperan 4 letras mayúsculas seguidas de 4 dígitos."
        )
    return True
