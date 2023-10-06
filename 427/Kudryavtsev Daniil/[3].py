#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Метод поиска в глубину

import numpy as np

def read_maze():
    
    """
Функция для чтения лабиринта из файла.
Возвращает размеры лабиринта и сам лабиринт в виде списка строк.
    """
    
    maz = []

    with open('maze-for-u.txt') as maze2:
        for line in maze2:
            maz.append(line.strip('\n'))
        x_max, y_max = len(maz[0]), len(maz)
    return x_max, y_max, maz


def set_point(coord, sign):
    """
   Функция для установки символа в указанной координате лабиринта.
   coord - координата в виде списка [x, y]
   sign - символ для установки
   """
    global maze_list

    maze_row = list(maze_list[coord[1]])
    if maze_row[coord[0]] == '.':
        maze_row[coord[0]] = ';'
        maze_list[coord[1]] = ''.join(maze_row)
    else:
        maze_row[coord[0]] = sign
        maze_list[coord[1]] = ''.join(maze_row)


def get_point(maze, row):
    """
   Функция для получения координаты точки в указанной строке лабиринта.
   maze - лабиринт в виде списка строк
   row - номер строки
   Возвращает координату точки в виде списка [x, y]
   """
    return [maze[row].find(" "), row]


def is_coord_in_maze(maze, coord):
    """
   Функция для проверки того, находится ли указанная координата внутри лабиринта.
   maze - лабиринт в виде списка строк
   coord - координата в виде списка [x, y]
   Возвращает True, если координата находится внутри лабиринта, иначе False.
   """
    if coord[0] < 0 or coord[0] > len(maze[0]) - 1:
        return False
    if coord[1] < 0 or coord[1] > len(maze) - 1:
        return False
    return True


def is_coord_exit(coord):
    """
   Функция для проверки того, является ли указанная координата выходом из лабиринта.
   coord - координата в виде списка [x, y]
   Возвращает True, если координата является выходом из лабиринта, иначе False.
   """
    if coord[1] > len(maze) - 2:
        return True
    return False


def is_coord_treasure(coord):
    """
  Функция для проверки того, является ли указанная координата местоположением сокровища.
  coord - координата в виде списка [x, y]
  Возвращает True, если координата является местоположением сокровища, иначе False.
  """
    global treasure_is_here

    return coord[1] == treasure_is_here[1] and coord[0] == treasure_is_here[0]


def is_path_clean(maze, coord):
    """
    Функция для проверки того, является ли указанная координата свободной от препятствий.
    maze - лабиринт в виде списка строк
    coord - координата в виде списка [x, y]
    Возвращает True, если координата свободна от препятствий, иначе False.
    """
    return maze[coord[1]][coord[0]] != '#'


def step(coord, direction):
    """
   Функция для получения следующей координаты в указанном направлении.
   coord - текущая координата в виде списка [x, y]
   direction - направление движения ('N', 'S', 'W' или 'E')
   Возвращает следующую координату в виде списка [x, y]
   """
    if direction == 'N':
        return step_north(coord)
    elif direction == 'S':
        return step_south(coord)
    elif direction == 'E':
        return step_east(coord)
    elif direction == 'W':
        return step_west(coord)


def step_north(coord):
    """
   Функция для получения следующей координаты при движении на север.
   coord - текущая координата в виде списка [x, y]
   Возвращает следующую координату в виде списка [x, y]
   """
    return [coord[0], coord[1] - 1]


def step_east(coord):
    """
    Функция для получения следующей координаты при движении на восток.
    coord - текущая координата в виде списка [x, y]
    Возвращает следующую координату в виде списка [x, y]
    """
    return [coord[0] + 1, coord[1]]


def step_south(coord):
    """
    Функция для получения следующей координаты при движении на юг.
    coord - текущая координата в виде списка [x, y]
    Возвращает следующую координату в виде списка [x, y]
    """
    return [coord[0], coord[1] + 1]


