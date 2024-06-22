n = int(input())
field = [list(input()) for _ in range(n)]
bee_energy = 15
collected_nectar = 0
bee_position = None
hive_position = None

for row in range(n):
    for col in range(n):
        if field[row][col] == 'B':
            bee_position = (row, col)
        elif field[row][col] == 'H':
            hive_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    row_movement, col_movement = directions[command]
    new_row, new_col = (bee_position[0] + row_movement) % n, (bee_position[1] + col_movement) % n

    if field[new_row][new_col].isdigit():
        collected_nectar += int(field[new_row][new_col])
        field[new_row][new_col] = '-'

    field[bee_position[0]][bee_position[1]] = '-'
    bee_position = (new_row, new_col)
    field[new_row][new_col] = 'B'

    bee_energy -= 1

    if bee_position == hive_position:
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if bee_energy == 0:
        if collected_nectar >= 30:
            bee_energy += collected_nectar - 30
            collected_nectar = 30
            if bee_energy == 0:
                print("This is the end! Beesy ran out of energy.")
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            break

for row in field:
    print(''.join(row))


# n = int(input())
# field = [list(input()) for _ in range(n)]
# bee_energy = 15
# collected_nectar = 0
# bee_position = None
# hive_position = None
#
# for i in range(n):
#     for j in range(n):
#         if field[i][j] == 'B':
#             bee_position = (i, j)
#         elif field[i][j] == 'H':
#             hive_position = (i, j)
#
# while True:
#     command = input()
#     new_i, new_j = bee_position
#     if command == 'up':
#         new_i = (new_i - 1) % n
#     elif command == 'down':
#         new_i = (new_i + 1) % n
#     elif command == 'left':
#         new_j = (new_j - 1) % n
#     elif command == 'right':
#         new_j = (new_j + 1) % n
#
#     if field[new_i][new_j].isdigit():
#         collected_nectar += int(field[new_i][new_j])
#         field[new_i][new_j] = '-'
#
#     field[bee_position[0]][bee_position[1]] = '-'
#     bee_position = (new_i, new_j)
#     field[new_i][new_j] = 'B'
#
#     bee_energy -= 1
#
#     if bee_position == hive_position:
#         if collected_nectar >= 30:
#             print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
#         else:
#             print("Beesy did not manage to collect enough nectar.")
#         break
#
#     if bee_energy == 0:
#         if collected_nectar >= 30:
#             bee_energy += collected_nectar - 30
#             collected_nectar = 30
#             if bee_energy == 0:
#                 print("This is the end! Beesy ran out of energy.")
#                 break
#         else:
#             print("This is the end! Beesy ran out of energy.")
#             break
#
# for row in field:
#     print(''.join(row))