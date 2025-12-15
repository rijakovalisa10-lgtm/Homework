import unittest
import numpy as np
from mnk import mnk_coefficients


class TestMnkCoefficients(unittest.TestCase):

    def test_simple_linear_case(self):
        #Тест на идеально линейные данные.
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]  # y = 2*x + 0
        a, b = mnk_coefficients(x, y)
        self.assertAlmostEqual(a, 2.0, places=10)
        self.assertAlmostEqual(b, 0.0, places=10)

    def test_noisy_linear_case(self):
        #Тест на зашумлённые данные — проверяем разумность результата.
        x = np.linspace(0, 10, 100)
        y_true = 3.5 * x + 2.0
        noise = np.random.normal(0, 0.1, size=x.shape)
        y = y_true + noise
        a, b = mnk_coefficients(x, y)
        self.assertAlmostEqual(a, 3.5, delta=0.05)
        self.assertAlmostEqual(b, 2.0, delta=0.05)

    def test_single_point(self):
        #Тест с одной точкой — система не переопределена, но np.linalg.lstsq всё равно решает.
        x = [5]
        y = [15]
        a, b = mnk_coefficients(x, y)
        self.assertAlmostEqual(a * x[0] + b, y[0], places=10)

    def test_constant_y(self):
        #Тест, когда y — константа (горизонтальная линия).
        x = [1, 2, 3, 4]
        y = [5, 5, 5, 5]
        a, b = mnk_coefficients(x, y)
        self.assertAlmostEqual(a, 0.0, places=10)
        self.assertAlmostEqual(b, 5.0, places=10)

    def test_constant_x(self):
        #Тест, когда x — константа (вертикальная линия — вырожденный случай).
        x = [3, 3, 3, 3]
        y = [1, 2, 3, 4]
        a, b = mnk_coefficients(x, y)
        y_pred = a * x[0] + b
        y_mean = np.mean(y)
        self.assertAlmostEqual(y_pred, y_mean, places=10)

    def test_mismatched_lengths(self):
        #Тест на разную длину x и y — должно быть исключение.
        x = [1, 2, 3]
        y = [1, 2]
        with self.assertRaises(ValueError):
            mnk_coefficients(x, y)

    def test_empty_input(self):
        #Тест на пустые массивы.
        x = []
        y = []
        with self.assertRaises(ValueError):
            mnk_coefficients(x, y)

    def test_numpy_arrays(self):
        #Тест с передачей numpy-массивов.
        x = np.array([0, 1, 2])
        y = np.array([1, 3, 5])  # y = 2*x + 1
        a, b = mnk_coefficients(x, y)
        self.assertAlmostEqual(a, 2.0, places=10)
        self.assertAlmostEqual(b, 1.0, places=10)


if __name__ == '__main__':
    unittest.main()
