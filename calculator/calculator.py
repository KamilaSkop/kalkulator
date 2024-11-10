class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Nie można dzielić przez zero")
        return a / b

    def modulus(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b
