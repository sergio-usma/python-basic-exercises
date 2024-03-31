class Arithmetic:
    """
    Arithmetic class do the sum, subtraction, etc. operations.
    """

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2


op1 = Arithmetic(5, 3)
print(f'Sum: {op1.sum()}')
print(f'Subtract: {op1.subtract()}')
print(f'Multiplication: {op1.multiply()}')
print(f'Division: {op1.divide():.2f}')



