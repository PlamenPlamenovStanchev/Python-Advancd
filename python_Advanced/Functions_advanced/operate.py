from functools import reduce

mapper = {
    '+': lambda num: reduce(lambda x, y: x + y, num),
    '-': lambda num: reduce(lambda x, y: x - y, num),
    '*': lambda num: reduce(lambda x, y: x * y, num),
    '/': lambda num: reduce(lambda x, y: x / y, num),
}

def operate(operator, *args):
    # if operator == '+':
    #     return reduce(lambda x, y: x + y, args)
    # elif operator == '-':
    #     return reduce(lambda x, y: x - y, args)
    # elif operator == '*':
    #     return reduce(lambda x, y: x * y, args)
    # elif operator == '/':
    #     if 0 in args:
    #         return 'Can not divide by zero'
    #     return reduce(lambda x, y: x / y, args)
    return mapper[operator](args)

print(operate('+', 1, 2, 3))