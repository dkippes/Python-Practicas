

frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', ' banana', 'kiwi'}

'pera' in frutas
'yerba' in frutas

# Conjunto vacio
set()

# Otra formas de crear conjuntos
a = set('abracadabra')
b = set('alacazam')

# Operaciones de conjuntoss
a - b # letras en a pero no en b
a | b # letras en a o en b o en ambas
a & b # letras en a y en b
a ^ b # letras en a o b pero no en ambos

# Comprension de conjuntos
a = {x for in 'abracadabra' if x not in 'abc'}