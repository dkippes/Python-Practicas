import datetime

# date objects
# El dia 30 de Abril de 2019
date = datetime.date(2019, 4, 30)

# Atributo año de la fecha
date.year
# Atributo mes de la fecha
date.month
# Atributo dia de la fecha
date.day

# Devuelve el dia de la semana. El lunes es 0 y domingo 6
date.weekday()
# Devuelve el dia de la semana. Lunes 1, domingo 7
date.isoweekday()
# Devuelve una tupla con 3 elementos: año, numero de semana, dia de la semana
date.isocalendar()
# Devuelve la fecha como un string 'YYYY-MM-DD'
date.isoformat()

# Fecha minima
date_min = datetime.date.min
# Fecha maxima
date_max = datetime.date.max

# El dia de hoy
today = datetime.date.today()

# El dia de ayer
yesterday = today - datetime.timedelta(day=1)

# resta de dos fechas
delta = today - yesterday


# datetime objets
# El dia 10 de Octubre de 2019 a las 9:15:30
date_and_time = datetime.datetime(2019, 10, 10, 9, 15, 30)

# Atributo año de la fecha y hora
date_and_time.year
# Atributo mes de la fecha y hora
date_and_time.month
# Atributo dia de la fecha y hora
date_and_time.day
# Atributo hora de la fecha y hora
date_and_time.hour
# Atributo minutos de la fecha y hora
date_and_time.minute
# Atributo segundos de la fecha y hora
date_and_time.second
# Atributo microsegundo de la fecha y hora
date_and_time.microsecond

# obtengo un objeto date a partir del objeto datetime
date_and_time.date()

# La fecha y hora actual (loca)
now = datetime.datetime.now()

# La fecha y hora actual en UTC (Coordinated Universal Time)
now = datetime.datetime.utcnow()


# time objects
# La hora 10:20:35
time = datetime.time(10, 20, 35)
# Atributo hora de la hora
time.hour
# Atributo minutos de la hora
time.minute
# Atributo segundos de la hora
time.second
# Atributo microsegundos de la hora
time.microsecond

# Hora minima
time_min = datetime.time.min
# Hora maxima
time_max = datetime.time.max