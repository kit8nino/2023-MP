# файл maze-for-me-done для ключа с координатами (344,434)
#Сделали Прядко Д.И и Денисова Е.А

from functools import cmp_to_key  # преобразует функцию сравнения в ключ сортировки.
import heapq
import random
wall ='#'

def read_maze():                      # Считываем лабиринт
    maze = []
    with open('maze-for-u.txt', 'r') as file:
        for line in file:
            string = line.strip()
            maze.append(list(string))
    return maze

def save_maze(marked_maze):           # Принимает пройденный лабиринт и сохраняет в файл
    with open('maze-for-me-done.txt', 'w') as file:   
        for i in marked_maze:
            for j in i:
                file.write(f"{j}")
            file.write(f"\n")   


def set_coord(maze):                  # Ставим ключ вруную 
    x_key = 0
    y_key = 0
    check = True
    while check:
        if(maze[x_key][y_key] == wall):
            x_key = int(input('Координаты ключа по x: '))
            y_key = int(input('Координаты ключа по y: '))
        else:
            check = False
        key = (x_key,y_key)
    return key

def mark(maze, path, symbol):         # Помечаем путь
    marked_maze = [row.copy() for row in maze]
    for position in path:
        row, col = position
        marked_maze[row][col] = symbol
    return marked_maze

def rand():                           #Рандомим ключ
    key = ()
    while(not (key and maze[key[0]][key[1]] != wall)):
        x = random.randint(0,598) 
        y = random.randint(0,797)
        key = (x,y)
    return key

#Жадный алгоритм
def calculate_heuristic(node, end):             # расчет эвристического расстояния
    curr_row, curr_col = node
    end_row, end_col = end
    return abs(curr_row - end_row) + abs(curr_col - end_col)

def compare_cells(a, b, end):                   # вычисляет их эвристическое расстояние до end, и возвращает разницу между ними
    return calculate_heuristic(a, end) - calculate_heuristic(b, end)

def sort_cells(cells, end):                 # Результатом функции является отсортированный список cells по возрастанию эвристического расстояния до конечной точки
    return sorted(cells, key=cmp_to_key(lambda a, b: compare_cells(a, b, end)))

def find_greedy_search(maze, start, end):
    queue = [(start, [])]
    visited = set() 

    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path + [current]
        visited.add(current)
        row, col = current
        cells = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        cells = sort_cells(cells, end)
        for cell in cells:
            n_row, n_col = cell
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != "#" and cell not in visited:
                queue.append((cell, path + [current]))

    return None


#A*
def a_sort(maze, start, end, steps): #Считает долго 
    queue = [(0, start, [start])]    #(значекние стоимости,координаты,путь)
    visited = set()                  #(множество для пройденных точек)
    while queue:
        f, point, path = heapq.heappop(queue)
        row = point[0]                
        col = point[1]
        if point == end:
            return path
        visited.add(point)
        for row_step, col_step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:   #всевозможные перемещения 
            row, col = row + row_step, col + col_step
            curr_point = (row, col)
            if (0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1 and (row, col) not in visited):
                new_path = path + [curr_point]
                g = len(new_path)
                h = calculate_heuristic(curr_point, end)
                f = g + h
                if len(queue) < steps:
                    heapq.heappush(queue, (f, curr_point, new_path))
                else:
                    heapq.heappushpop(queue, (f, curr_point, new_path))
    return None


maze = read_maze()
k = int(input("Ручой ввод(-1) , рандомная точка (1): "))
key = rand() if k ==1 else set_coord(maze)

maze[key[0]][key[1]] = '*'   #Помечаем ключ

start = (0, 1)
end = (599, 798)
print("Координаты входа: ", start)
print("Координаты ключа: ", key)
print("Координаты выхода: ", end)

#Используем жадный алгоритм и отмечаем путь '.'
greedy_path = find_greedy_search(maze, start, key)
print("Длина от входа до ключа: ", len(greedy_path))
marked_maze = mark(maze, greedy_path, ".")

max_steps = 4000    

#Используем A* и отмечаем путь ','
a_path = a_sort(maze, key, end, max_steps)
print("Длина от ключа до выхода: ", len(a_path))
arked_maze = mark(marked_maze, a_path, ",")



save_maze(marked_maze)

