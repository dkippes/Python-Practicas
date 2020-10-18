def maximo_2(a,b):
    "Devuelve el maximo entre a y b"
    maximo = a
    if b > a:
        maximo = b
    return maximo

def maximo_3(a, b, c):
    "Devuelve el maximo entre a, b y c"
    return maximo_2(a, maximo_2(b,c))

print(maximo_2(2, 5))
print(maximo_3(6, 1, 5))

#Le puedo no pasar un parametro si ya esta en el argumento
def peso(masa, gravedad=9.8):
    "Formula del peso"
    return masa * gravedad

print("Peso en la tierra:", peso(10))
print("Peso en la luna:", peso(10, 1.63))


#Pasarle todos los parametros que quiera
def suma_numeros(*args):
    "Suma los numeros pasados por parametro"
    return sum(args)

print("6 + 7 + 8 =", suma_numeros(*[6,7,8])) #Empaquetado
print("6 + 7 + 8 =", suma_numeros(6,7,8))    #Desempaquetado, son lo mismo