import sqlite3

# Conexion a la base de datos
conn = sqlite3.connect(':memory:')

# Cursor
cursor = conn.cursor()

# Creo la tabla
conn.execute(
    """CREATE TABLE currency (ID integer primary key, name text, symbol text)""")


# Inserto datos de monedas
cursor.execute("INSERT INTO currency VALUES (1, 'Peso (ARG)', '$')")
cursor.execute("INSERT INTO currency VALUES (2, 'Dolar', 'U$S')")

# Guardo los cambios
conn.commit()

# Revierto los cambios
conn.rollback()

# Consulto todas las monedas
query = "SELECT * FROM currency"

# Busco el resultado
currency = cursor.execute(query).fetchone()

print(currency)
print(cursor.fetchone())
print(cursor.fetchone())

currencies = cursor.execute(query).fetchall()
print(currencies)

# Cierro la conexion a la base de datos
conn.close()
