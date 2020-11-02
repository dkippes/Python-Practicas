
#Abrir archivo
a_file = open('home/aolmedo/coursera/python', 'r')

#Leer todo el contenido del archivo
a_file.read()

#Cerrar el archivo
a_file.close()

#Abrir un archivo como un context manager utilizando la sentencia with

with open('home/aolmedo/coursera/python', 'r') as a_file:
        a_file.read()