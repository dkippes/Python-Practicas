# Series de Fibonacci:
# la suma de dos elementos define el siguiente
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b