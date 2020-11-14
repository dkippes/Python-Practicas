s1 = "Prueba"

# Devuelve el numero de ocurrencias de una subcadena de texto en toda la cadena o en un rango
s1.count('a') #cuenta cuantas veces aparece a
# Indica si la cadena de texto empieza con la subcadena pasada
s1.startswith('a')
# indica si la cadena texto termina con la subcadena pasada
s1.endswith('a')
# Busca la subcadena pasada
s1.find('ue')
# Similar a find solo que al no encontrar la subcadena levanta una excepcion de tipo ValueError
s1.index('a')
# Igual que find solo que no devuelve la primera ocurrencia sino la ultima
s1.rfind('ue')
# Similar a rfind solo que al no encontrar la subcadena levanta una excepcion de tipo ValueError
s1.rindex('a')
# Indica si todos los caracteres de la cadena de texto son decimales
s1.isdecimal()
# Indica si todos los caracteres de la cadena de texto son digitos
s1.isdigit()
# Indica si todos los caracteres de la cadena de texto son minuscula
s1.islower()
# Indica si todos los caracteres de la cadena de texto son mayuscula
s1.isupper()
# Indica si la cadena esta con las matusculas y minusculas al estilo de un titulo
s1.istitle()
# indica si la cadena son todos espacios
s1.isspace()
# Indica si la cadena esta compuesta por todos caracteres alfabeticos
s1.isalpha()
# Indica si la cadena esta compuesta por todos caracteres alfanumericos
s1.isalnum()