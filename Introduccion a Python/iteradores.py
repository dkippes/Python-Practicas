lista = [1,2,3]
it = iter(lista)
it
next(it)
next(it)
next(it)
next(it)

class Iterador:
    """
        Iterador que devuelve los elementos de las posiciones pares de una lista
    """
    def __init__(self, data):
        self.data = data
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.data):
            raise StopIteration()
        elem = self.data(self.indice)
        self.indice += 2
        return elem

it = Iterador([])
for e in it:
    print(e)
it = Iterador([1])
for e in it:
    print(e)
it = Iterador([1,2])
for e in it:
    print(e)
it = Iterador([1,2,3,4,5,6])
for e in it:
    print(e)