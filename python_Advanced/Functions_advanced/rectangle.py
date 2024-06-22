def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values'

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f'Rectangle area: {area()}\n Rectangle perimeter: {perimeter()}'

print(rectangle(4,5))

