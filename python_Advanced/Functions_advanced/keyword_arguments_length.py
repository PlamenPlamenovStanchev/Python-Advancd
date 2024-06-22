def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 26}
print(kwargs_length(**dictionary))