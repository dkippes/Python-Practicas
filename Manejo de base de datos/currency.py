import sqlite3

DB_PATH = 'prueba.db'


class CurrencyDoesNotExists(Exception):
    pass


class CurrencyManager(object):

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def insert(self, obj):
        query = 'INSERT INTO currency VALUES ("{}", "{}", "{}")'.format(
            obj.code, obj.name, obj.symbol)
        self.cursor.execute(query)
        self.conn.commit()

    def get(self, code):
        query = 'SELECT * FROM currency WHERE code="{}"'.format(code)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise CurrencyDoesNotExists(
                "No existe la moneda de codigo {}".format(code))
        return Currency(code=data[0], name=data[1], symbol=data[2])

    def filter(self, **kwargs):
        code = kwargs.get('code')
        name = kwargs.get('name')
        symbol = kwargs.get('symbol')

        condition = ' WHERE '
        add_and = False
        add_condition = False

        if code:
            condition += 'code="{}" '.format(code)
            add_condition = True
            add_and = True
        if name:
            if add_and:
                condition += 'AND '
            condition += 'name="{}" '.format(name)
            add_condition = True
            add_and = True
        if symbol:
            if add_and:
                condition += 'AND '
            condition += 'symbol="{}"'.format(symbol)
            add_condition = True

        query = 'SELECT * FROM currency'
        if add_condition:
            query += condition

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        currencies = []
        for data in result:
            currency = Currency(code=data[0], name=data[1], symbol=data[2])
            currencies.append(currency)

        return currencies

    def update(self, old_obj, obj):
        updated = False
        add_comma = False

        query = 'UPDATE currency SET'

        if old_obj.name != obj.name:
            query += 'name"{}"'.format(obj.name)
            updated = True
            add_comma = True
        if old_obj.symbol != obj.symbol:
            if add_comma:
                query += ', '
            query += 'symbol="{}"'.format(obj.symbol)
            updated = True

        if updated:
            query += ' WHERE code="{}"'.format(obj.code)
            self.cursor.execute(query)
            self.conn.commit()

    def save(self, obj):
        try:
            old_obj = self.get(code=obj.code)
        except CurrencyDoesNotExists:
            self.insert(obj)
        else:
            self.update(old_obj, obj)

    def delete(self, obj):
        query = 'DELETE FROM currency WHERE code="{}"'.format(obj.code)
        self.cursor.execute(query)
        self.conn.commit()


class Currency(object):
    "Currency Model"
    objects = CurrencyManager(DB_PATH)

    def __init__(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return u'{}'.format(self.name)


#peso_arg = Currency(code='ARS', name='Peso (Arg)', symbol='$')
#dolar = Currency(code='USD', name='Dolar', symbol='U$S')
#euro = Currency(code='EUR', name='Euro', symbol='Eu')

# Currency.objects.insert(peso_arg)
# Currency.objects.insert(dolar)
# Currency.objects.insert(euro)

# print(Currency.objects.get(code='ARS'))

# print(Currency.objects.get(code='ART'))

# print(Currency.objects.filter(code='EUR'))
# print(Currency.objects.filter(name='Dolar'))
# print(Currency.objects.filter(symbol='Eu'))

# print(Currency.objects.filter())
