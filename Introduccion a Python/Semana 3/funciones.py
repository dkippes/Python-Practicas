def cero():
    return 0

c = cero()
print(c)
print(cero())

def suma_uno(un_numero):
    "Suma uno al numero recibido como parametro" #docstring -> es una buena practica
    return un_numero + 1

print(suma_uno(cero()))

def suma(a,b):
    resultado = a + b
    return resultado

print(suma(10,5))