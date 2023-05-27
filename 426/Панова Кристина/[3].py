import heapq


def parse_maze(maze_file):
    with open(maze_file, 'r') as file:
        return [list(line) for line in file]


def neighbors(maze, current):
    x, y = current
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            yield (nx, ny)


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_path(maze, start, end, algorithm='a*'):
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while queue:
        _, current = heapq.heappop(queue)
        if current == end:
            break
        for next in neighbors(maze, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (0 if algorithm == 'dijkstra' else heuristic(end, next))
                heapq.heappush(queue, (priority, next))
                came_from[next] = current

    if current != end:
        return None  # No path found

    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def save_maze(maze, maze_file, path_to_key, path_to_exit):
    for cell in path_to_key:
        maze[cell[0]][cell[1]] = '.'
    maze[path_to_key[-1][0]][path_to_key[-1][1]] = '*'
    for cell in path_to_exit[1:]:
        maze[cell[0]][cell[1]] = ','
    with open(maze_file, 'w') as file:
        file.writelines(''.join(row) for row in maze)



maze_file = 'maze-for-u.txt'
maze = parse_maze(maze_file)
avatar_coord = (1, 1)  # заменить на реальные координаты
key_coord = (1, 2)  # заменить на реальные координаты
exit_coord = (2, 2)  # заменить на реальные координаты

path_to_key = find_path(maze, avatar_coord, key_coord, algorithm='dijkstra')
if path_to_key is None:
    print("Не существует пути от ключа до выхода.")

path_to_exit = find_path(maze, key_coord, exit_coord, algorithm='a*')
if path_to_exit is None:
    print("Не существует пути от ключа до выхода.")

save_maze(maze, 'maze-for-me-done.txt', path_to_key, path_to_exit)

