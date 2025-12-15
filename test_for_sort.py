from quicksort import quicksort
import unittest

class TestQuicksort(unittest.TestCase):

    def test_sorted_list(self):
        #Тест на уже отсортированный список.
        arr = [1, 2, 3, 4, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        #Тест на список, отсортированный в обратном порядке.
        arr = [5, 4, 3, 2, 1]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_list(self):
        #Тест на случайный список.
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_empty_list(self):
        #Тест на пустой список.
        arr = []
        result = quicksort(arr)
        self.assertEqual(result, [])

    def test_single_element(self):
        #Тест на список из одного элемента.
        arr = [42]
        result = quicksort(arr)
        self.assertEqual(result, [42])

    def test_all_equal_elements(self):
        #Тест на список с одинаковыми элементами.
        arr = [7, 7, 7, 7]
        result = quicksort(arr)
        self.assertEqual(result, [7, 7, 7, 7])

    def test_negative_numbers(self):
        #Тест с отрицательными числами.
        arr = [-3, -1, -4, -1, -5]
        result = quicksort(arr)
        self.assertEqual(result, [-5, -4, -3, -1, -1])

    def test_mixed_positive_negative_zero(self):
        #Тест с отрицательными, нулём и положительными числами.
        arr = [0, -1, 5, -10, 3, 0, 2]
        result = quicksort(arr)
        self.assertEqual(result, [-10, -1, 0, 0, 2, 3, 5])

    def test_large_list(self):
       # Тест на большой список.
        import random
        arr = list(range(1000))
        random.shuffle(arr)
        result = quicksort(arr)
        self.assertEqual(result, list(range(1000)))

    def test_non_integer_elements(self):
        #Тест с числами с плавающей точкой (если функция универсальна).
        arr = [3.5, 1.2, 4.8, 1.2, 0.1]
        result = quicksort(arr)
        self.assertEqual(result, [0.1, 1.2, 1.2, 3.5, 4.8])

    def test_strings(self):
        #Тест сортировки строк (если функция поддерживает сравнение объектов).
        arr = ["banana", "apple", "cherry"]
        result = quicksort(arr)
        self.assertEqual(result, ["apple", "banana", "cherry"])
        
        
if __name__ == '__main__':
    unittest.main()