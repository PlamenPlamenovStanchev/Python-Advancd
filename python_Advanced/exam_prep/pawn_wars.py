def print_matrix(matrix):
    print()

    [print(' '.join(el)) for el in matrix]
    print()


def is_index_in_range(index):
    if 0 <= index < 8:
        return True
    return False


def diagonals_interaction(current_position, matrix, direction='up'):
    row, col = current_position
    target = 'b'

    if direction != "up":
        row += 1
        target = 'w'
    else:
        row -= 1

    to_right_col = col + 1
    to_left_col = col - 1
    if is_index_in_range(row) and is_index_in_range(to_right_col) and matrix[row][to_right_col] == target:
        return row, to_right_col
    elif is_index_in_range(row) and is_index_in_range(to_left_col) and matrix[row][to_left_col] == target:
        return row, to_left_col


def is_queen(row, end_row):
    if row == end_row:
        return True
    return False


rows = 8
starting_letter = ord('a')

row_mapper = {}
column_mapper = {}

for i in range(rows):
    row_mapper[i] = rows - i

for i in range(rows):
    column_mapper[i] = chr(starting_letter + i)

matrix = []

white_pawns_coords = []
black_pawns_coords = []

for row_num in range(8):
    row_data = input().split()
    if "w" in row_data:
        white_pawns_coords = [row_num, row_data.index("w")]
    if "b" in row_data:
        black_pawns_coords = [row_num, row_data.index("b")]
    matrix.append(row_data)


def play_a_move(matrix, white_pawns_coords, black_pawns_coords):
    # White plays
    coords = diagonals_interaction(white_pawns_coords, matrix)
    if coords:
        print(f"Game over! White win, capture on {column_mapper[coords[1]]}{row_mapper[coords[0]]}.")
        exit()
    # Move forward
    matrix[white_pawns_coords[0]][white_pawns_coords[1]] = '-'
    white_pawns_coords = [white_pawns_coords[0] - 1, white_pawns_coords[1]]
    matrix[white_pawns_coords[0]][white_pawns_coords[1]] = 'w'

    if is_queen(white_pawns_coords[0], 0):
        print(
            f"Game over! White pawn is promoted to a queen at {column_mapper[white_pawns_coords[1]]}{row_mapper[white_pawns_coords[0]]}.")
        exit()

    # Black plays
    coords = diagonals_interaction(black_pawns_coords, matrix, direction='down')
    if coords:
        print(f"Game over! Black win, capture on {column_mapper[coords[1]]}{row_mapper[coords[0]]}.")
        exit()
    # Move forward
    matrix[black_pawns_coords[0]][black_pawns_coords[1]] = '-'
    black_pawns_coords = [black_pawns_coords[0] + 1, black_pawns_coords[1]]
    matrix[black_pawns_coords[0]][black_pawns_coords[1]] = 'b'

    if is_queen(black_pawns_coords[0], 7):
        print(
            f"Game over! Black pawn is promoted to a queen at {column_mapper[black_pawns_coords[1]]}{row_mapper[black_pawns_coords[0]]}.")
        exit()

    return matrix, white_pawns_coords, black_pawns_coords


while True:
    matrix, white_pawns_coords, black_pawns_coords = play_a_move(matrix, white_pawns_coords, black_pawns_coords)
    # Visually move the pawns

    # print_matrix(matrix)