#calculator class
from math import sqrt

class Calculator:
    """Calculator class doc string

    note: current version uses built-in numeric type. Future version will
    include support for 'bigfloat' in order to allow for more precise
    arithmetic with foating point decimals.
    """

    def __init__(self):
        self._display  = 0
        self._number_1 = 0
        self._number_2 = 0
        self._operator = ""
        self._memory   = 0

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, update):
        self._display = update

    @property
    def number_1(self):
        return self._number_1

    @number_1.setter
    def number_1(self, update):

        if(hasattr(update, "__abs__")):
        """way of checking that the number to be updated is actually a
        numerical type, but without type checking (which is a no-no in Python)
        """
        self._number_1 = update

    @property
    def number_2(self):
        return self._number_2

    @number_2.setter
    def number_2(self, update):

        if(hasattr(update, "__abs__")):
        """way of checking that the number to be updated is actually a
        numerical type, but without type checking (which is a no-no in Python)
        """
        self._number_2 = update

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, update):
        self._operator = update

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, update):
        self._memory = update

    def enter_number(self, number):
        self.display = number
        return self.display

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def square(self, base):
        return base ** 2

    def square_root(self, radicand):
        return math.sqrt(radicand)

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def inverse(self, number):
        return 1 / number

    def evaluate(self):


