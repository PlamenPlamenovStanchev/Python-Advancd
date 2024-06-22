# from collections import  deque
#
#
# expression = input().split()
# numbers = deque()
#
# for char in expression:
#     if char not in '+-*/':
#         numbers.append(int(char))
#     else:
#         while len(numbers) > 1:
#             first_num = numbers.popleft()
#             second_num = numbers.popleft()
#             if char == "+":
#                 numbers.appendleft(first_num + second_num)
#             elif char == "-":
#                 numbers.appendleft(first_num - second_num)
#             elif char == "*":
#                 numbers.appendleft(first_num * second_num)
#             elif char == "/":
#                 numbers.appendleft(first_num // second_num)
#
# print(numbers[0])




# from collections import  deque
#
#
# expression = input().split()
# numbers = deque()
#
# for char in expression:
#     if char not in '+-*/':
#         numbers.append(int(char))
#     else:
#         while len(numbers) > 1:
#             first_num = numbers.popleft()
#             second_num = numbers.popleft()
#             numbers.appendleft(eval(str(first_num) + char + str(second_num)))
#
# print(numbers[0])


from collections import deque


expression = input().split()
numbers = deque()

opperators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(opperators[char](first_num, second_num))

print(numbers[0])




