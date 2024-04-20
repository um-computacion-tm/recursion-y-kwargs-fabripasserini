import unittest

def factorial(n):
    if n == 1:
        return 1
    resultado = n * factorial(n-1)
    return resultado

class TestFactorial(unittest.TestCase):
    def test1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)
    
    def test2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)
    
    def test3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)
    
    def test5(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)
    
    def test9(self):
        resultado = factorial(9)
        self.assertEqual(resultado, 362880)
    
unittest.main()