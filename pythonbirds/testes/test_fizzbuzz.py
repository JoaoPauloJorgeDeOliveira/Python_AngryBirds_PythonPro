import unittest
from aula02_fizzbuzz import fizzbuzz

class TesteFizzBuzz(unittest.TestCase):
    def test_com_10(self):
        entrada = 10
        resultado = fizzbuzz(entrada)
        esperado = [
                    '1',
                    'fizz',
                    '3',
                    'fizz',
                    'buzz',
                    'fizz',
                    '7',
                    'fizz',
                    '9',
                    'fizzbuzz'
                    ]
        self.assertListEqual(esperado, resultado)