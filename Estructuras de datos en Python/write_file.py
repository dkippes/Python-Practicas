#Escribir un string en el archivo
with open('home/aolmedo/coursera/python', 'w') as a_file:
    a_file.write('Hola Mundo')

#Ecribir muchas lineas en el archivo
with open('home/aolmedo/coursera/python', 'w') as a_file:
    a_file.writelines(['Linea 1.\n', 'Linea 2.\n', 'Linea 3.\n'])

#Escribir un sstring en el archivo, agregandolo al final del mismo
with open('home/aolmedo/coursera/python', 'a') as a_file:
    a_file.write('Hola Mundo')