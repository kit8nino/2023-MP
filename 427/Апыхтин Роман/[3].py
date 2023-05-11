import numpy as np
import codecs
import random

# функция, которая проверяет, достигнут ли конец лабиринта
def is_exit_position(x, y, maze):
    return (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1) and maze[x][y] == ' '

def coord(maze):
    x, y = random.randint(0, len(maze) - 1), random.randint(0, len(maze[0]) - 1)
    while maze[x][y] != ' ':
        x, y = random.randint(0, len(maze) - 1), random.randint(0, len(maze[0]) - 1)
    return x, y

#поиск в глубину
def dfs(startx, starty, stopx, stopy, graph):
    stack = [(startx, starty)]
    visited = {(startx, starty)}#множество для отслеживания посещённых позиций
    paths = {(startx, starty):[]}# хранение путей от стартовой позиции до каждой посещенной позиции
    while stack:
        x, y = stack.pop()
        if x == stopx and y == stopy:
            return paths[(x, y)], True
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph[0]) and graph[nx][ny] == ' ' and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny))
                paths[(nx, ny)] = paths[(x, y)] + [(x, y)]
    return [], False

#загружаем лабиринт из файла
def load_maze(filename):
    with codecs.open(filename, "r", "utf_8_sig") as f:
        lines = f.readlines()
    maze = np.array([[c for c in line.strip()] for line in lines])
    return maze
maze = load_maze("maze-for-u.txt")
start_x, start_y = coord(maze)#генерация случайных координат для стратовой позиции
key_x, key_y = coord(maze)#генерация случайных координат для позиции ключа

#определяет эвристическую оценку расстояния между точками
def heuristic(x, y, stopx, stopy):
    return abs(x - stopx) + abs(y - stopy)

#функция для поиска оптимального пути А*
def astar(start_x, start_y, exit_x, exit_y, maze, g_weight=1, h_weight=1, max_steps=10000):
    # определяем эвристическую функцию
    def heuristic(x, y, exit_x, exit_y):
        return h_weight * (abs(x - exit_x) + abs(y - exit_y))

    # определяем начальные значения
    open_set = {(start_x, start_y)}#позиции которые нужно пройти
    closed_set = set()#позиции которые пройдены
    g_score = {(start_x, start_y): 0}#хранение значений пути от стратовой позиции до каждой
    f_score = {(start_x, start_y): heuristic(start_x, start_y, exit_x, exit_y)}#хранение значений функции оценки f для каждой позиции
    came_from = dict()#хранение информации о пути от стартовой позиции до каждой позиции

    # находим путь
    for i in range(max_steps):
        #получаем ячейку с наименьшим f_score cell
        curr_x, curr_y = min(open_set, key=lambda cell: f_score[cell])
        if curr_x == exit_x and curr_y == exit_y:
            #строим путь
            path = [(curr_x, curr_y)]
            while (curr_x, curr_y) in came_from:
                curr_x, curr_y = came_from[(curr_x, curr_y)]
                path.append((curr_x, curr_y))
            path.reverse()
            return path, True

        open_set.remove((curr_x, curr_y))
        closed_set.add((curr_x, curr_y))

        #обрабатываем соседние элементы
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = curr_x + dx, curr_y + dy
            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == ' ':
                tent_g_score = g_score[(curr_x, curr_y)] + 1
                if tent_g_score < g_score.get((nx, ny), float('inf')):
                    came_from[(nx, ny)] = (curr_x, curr_y)
                    g_score[(nx, ny)] = tent_g_score
                    f_score[(nx, ny)] = tent_g_score * g_weight + heuristic(nx, ny, exit_x, exit_y) * h_weight
                    if (nx, ny) not in open_set:
                        open_set.add((nx, ny))
    # путь не найден
    return [], False


maze = load_maze("maze-for-u.txt")
start_x, start_y = coord(maze)
key_x, key_y = coord(maze)

path_to_key, success = dfs(start_x, start_y, key_x, key_y, maze)
if not success:
    print("Путь не найден!")
else:
    print("Найденный путь:", path_to_key)

path_to_exit, success = astar(key_x, key_y, len(maze) - 1, len(maze[0]) - 2, maze, g_weight=1, h_weight=2, max_steps=100000)
if not success:
    print("Не удалось найти путь к выходу")
else:
    print("Путь к выходу:", path_to_exit)

#сохранение лабиринта с указанием пути к ключу и выхода из него
maze_with_path = maze.copy()
maze_with_path[key_x][key_y] = '*'

if path_to_key and path_to_exit:
    for x, y in path_to_key:
        maze_with_path[x][y] = '.'
    for x, y in path_to_exit:
        maze_with_path[x][y] = ','
    maze_with_path[len(maze) - 1][len(maze[0]) - 2] = 'E'#обозначение выхода

#запись результата в файл
with codecs.open('maze-for-me-done.txt', 'w', 'utf_8_sig') as f:
    for line in maze_with_path:
        f.write(''.join(line) + '\n')


