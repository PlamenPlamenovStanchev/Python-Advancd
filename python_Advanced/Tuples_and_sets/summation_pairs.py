# numbers = list(map(int, input().split()))
# target = int(input())
#
#
# for i in range(len(numbers)):
#     if numbers[i] == " ":
#         continue
#     for j in range(i+1, len(numbers)):
#         if numbers[j] == " ":
#             continue
#         if numbers[i] + numbers[j] == target:
#             print(f"{numbers[i]} + {numbers[j]} = {target}")
#             numbers[i] = " "
#             numbers[j] = " "
#             break

numbers = list(map(int, input().split()))
target = int(input())

target_set = set()
map_values = {}


for value in numbers:
    if value in target_set:
        target_set.remove(value)
        pair = map_values[value]
        del map_values[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        target_set.add(resulting_number)
        map_values[resulting_number] = value