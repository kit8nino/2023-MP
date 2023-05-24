#!/usr/bin/env python
# coding: utf-8

# In[10]:


import heapq

# Загрузка лабиринта из файла
def load_maze(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

# Сохранение лабиринта в файл
def save_maze(filename, maze):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

# Проверка, является ли данная позиция внутренней точкой лабиринта
def position(maze, x, y):
    height = len(maze)
    width = len(maze[0])
    return 0 <= x < width and 0 <= y < height and maze[y][x] != '#'

# Получение соседних позиций для данной позиции
def get_n(maze, x, y):
    n = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Право, Лево, Вниз, Вверх
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if is_valid_position(maze, nx, ny):
            n.append((nx, ny))
    return n

# Алгоритм Дейкстры для поиска пути от начальной позиции до ключа
def D(maze, start_x, start_y, key_x, key_y):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, []))
    visited = set()

    while queue:
        cost, x, y, path = heapq.heappop(queue)
        if x == key_x and y == key_y:
            return cost, path

        if (x, y) in visited:
            continue

        visited.add((x, y))
        n = get_n(maze, x, y)
        for nx, ny in n:
            if (nx, ny) not in visited:
                new_cost = cost + 1
                new_path = path + [(x, y)]
                heapq.heappush(queue, (new_cost, nx, ny, new_path))

    return float('inf'), None

# Расчет эвристического значения для A*
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Алгоритм A* для поиска оптимального пути от начальной позиции до ближайшего выхода
def ast(maze, start_x, start_y):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, []))
    visited = set()

    while queue:
        cost, x, y, path = heapq.heappop(queue)
        if maze[y][x] == 'E':
            return cost, path

        if (x, y) in visited:
            continue

        visited.add((x, y))
        n = get_n(maze, x, y)
        for nx, ny in n:
            if (nx, ny) not in visited:
                new_cost = cost + 1
                new_path = path + [(x, y)]
                h = heuristic(nx, ny, start_x, start_y)
                heapq.heappush(queue, (new_cost + h, nx, ny, new_path))

    return float('inf'), None

# Загрузка лабиринта из файла
maze = load_maze('maze-for-u.txt')

# Координаты аватара и ключа (выберите или задайте сами)
avatar_x = 1
avatar_y = 1
key_x = 7
key_y = 7

# Поиск пути от аватара до ключа с использованием алгоритма Дейкстры
D_cost, D_path = D(maze, avatar_x, avatar_y, key_x, key_y)

# Поиск оптимального пути от аватара до ближайшего выхода с использованием алгоритма A*
ast_cost, ast_path = ast(maze, avatar_x, avatar_y)

# Обозначение ключа и маршрута в лабиринте
maze[key_y][key_x] = '*'
for x, y in D_path:
    maze[y][x] = '.'
for x, y in ast_path:
    maze[y][x] = ','

# Сохранение лабиринта с обозначенным ключом и маршрутом
save_maze('maze-for-me-done.txt', maze)

# Вывод информации о пути
print("Длина пути до ключа:", D_cost)
print("Оптимальный путь до ключа:")
for point in D_path:
    print(point)
print()
print("Длина пути до ближайшего выход:", ast_cost)
print("Оптимальный путь до ближайшего выхода:")
for point in ast_path:
    print(point)


# In[ ]:




