n = int(input())

health = 100
maze = []
t_row, t_col = 0, 0

for row in range(n):
    maze.append([x for x in input()])
    for col in range(n):
        if maze[row][col] == "P":
            t_row, t_col = row, col

movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    move = input()

    if not(0 <= t_row + movement[move][0] < n and 0 <= t_col + movement[move][1] < n):
        continue

    maze[t_row][t_col] = "-"
    t_row += movement[move][1]
    t_col += movement[move][0]

    if maze[t_row][t_col] == "X":
        print("Player escaped the maze. Danger passed!")
        maze[t_row][t_col] = "P"
        break
    elif maze[t_row][t_col] == "H":
        health = min(health + 15, 100)
    elif maze[t_row][t_col] == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead, Maze over!")
            maze[t_row][t_col] = "P"
            break

    maze[t_row][t_col] = "P"

print(f"Player's health: {health} units")
for row in maze:
    print(''.join(row))
    