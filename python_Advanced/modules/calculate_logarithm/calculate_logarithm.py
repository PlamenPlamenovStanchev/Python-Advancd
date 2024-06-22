import math
# from math import log
number = int(input())

base = input()

if base == 'natural':
    print(f'{math.log(number):.2f}')
#   print(f'{log(number):.2f}')
else:
    base = int(base)
    print(f'{math.log(number, base):.2f}')
#   print(f'{log(number, base):.2f}')

