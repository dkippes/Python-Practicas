nombre = 'Diego'

lista = list(nombre)

# El indexado funciona de igual manera
nombre[0]
lista[0]

# El slicing funciona de igual manera
nombre[:4]
lista[:4]

# La funcion len funciona de igual manera
len(nombre)
len(lista)

# El in funciona en ambas
'A' in nombre
'A' in lista


# El not in funciona en ambas
'z' not in nombre
'z' not in lista

# Los strings tambien se pueden nrecorrer con un for
for letra in nombre:
    print(letra)

# Los strings son imutables
lista[2] = '0'
nombre[2] = 'o' # TypeError

'Hola ' + nombre
nombre + '!!'
nombre[:2] + 'o' + nombre[3:]