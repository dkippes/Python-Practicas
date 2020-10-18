import random

print(random.random())

print((random.random()*10)%6+1)

print(random.choice([1,2,3,4,5,6]))

print(random.choice(['rojo', 'verde', 'azul', 'negro', 'blanco']))

print(random.choices(['rojo', 'verde', 'azul', 'negro', 'blanco'], k=2))