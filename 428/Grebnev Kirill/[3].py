# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:29:33 2023

@author: Кирилл
"""

import numpy as np
import random
import codecs


#Загружаем файл с текстовым представлением лабиринта
def load_maze(filename):
    with codecs.open(filename, "r", "utf_8_sig") as f:
        lines = f.readlines()
    maze = np.array([[c for c in line.strip()] for line in lines])
    return maze
maze = load_maze("maze-for-u.txt")


#Проверка достижения конца лабиринта
def end_of_maze(x, y, maze):
     (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1) and maze[x][y] == ' '

def coord(maze):
    x = random.randint(0, len(maze) - 1)
    y = random.randint(0, len(maze[0]) - 1)
    while maze[x][y] != ' ':
        x = random.randint(0, len(maze) - 1)
        y = random.randint(0, len(maze[0]) - 1)
    return x, y
start_x, start_y = coord(maze)#координаты для стратовой позиции
key_x, key_y = coord(maze)#координаты для позиции ключа

#Поиск в глубину
def DFS(startx, starty, stopx, stopy, graph):
    stack = [(startx, starty)]
    visited = {(startx, starty)} #посещённые координаты
    paths = {(startx, starty):[]} #хранение путей от стартовой позиции до каждой посещенной координаты
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

#Функция А* 
def A(start_x, start_y, exit_x, exit_y, maze, g_weight=1, h_weight=1, max_steps=10000):
    # определяем эвристическую функцию
    def heuristic(x, y, exit_x, exit_y):
        return h_weight * (abs(x - exit_x) + abs(y - exit_y))

    # определяем начальные значения
    open_set = {(start_x, start_y)}#позиции которые нужно пройти
    closed_set = set()#пройденные позиции
    g_st = {(start_x, start_y): 0}#хранение значений пути от стратовой позиции до каждой
    f_st = {(start_x, start_y): heuristic(start_x, start_y, exit_x, exit_y)}#хранение значений функции оценки f для каждой позиции
    came_from = dict()#хранение информации о пути от стартовой позиции до каждой позиции

    # находим путь
    for i in range(max_steps):
        #получаем ячейку с наименьшим f_st cell
        curr_x, curr_y = min(open_set, key=lambda cell: f_st[cell])
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
            nx = curr_x + dx
            ny = curr_y + dy
            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == ' ':
                tent_g_st = g_st[(curr_x, curr_y)] + 1
                if tent_g_st < g_st.get((nx, ny), float('inf')):
                    came_from[(nx, ny)] = (curr_x, curr_y)
                    g_st[(nx, ny)] = tent_g_st
                    f_st[(nx, ny)] = tent_g_st * g_weight + heuristic(nx, ny, exit_x, exit_y) * h_weight
                    if (nx, ny) not in open_set:
                        open_set.add((nx, ny))
    #путь не найден
    return [], False


maze = load_maze("maze-for-u.txt")
start_x, start_y = coord(maze)
key_x, key_y = coord(maze)

path_to_key, success = DFS(start_x, start_y, key_x, key_y, maze)
if not success:
    print('Путь не найден')
else:
    print('Путь до ключа:', path_to_key)

path_to_exit, success = A(key_x, key_y, len(maze) - 1, len(maze[0]) - 2, maze, g_weight=1, h_weight=2, max_steps=100000)
if not success:
    print('Не удалось найти путь к выходу')
else:
    print('Путь к выходу:', path_to_exit)

#сохранение лабиринта с указанием пути к ключу и выхода из него
maze_with_path = maze.copy()
maze_with_path[key_x][key_y] = '*'

if path_to_key and path_to_exit:
    for x, y in path_to_key:
        maze_with_path[x][y] = '.'
    for x, y in path_to_exit:
        maze_with_path[x][y] = ','
    maze_with_path[len(maze) - 1][len(maze[0]) - 2] = 'B'#обозначение выхода

#Запись в файл
with codecs.open('maze-for-me-done.txt', 'w', 'utf_8_sig') as k:
    for line in maze_with_path:
        k.write(''.join(line) + '\n')






















