x=1
y=2

#Encadenando

if x < y:
    print(x, "es menor que", y)
elif x > y:
    print(x, "es mayor que", y)
else:
    print(x, "es igual a", y)

#Anidando -> dificultan la lectura del programa

if x == y:
    print(x, "es igual a", y)
else:
    if x < y:
        print(x, "es menor que", y)
    else:
        print(x, "es mayor que", y)
    