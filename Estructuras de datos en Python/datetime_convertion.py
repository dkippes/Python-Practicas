import datetime

date_and_time = datetime.datetime(2019, 4, 30, 11, 25, 30)

#La funcion strftime crea un string a partir de un objeto datetime
date_and_time.strftime('%Y-%m-%d')
date_and_time.strftime('%Y-%m-%d %H:%M:%S')
date_and_time.strftime('%Y-%m-%d')
date_and_time.strftime('%Y-%m-%d T%H:%M:%S')

#La funcion strptime crea un objeto datetime a partir de un string
datetime.datetime.strptime('2019-01-10', '%Y-%m-%d')
datetime.datetime.strptime('2019-01-10 11:30:35', '%Y-%m-%d %H:%M:%S')
datetime.datetime.strptime('2019-01-10 T11:30:25', '%Y-%m-%d T%H:%M:%S')
