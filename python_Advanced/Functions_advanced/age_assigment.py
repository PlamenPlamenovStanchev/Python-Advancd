def age_assignment(*args, **kwargs):
    persons = {name: kwargs[name[0]] for name in args}
    # for name in args:
    #     persons[name] = kwargs[name[0]]

    persons = sorted(persons.items())

    # result = []
    # for name, age in persons:
    #     result.append(f'{name} is {age} years old.')

    return '\n'.join(f'{name} is {age} years old.' for name, age in persons)

