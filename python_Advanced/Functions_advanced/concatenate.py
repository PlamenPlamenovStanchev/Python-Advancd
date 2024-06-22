def concatenate(*args, **kwargs):
    result = ''.join(args)
    # for string in args:
    #     result += string

    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result