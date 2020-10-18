def suma_n(n):
    "Suma los numeros de 1 a n"
    result = 0
    x = n
    while x > 0:
        result += x
        x -=1
    return result

print(suma_n(5))

print("****************************")
def ciclo_infinito():
    "Imprime el numero 1 infinitas veces"
    i = 1
    while i <= 10:
        print(i, end =" ")

#ciclo_infinito()

def sumarNumerosPares(n):
    suma = 0
    for i in range(n + 1):
        if i % 2 == 0:
            suma += i
    return(suma)

print(sumarNumerosPares(4))

sm = 0
for i in range(10):
    sm += i

print(sm)
