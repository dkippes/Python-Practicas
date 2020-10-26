import string

name = 'Diego'
formatter = string.Formatter()
formatter.format('Hola {}', name)

'Hola {}'.format(name)

# Ejemplos de la funcion format
'{} + {} = {}'.format(2, 5, 7)

'{1} + {2} = {0}'.format(7, 5, 2)

'Hola {name}'.format(name = name)

'{0} + {1} = {result}'.format(2, 5, result = 7)

'{0:f} + {1:f} = {result:f}'.format(2, 5, result = 7)
'{0:.3f} + {1:.3f} = {result:.3f}'.format(2, 5, result = 7)
'{:d}'.format(25)
'{:.0f}'.format(25.50)

uno = 'Hola {name:16}'.format(name = name)
dos = 'Hola {name:<16}'.format(name = name) #a la izquierda
tres = 'Hola {name:>16}'.format(name = name) #a la derecha
cuatro = 'Hola {name:^16}'.format(name = name) #centrado
cinco = 'Hola {name:*^16s}'.format(name = name) #se completa con asterisco


nro_cuenta = '32673'

saldo = 100.2543

print('El saldo de la cuenta {} es ${:.2f}'.format(nro_cuenta, saldo))