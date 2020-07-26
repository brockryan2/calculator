# Unit Tests for calculator

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_initialize(self):
        test_calc = Calculator()
        self.assertIsInstance(test_calc, Calculator)

        test_calc.enter_number(10)
        self.assertEqual(test_calc.display, 10)


    def test_add(self):
        test_calc = Calculator()
        test_calc.enter_number(10)

        test_add_int = test_calc.add(10)
        self.assertEqual(test_add_int, 20)

        test_calc.enter_number(10.999)
        test_add_float = test_calc.add(10.333)
        self.assertEqual(test_add_float, 21.332)


    def test_subtract(self):
        test_calc = Calculator()
        test_calc.enter_number(10)

        test_subtract_int = test_calc.subtract(10)
        self.assertEqual(test_subtract_int, 0)

        test_calc.enter_number(10)
        test_subtract_float = test_calc.subtract(10.5)
        self.assertEqual(test_subtract_float, -0.5)


    def test_multiply(self):
        test_calc = Calculator()
        test_calc.enter_number(10)

        test_multiply_int = test_calc.multiply(10)
        self.assertEqual(test_multiply_int, 100)

        test_calc.enter_number(0.5)
        test_multiply_float = test_calc.multiply(0.5)
        self.assertEqual(test_multiply_float, 0.25)


    def test_divide(self):
        test_calc = Calculator()
        test_calc.enter_number(10)

        test_divide_int = test_calc.divide(10)
        self.assertEqual(test_divide_int, 1)

        test_calc.enter_number(0.5)
        test_divide_float = test_calc.divide(1.25)
        self.assertEqual(test_divide_float, 0.4)


if __name__ == '__main__':
    unittest.main()
