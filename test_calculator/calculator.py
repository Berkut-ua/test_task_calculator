import types

class CalculationStrategy:
    def __init__(self, func = None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self, x, y):
        return 0
    


def addition(self, x, y):
    return x + y


def subtraction(self, x, y):
    return x - y


def multiplication(self, x, y):
    return x * y


def division(self, x, y):
    return x / y if y > 0 else 'Error'


def calculate(src_data,
              result_type = lambda r: {'result': r}):
    operations = {'+': addition,
                  '-': subtraction,
                  '*': multiplication,
                  '/': division}

    strat = CalculationStrategy(operations[src_data[1]])
    
    return result_type(strat.execute(src_data[0], src_data[2]))
