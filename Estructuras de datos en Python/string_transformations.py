s1 = "Prueba"
s2 = "prueba"
s3 = "   prueba  "
s4 = "Hola Mundo"

# Capitaliza la cadena de texto
s2.capitalize()
# Convierte todos los caracteres a minuscula
s1.lower()
# Convierte todos los caracteres a mayuscula
s2.upper()
# Saca todos los espacios al final y comienzo de la cadena de caracteres
s3.strip()
# Separa la cadena de caracteres, en este caso por un espacio vacio
s4.split(" ")
# Intercambia las mayusculas por las minusculas y al reves
s1.swapcase()
# Le pone formato tiutlo a la cadena
s2.title()
# Quita los espacios en blanco de la derecha
s3.rsplit()
# Quita los espacios en blanco de la izquierda
s3.lstrip()
# Justifica la cadena a la derecha con una long de tantos caracteres como se indica en el parametro
s1.rjust(10)
# Justifica la cadena a la izquierda con una long de tantos caracteres como se indica en el parametro
s1.ljust(10)
# Reemplaza una cadena de texto por otra cadena de texto
s2.replace("r", "h")
# Centra la cadena de texto tomando como longitud la cantidad de caracteres indicada por el parametro
s1.center(10)
# Completa la cadena de texto con ceros al principio de la cadena segun la longitud pasada
s1.zfill(10)