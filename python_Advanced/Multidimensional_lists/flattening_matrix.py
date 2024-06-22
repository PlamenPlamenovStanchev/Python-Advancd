rows_count = int(input())

matrix = []

for i in range(rows_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)
        # flattened.extend(row_data)

print(flattened)