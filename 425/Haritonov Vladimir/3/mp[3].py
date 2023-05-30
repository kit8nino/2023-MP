import random
import heapq
import sys

#Функция set_avatar_position -Генерирует случайные координаты (строка и столбец).Устанавливает символ A на начальной позиции аватара и возвращает координаты начальной позиции аватара в виде кортежа (start_row, start_col).
def set_avatar_position(maze):
    rows = len(maze)
    cols = len(maze[0])
    start_row = random.randint(0, rows-1)
    start_col = random.randint(0, cols-1)
    while maze[start_row][start_col] == '#': # Проверяем позицию аватара, если он находится в стене, то изменяем положение
        start_row = random.randint(0, rows-1)
        start_col = random.randint(0, cols-1)
    maze[start_row][start_col] = 'A'
    return (start_row, start_col)
#Функция set_key_position - Генерирует случайные координаты (строка и столбец).Проверяет, чтобы позиция ключа не была в стене (#) или на нач. поз-ии аватара (A).
#Устанавливает символ * на позиции ключа в лабиринте.
# Возвращает координаты позиции ключа в виде кортежа (key_row, key_col).
def set_key_position(maze):
    rows = len(maze)
    cols = len(maze[0])
    key_row = random.randint(0, rows-1)
    key_col = random.randint(0, cols-1)
    while maze[key_row][key_col] == '#' or maze[key_row][key_col] == 'A':  # Проверяем, что позиция не является стеной или начальной позицией аватара
        key_row = random.randint(0, rows-1)
        key_col = random.randint(0, cols-1)
    maze[key_row][key_col] = '*'  # Обозначаем позицию ключа
    return (key_row, key_col)
#Функция read_maze - принимает путь к файлу с лабиринтом в качестве аргумента. Открывает файл и читает его содержимое.
#Создает двумерный список maze, представляющий лабиринт, где каждый символ в файле представляет одну ячейку лабиринта и удаляет лишние символы.Преобразует каждую строку в список символов.
#Возвращает полученный двумерный список maze, представляющий лабиринт.
def read_maze(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            maze.append(row)
    return maze
maze_file = 'maze-for-u.txt' 
maze = read_maze(maze_file)
#Функция find_entrance - скарнирует первую строку лабиринта и находит пустой символ, который и является входом
def find_entrance(maze):
    for col, cell in enumerate(maze[0]):
        if cell == ' ':  # Проверяем, является ли ячейка входом (пропуском в стене)
            return (0, col)
    return None
#Функция find_exit - скарнирует последнюю строку лабиринта и находит пустой символ, который и является выходом
def find_exit(maze):
    last_row = len(maze)-1
    for col, cell in enumerate(maze[last_row]):
        if cell == ' ':  # Проверяем, является ли ячейка выходом (пропуском в стене)
            return (last_row, col)
    return None 
# Функция для нахождения оптимального пути с использованием алгоритма A*
def find_optimal_path(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    g_scores = [[sys.maxsize] * cols for _ in range(rows)]  # Инициализация всех g-значений бесконечностью
    g_scores[start[0]][start[1]] = 0  # g-значение для начальной точки равно 0
    f_scores = [[sys.maxsize] * cols for _ in range(rows)]  # Инициализация всех f-значений бесконечностью
    f_scores[start[0]][start[1]] = heuristic(start, end)  # f-значение для начальной точки равно эвристической оценке
    open_set = [(f_scores[start[0]][start[1]], start)]  # Открытое множество с приоритетом для выбора следующей точки
    closed_set = set()  # Закрытое множество для посещенных точек
    came_from = {}  # Словарь для отслеживания предыдущей точки в оптимальном пути

    while open_set:
        current_f, current_pos = heapq.heappop(open_set)
        if current_pos == end:
            return reconstruct_path(came_from, end)
        closed_set.add(current_pos)
        neighbors = get_neighbors(current_pos, maze)
        for neighbor in neighbors:
            if neighbor in closed_set:
                continue
            tentative_g = g_scores[current_pos[0]][current_pos[1]] + 1  # Расстояние между соседними точками равно 1
            if tentative_g < g_scores[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current_pos
                g_scores[neighbor[0]][neighbor[1]] = tentative_g
                f_scores[neighbor[0]][neighbor[1]] = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_scores[neighbor[0]][neighbor[1]], neighbor))
    return None  # Если путь не найден

# Функция для восстановления оптимального пути
def reconstruct_path(came_from, current_pos):
    path = []
    while current_pos in came_from:
        path.append(current_pos)
        current_pos = came_from[current_pos]
    path.reverse()
    return path

# Функция для эвристической оценки (в данном случае - прямое расстояние между точками)
def heuristic(start, end):
    return abs(end[0]-start[0])+abs(end[1]-start[1])

maze_file = 'maze-for-u.txt'
maze = read_maze(maze_file)
avatar_position = set_avatar_position(maze)
key_position = set_key_position(maze)
entrance_position = find_entrance(maze)
exit_position = find_exit(maze)
print("Начальная позиция аватара:", avatar_position)
print("Позиция ключа:", key_position)
print("Позиция входа в лабиринт:", entrance_position)
print("Позиция выхода из лабиринта:", exit_position)

optimal_path = find_optimal_path(maze, avatar_position, exit_position)
if optimal_path is not None:
    print("Оптимальный путь до ближайшего выхода:", optimal_path)

# Обновление лабиринта с указанием ключа и пути
maze_with_path = maze.copy()
for pos in optimal_path:
    maze_with_path[pos[0]][pos[1]] = '?'
maze_with_path[key_position[0]][key_position[1]] = '*'

# Сохранение лабиринта с путем в файл 'maze-for-me-done.txt'
maze_done_file = 'maze-for-me-done.txt'
with open(maze_done_file, 'w') as f:
    for row in maze_with_path:
        line = ''.join(row)
        f.write(line+'\n')

print("Лабиринт с путем сохранен в файл 'maze-for-me-done.txt'.")
