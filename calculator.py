#calculator class
from math import sqrt

class Calculator:
    """Calculator class doc string

    note: current version uses built-in numeric type. Future version will
    include support for 'bigfloat' in order to allow for more precise
    arithmetic with foating point decimals.
    """

    def __init__(self):
        self._display  = None
        self._number1  = None
        self._number2  = None
        self._operator = None
        self._memory   = None

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, update):
        self._display = update

    @property
    def number1(self):
        return self._number1

    def isNumber(self, number):
        """way of checking that the number to be updated is actually a
        numerical type, but without type checking (which is a no-no in Python)
        """
        return hasattr(number, "__abs__")

    @number1.setter
    def number1(self, update):
        if(self.isNumber(update)):
            self._number1 = update

    @property
    def number2(self):
        return self._number2

    @number2.setter
    def number2(self, update):
        if(self.isNumber(update)):
            self._number2 = update

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

    def multiplicative_inverse(self, number):
        return 1 / number

    def negative(self, number):
        return number * -1

    def clear(self):
        self._number2  = None
        self._operator = None
        self._display  = None

    def all_clear(self):
        self._display  = None
        self._number1  = None
        self._number2  = None
        self._operator = None

    def memory_store(self, number):
        self._display = self._memory

    def memory_recall(self, memory):
        return self._memory

    def memory_clear(self):
        self._memory = None

    def memory_plus(self):
        pass

    def memory_minus(self):
        pass

    def number_button(self, number):
        self._display = number

        if(self._number1 == None and self._number2 == None):
            self._number1 = number

        elif(self._number1 != None and self._number2 == None):
            self._number2 = number

        elif(self._number1 == None and self._number2 != None):
            self._number1 = number

        else:
            self.all_clear()
            self._number1 = number

    def decimal_button(self):
        pass

    def operator_button(self, operator):
        self._operator = operator

    def evaluate(self):
        pass
