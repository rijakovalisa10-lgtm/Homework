import unittest
from prime_factors import prime_factors

class TestPrimeFactors(unittest.TestCase):

    def test_prime_number(self):
        #Тест: простое число должно вернуть себя.
        self.assertEqual(prime_factors(7), [7])
        self.assertEqual(prime_factors(13), [13])

    def test_composite_number(self):
        #Тест: составное число.
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(100), [2, 2, 5, 5])

    def test_power_of_prime(self):
        #Тест: степень простого числа.
        self.assertEqual(prime_factors(8), [2, 2, 2])
        self.assertEqual(prime_factors(27), [3, 3, 3])

    def test_one_and_zero(self):
        #Тест: граничные случаи.
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(-5), [])

    def test_two(self):
        #Тест: самое маленькое простое число.
        self.assertEqual(prime_factors(2), [2])

    def test_large_number(self):
        #Тест: большое число.
        self.assertEqual(prime_factors(999), [3, 3, 3, 37])
        self.assertEqual(prime_factors(1001), [7, 11, 13])

if __name__ == '__main__':
    unittest.main()