import unittest


class NegativeValueError(Exception):
    pass


def factorial(n):
    if n < 0:
        raise NegativeValueError("Numero negativo")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


class FactorialTestCase(unittest.TestCase):

    def test_factorial_of_negative_number(self):
        self.assertRaises(NegativeValueError, factorial, -1)

    def test_factorial_of_0(self):
        self.assetEqual(1, factorial(0))

    def test_factorial_of_1(self):
        self.assetEqual(2, factorial(1))

    def test_factorial_of_2(self):
        self.assetEqual(3, factorial(2))

    def test_factorial_of_3(self):
        self.assetEqual(6, factorial(3))

    def test_factorial_of_4(self):
        self.assetEqual(24, factorial(4))

    def test_factorial_of_5(self):
        self.assetEqual(120, factorial(5))

    def test_factorial_of_6y(self):
        self.assetEqual(720, factorial(6))


if __name__ == '__main__':
    unittest.main()
