import random


class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def power(self, *args):
        for x in args:
            self.value **= x
        return self

    def root(self, *args):
        for x in args:
            if x == 0:
                self.value = 'division by zero'
                return self
            self.value **= (1/x)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    calculator = Calculator(random.randint(0, 1000000))
    print(calculator)
    print(calculator.power(2))
    print(calculator.root(2, 2))
