#los str dinamicos son caracteres con variables

name = "Diego"
"Hola %s" % name    #%s es string
"El numero es %d" % 5   #%d es entero
"El numero es %2d" % 5  #%2d dos digitos de entero
"El decimal es %f" % 6.5    #f es decimal
"El decimal es %2f" % 6.5   #2f dos decimales
"Hola %(name)s" % {'name': name}    #pasarle un parametro con el nombre

"Hola {}".format(name)  #reemplaza las llaves por el argumento name, es como %
"La suma de 1 + 2 es {0}".format(1+2)

' '.join(["hola", name])    #concatena los elementos de una lista con espacios
', '.join(["1", "2", "3", "4"]) #concatena los elementos de una lista con coma

a_string = 'Hola Mundo Python!'
print(a_string[-7:])