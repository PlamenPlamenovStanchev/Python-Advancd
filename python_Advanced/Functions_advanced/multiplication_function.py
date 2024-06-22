from functools import reduce


def multiply(*args):

    return reduce(lambda x, y: x * y, args)

    # total = 1
    # for num in args:
    #     total *= num
    # return total

print(multiply(1,3,5))