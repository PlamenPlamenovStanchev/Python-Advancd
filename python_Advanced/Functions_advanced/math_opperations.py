def math_operations(*args, **kwargs):
    operations = {
        'a': lambda x, y: x + y,
        's': lambda x, y: x - y,
        'd': lambda x, y: x / y if y != 0 else x,
        'm': lambda x, y: x * y

    }
    keys = list(operations.keys())
    for i in range(len(args)):
        key = keys[i % 4]
        operation = operations[key]
        kwargs[key] = operation(kwargs[key], args[i])

    # for i in range(len(args)):
    #     if i % 4 == 0:
    #         kwargs['a'] += args[i]
    #     elif i % 4 == 1:
    #         kwargs['s'] -= args[i]
    #     elif i % 4 == 2:
    #         if not args[i] == 0:
    #             kwargs['d'] /= args[i]
    #     else:
    #         kwargs['m'] *= args[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f'{key}: {value:.1f}' for key, value in result)