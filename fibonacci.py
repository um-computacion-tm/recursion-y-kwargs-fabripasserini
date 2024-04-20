import unittest

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n -1) + fibonacci(n - 2)
    
class Testfibonacci(unittest.TestCase):
    def test1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 0)

    def test2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

    def test5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 3)

    def test7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 8)

    def test9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 21)

unittest.main()