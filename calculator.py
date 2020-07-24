#calculator class
from math import sqrt

class Calculator:

    def __init__(self):
        self.display = 0
        self.memory = 0

    def enter_number(self, number):
        self.display = number
        return self.display

    def add(self, number):
        return display + number

    def subtract(self, number):
        return display - number

    def multiply(self, number):
        return display * number

    def divide(self, number):
        return display / number

    def square(self, number):
        return display ** number

    def square_root(self, number):
        return math.sqrt(number)

    def power(self, base, exponent):
        return math.pow(base, exponent)

