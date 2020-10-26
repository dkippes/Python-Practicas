s1 = "Hola Mundo"       #una sola linea
s2 = 'Hola Mundo'       #con 3 comillas sirve para salto de linea
s3 = """Hola
 Mundo"""
s4 = '''Hola
 Mundo'''

s5 = "áéíóú"
s6 = s5.encode('utf-8') #unicode a enconde, lo codifica para que se lea, el typo sin encode es "str" al pasarlo es "byte"
s7 = s5.encode('ascii')

