def sorting_cheeses(**kwargs):

    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for cheese_name, quantities in sorted_cheeses:
        result += f'{cheese_name}\n'
        reversed_quantity = reversed(quantities)
        for quantity in reversed_quantity:
            result += f'{quantity}\n'

    return result

print(sorting_cheeses())
