# преобразуем лабиринт в матрицу
with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


# найдем координаты старта и ключа
def get_data(maze):

    x_start = int(input('Координаты аватара X: '))
    y_start = int(input('Координаты аватара Y: '))

    x_key = int(input('Координаты ключа X : '))
    y_key = int(input('Координаты ключа Y : '))
    maze[x_key][y_key] = " "

    start = (x_start, y_start)
    key = (x_key, y_key)

    return start, key


# Поиск в глубину
def dfs(start, end, maze):
    len_maze_y = len(maze[0])
    len_maze_x = len(maze)
    stack = [start]
    visited = {start}
    paths = {start: []}

    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            return paths[current_pos]

        x_coord, y_coord = current_pos

        # проверяем все возможные направления движения
        if (x_coord - 1) >= 0 and maze[x_coord - 1][y_coord] == " " and (x_coord - 1, y_coord) not in visited:
            stack.append((x_coord - 1, y_coord))
            visited.add((x_coord - 1, y_coord))
            paths[(x_coord - 1, y_coord)] = paths[current_pos] + [current_pos]

        if (x_coord + 1) < len_maze_x and maze[x_coord + 1][y_coord] == " " and (x_coord + 1, y_coord) not in visited:
            stack.append((x_coord + 1, y_coord))
            visited.add((x_coord + 1, y_coord))
            paths[(x_coord + 1, y_coord)] = paths[current_pos] + [current_pos]

        if (y_coord - 1) >= 0 and maze[x_coord][y_coord - 1] == " " and (x_coord, y_coord - 1) not in visited:
            stack.append((x_coord, y_coord - 1))
            visited.add((x_coord, y_coord - 1))
            paths[(x_coord, y_coord - 1)] = paths[current_pos] + [current_pos]

        if (y_coord + 1) < len_maze_y and maze[x_coord][y_coord + 1] == " " and (x_coord, y_coord + 1) not in visited:
            stack.append((x_coord, y_coord + 1))
            visited.add((x_coord, y_coord + 1))
            paths[(x_coord, y_coord + 1)] = paths[current_pos] + [current_pos]

    return None


start, key = get_data(maze)
pathToKey = dfs(start, key, maze)

for coords in pathToKey:
    x, y = coords
    maze[x][y] = "."
    maze[key[0]][key[1]] = '*'

with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")
