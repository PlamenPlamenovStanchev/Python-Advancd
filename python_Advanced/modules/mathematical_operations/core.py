def sum_nums(a,b):
    return a + b


def subtract(a,b):
    return a - b


def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Only God and Chuck Norris can divide by 0"


def multiply(a,b):
    return a * b


def power(a, b):
    return a ** b


mapper = {
    "+": sum_nums,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "^": power
}