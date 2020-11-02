import math

class NegativeNumber(Exception):
    "Excepcion de tipo numero negativo"
    pass

def raiz_cuadrada(number):
    if number < 0:
        raise NegativeNumber("Numero negativo")
    return math.sqrt(number)