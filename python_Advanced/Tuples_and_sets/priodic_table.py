# elements = set()
#
# for _ in range(int(input())):
#     for element in input().split():
#         elements.add(element)
#
# print("\n".join(elements))


print(*{element for _ in range(int(input())) for element in input().split()}, sep="\n")