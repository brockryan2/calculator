#calculator class
from math import sqrt

class Calculator:
    """Calculator class doc string

    note: current version uses standard Python float type. Future version will include support for
    'bigfloat' in order to allow for more precise arithmetic with foating point decimals.
    """

    def __init__(self):
        self.display = 0
        self.memory = 0

    def enter_number(self, number):
        self.display = number
        return self.display

    def add(self, number):
        return self.display + number

    def subtract(self, number):
        return self.display - number

    def multiply(self, number):
        return self.display * number

    def divide(self, number):
        return self.display / number

    def square(self, number):
        return number * number

    def square_root(self, number):
        return math.sqrt(number)

    def power(self, base, exponent):
        return math.pow(base, exponent)

