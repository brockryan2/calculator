# Unit Tests for calculator

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    result = Calculator.add(10, 3, 7)
    self.assertEqual(result, 20)




if __name__ == '__main__':
  unittest.main()
