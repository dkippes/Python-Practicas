#La funcion read lee todo el contenido del archivo
with open('home/aolmedo/coursera/python', 'r') as a_file:
    print(a_file.read())

#La funcion readline la linea actual del archivo
with open('home/aolmedo/coursera/python', 'r') as a_file:
    print(a_file.readline())

#La funcion readlines las lineas del archivo y las guarda en una lista
with open('home/aolmedo/coursera/python', 'r') as a_file:
    print(a_file.readlines())

#La funcion list genera una lista con las lineas del archivo
with open('home/aolmedo/coursera/python', 'r') as a_file:
    print(list(a_file()))

#El for recorre linea a linea
with open('home/aolmedo/coursera/python', 'r') as a_file:
    for line in a_file:
        print(line)