def step_west(coord):
    """
    Функция для получения следующей координаты при движении на запад.
    coord - текущая координата в виде списка [x, y]
    Возвращает следующую координату в виде списка [x, y]
    """
    return [coord[0] - 1, coord[1]]


def cut_way_back(direction):
    """
    Функция для получения списка возможных направлений движения, исключая обратное направление.
    direction - текущее направление движения ('N', 'S', 'W' или 'E')
    Возвращает список возможных направлений движения
    """
    if direction == 'N':
        return 'N', 'E', 'W'

    if direction == 'S':
        return 'S', 'E', 'W'

    if direction == 'E':
        return 'N', 'E', 'S'

    if direction == 'W':
        return 'N', 'S', 'W'


def recorde_treasure_path(coord):
    """
  Функция для отметки пути от начала лабиринта до сокровища.
  coord - начальная координата в виде списка [x, y]
  """
    global maze_list, path_to_exit

    for node in path_to_exit:
        set_point(coord, '.')
        coord = step(coord, node)


def find_treasure(maze, coord, possible_ways):
    global path_to_exit, current_path

    if is_coord_exit(coord):
        print('Выход')
        return

    if is_coord_treasure(coord):
        path_to_exit = current_path.copy()
        return

    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
            current_path.append(direction)
            find_treasure(maze, step(coord, direction), cut_way_back(direction))
            current_path.pop()
    return


def find_exit(treasure, end):
    dist = 0

    queue = [treasure]

    past_way[treasure[1]][treasure[0]] = 0

    while queue:

        node = queue.pop(0)

        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            temp_x = node[0] + i[0]
            temp_y = node[1] + i[1]
            if not (temp_x < 0 or temp_x >= max_x or temp_y < 0 or temp_y >= max_y):
                if maze[temp_y][temp_x] == " " and past_way[temp_y][temp_x] == -1:
                    past_way[temp_y][temp_x] = [node[0], node[1]]
                    queue.append([temp_x, temp_y])

        temp_x = end[0]
        temp_y = end[1]

    while past_way[temp_y][temp_x] != 0:
        set_point([temp_x, temp_y], ',')
        dist += 1
        temp_x = past_way[temp_y][temp_x][0]
        temp_y = past_way[temp_y][temp_x][1]
        temp_x, temp_y = temp_x, temp_y

    return dist


if __name__ == '__main__':
    max_x, max_y, maze = read_maze()
    maze_list = list(maze)
    POSSIBLE_WAYS = ('N', 'S', 'W', 'E')

    past_way = [[-1 for j in range(max_x)] for i in range(max_y)]

    path_to_exit = []
    for i in range(len(maze) * len(maze[0])):
        path_to_exit.append(' ')
    current_path = []

    start_point = get_point(maze, 0)
    end_point = get_point(maze, max_y - 1)
    print("Начало:", start_point)
    print("Конец:", end_point)

    treasure_is_here = ()

    while not (treasure_is_here and is_path_clean(maze, treasure_is_here)):
        x = np.random.randint(1, max_x - 1)
        y = np.random.randint(1, max_y - 1)

        treasure_is_here = (abs(x) if abs(x) < max_x - 1 else max_x - 1, abs(y) if abs(y) < max_y - 1 else max_y - 1)

    set_point(treasure_is_here, '*')
    print(f"Координаты сокровища: {treasure_is_here}")

    find_treasure(maze, start_point, POSSIBLE_WAYS)

    recorde_treasure_path(start_point)

    dist_from_treasure_to_exit = find_exit(treasure_is_here, end_point)

    f = open('maze-for-me-done.txt', 'w')
    for i in range(len(maze_list)):
        f.write(maze_list[i])
        f.write("\n")
    f.close()
    print('Дистанция от * до выхода: ', dist_from_treasure_to_exit)
-3.py
10 кб

