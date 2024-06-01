import unittest
from equation import *

class TestApp(unittest.TestCase):
    def test_equation(self):
        self.assertEqual(equation(1, 4, 3), [-1, -3])
        self.assertEqual(equation("1", "5", "6"), [-2, -3])
        self.assertEqual(equation(1,3,4), "Действительных корней нет")
        self.assertEqual(equation(1, "", -4), [2, -2])
        self.assertEqual(equation(1, 3, None), [0, -3])
        self.assertEqual(equation(1, 1.5, 0.5), [-0.5, -1])

    def test_coefficients(self):
        self.assertRaises(TypeError, equation, 0, 4, 3)
        self.assertRaises(TypeError, equation, None, 4, 3)
        self.assertRaises(TypeError, equation, 1, "t", 3)
        self.assertRaises(TypeError, equation, 1, 4, "l")


if __name__ == '__main__':
    unittest.main()