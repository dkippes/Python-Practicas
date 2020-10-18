for i in range(10):
    print(i)

print("******************************")
for i in 'Hola Mundo!':
    print(i)

print("******************************")
def contador(n):
    c = 0
    for i in range(n):
        c += 1
    return c

print(contador(10))

print("******************************")
def sumatoria(numeros):
    acum = 0
    for n in numeros:
        acum += n
    return print(acum)

sumatoria([1,2,3,4,5])

print("******************************")
def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar"
    for indice in [1,2,3,4,5,6,7,8,9,10]:
        print(f"{numero} * {indice} = {numero * indice}")
    
tabla_multiplicar(2)