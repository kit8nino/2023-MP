#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
from heapq import heappop, heappush


maze_file = 'maze-for-u.txt'

#"Устанавливаем ключ в лабиринт", ключ будет лежать в случайной свободной клетке.
def place_key(maze_file):
    with open(maze_file, 'r+') as file:
        maze = [list(line.strip()) for line in file]

        rows = len(maze)
        cols = len(maze[0])

        empty_cells = []

        
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == ' ':
                    empty_cells.append((i, j))

        if len(empty_cells) == 0:
            return False  

        
        key_pos = random.choice(empty_cells)
        maze[key_pos[0]][key_pos[1]] = '*'

        
        file.seek(0)
        file.writelines([''.join(row) + '\n' for row in maze])
        file.truncate()

        return True


success = place_key(maze_file)
if success:
    print("Ключ размещен")
else:
    print("Не удалось разместить ключ")


def read_maze(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip()
            maze.append(list(row))
    return maze


maze = read_maze(maze_file)

#Поиск входа и выхода из лабиринта
def find_start_end(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None
    for i in range(cols):
        if maze[0][i] == ' ':
            start = (0, i)
        if maze[rows - 1][i] == ' ':
            end = (rows - 1, i)
    return start, end


start, end = find_start_end(maze)
print("Координаты входа и выхода: ", start, end)


#Поиск ключа в лабиринте.
def find_key(maze):
    rows = len(maze)
    cols = len(maze[0])

    key = None

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '*':
                key = (i, j)
                break
        if key:
            break
    return key


key = find_key(maze)
print("Координаты ключа: ", key)


def depth_first_search(maze, start, goal):
    visited = set()
    path = []

    def dfs(current):
        if current == goal:
            return True

        visited.add(current)

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (
                0 <= n_row < len(maze)
                and 0 <= n_col < len(maze[0])
                and maze[n_row][n_col] != "#"
                and neighbor not in visited
            ):
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                path.pop()

        return False

    if dfs(start):
        return path
    else:
        return None
    
def a_star_search(maze, start, goal, g_weight, h_weight, max_steps):
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set()

    while queue:
        _, cost, current, path = heappop(queue)
        if current == goal:
            return path + [current]

        visited.add(current)

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (
                0 <= n_row < len(maze)
                and 0 <= n_col < len(maze[0])
                and maze[n_row][n_col] != "#"
                and neighbor not in visited
            ):
                new_cost = cost + 1
                priority = new_cost * g_weight + heuristic(neighbor, goal) * h_weight
                if priority <= max_steps:
                    heappush(queue, (priority, new_cost, neighbor, path + [current]))

    return None




dfs_path_start_to_key = depth_first_search(maze, start, key)

if dfs_path_start_to_key:
    print("Кратчайший путь от входа до ключа (поиск в глубину):")
    print("Длина пути:", len(dfs_path_start_to_key))
    for position in dfs_path_start_to_key:
        print(position)
else:
    print("Путь от входа до ключа не найден (поиск в глубину).")


a_star_g_weight = 1  
a_star_h_weight = 1  
a_star_max_steps = 10000  

a_star_path_key_to_end = a_star_search(maze, key, end, a_star_g_weight, a_star_h_weight, a_star_max_steps)

if a_star_path_key_to_end:
    print("Кратчайший путь от ключа до выхода (A*):")
    print("Длина пути:", len(a_star_path_key_to_end))
    for position in a_star_path_key_to_end:
        print(position)
else:
    print("Путь от ключа до выхода не найден (A*).")
    
def mark_path(maze, path, marker):
    marked_maze = [row.copy() for row in maze]
    for position in path:
        row, col = position
        marked_maze[row][col] = marker
    return marked_maze


marked_dfs_path_start_to_key = mark_path(maze, dfs_path_start_to_key, ".")


marked_a_star_path_key_to_end = mark_path(maze, a_star_path_key_to_end, ",")


marked_combined_maze_file = "maze-for-me-done.txt"
with open(marked_combined_maze_file, "w") as file:
    for row in marked_dfs_path_start_to_key:
        file.write("".join(row) + "\n")
    for row in marked_a_star_path_key_to_end:
        file.write("".join(row) + "\n")

print("Файл с помеченным путем (поиск в глубину + A*) создан: maze-for-me-done.txt")


# In[ ]:




