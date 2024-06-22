def func_executor(*args):
    # result = []
    # for func, data in args:
    #     result.append(f'{func.__name__} - {func(*data)}')
    #
    # return '\n'.join(result)
    return '\n'.join(f'{func.__name__} - {func(*data)}' for func, data in args)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2

