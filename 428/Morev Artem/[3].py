from random import shuffle
import math as mt
import numpy as np
import tkinter
import time
from collections import deque
from numpy import copy
import random

def read_file(): 
    fin = open("maze-for-u.txt",'r')
    maze = fin.readlines()
    height = len(maze)
    width = len(maze[0])
    return maze, height, width



def check_init_coord(x, y, maze=read_file()[0]):
    if maze[x][y] != '#':
        return True


def init_values(max_x, max_y):
    while True:
        x = int(input(f"Координата аватара, x < {max_x}:"))
        y = int(input(f"Координата аватара, y < {max_y}: "))
        if check_init_coord(x, y):
            break
        print("Начальные координаты находятся на стене или вне лабиринта!")

    while True:
        x_e = int(input(f"Координата выхода, x < {max_x}: "))
        y_e = int(input(f"Координата выхода, y < {max_y}: "))
        if check_init_coord(x_e, y_e):
            break
        print("Координаты выхода находятся на стене или вне лабиринта!")
        
    return (x, y), (x_e, y_e)

maze, height, width = read_file()#лабиринт,высота,ширина
start_coord, exit_coord = init_values(width, height)#начальная и конечная координата


# Эта функция используется для проверки, находится ли текущая позиция start_coord в лабиринте на выходе exit_coord.
def is_exit(start_coord, exit_coord):
    return start_coord[0] == exit_coord[0] and start_coord[1] == exit_coord[1]

def poisk_shirina(maze,start_coord,exit_coord):
    INF = 10 ** 9
    
    height = len(maze)
    width = len(maze[0])
    #Заполнили массив расстояний до координат максимальными значениями(бесконечностью)
    long_coord = [[INF]*height for _ in range(width)]
    #Проверка были ли мы в данной точке 
    check_coord = [[False]*height for _ in range(width)]
    queue = deque()
    #Записали что до стартовой точки расстояние 0
    long_coord[start_coord[0]][start_coord[1]] = 0
    #Записали что стартовую точку посетили
    check_coord[start_coord[0]][start_coord[1]] = True
    queue.append(start_coord)
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    
    P = [[None]*height for _ in range(width)]
    
    while len(queue) != 0:
        x,y = queue.popleft()
        for dx , dy in delta:
            nx , ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and not check_coord[nx][ny] and maze[nx][ny] != '#':
                          long_coord[nx][ny] = long_coord[x][y] + 1
                          P[nx][ny] = (x,y)
                          check_coord[nx][ny] = True
                          queue.append((nx,ny))
    print(long_coord[exit_coord[0]][exit_coord[1]])
  
    cur = exit_coord
    path = []
    
    while cur is not None:
        path.append(cur)
        cur = P[cur[0]][cur[1]]
    path.reverse()
    return path

poisk_shirina(maze, start_coord, exit_coord)          
path = poisk_shirina(maze, start_coord, exit_coord)   
def draw_visited_coords(path, maze, filename):
    # Создаем копию лабиринта, чтобы не менять оригинальный
    print(path)
    maze_copy = [list(row) for row in maze]
    # Проходим по всем посещенным координатам и отмечаем их в лабиринте
    for x, y in path:
        maze_copy[x][y] = '.'
    # Открываем файл для записи
    with open(filename, 'w') as f:
        # Записываем измененный лабиринт в файл
        for row in maze_copy:
            f.write(''.join(row))
            f.write('n')

draw_visited_coords(path, maze, 'visited.txt')

#Алгоритм А*------------------------------------------------------------------------------

def get_neighbours(position, maze):
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Верх, низ, лево, право
    for direction in directions:
        x = position[0] + direction[0]
        y = position[1] + direction[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '#':
            neighbours.append((x, y))
    return neighbours

def find_exit_position(maze):
    possible_exits = []
    for i in range(len(maze)):
        if maze[i][0] != '#':
            possible_exits.append((i, 0))
        if maze[i][-1] != '#':
            possible_exits.append((i, len(maze[i]) - 1))
    for j in range(len(maze[0])):
        if maze[0][j] != '#':
            possible_exits.append((0, j))
        if maze[-1][j] != '#':
            possible_exits.append((len(maze) - 1, j))
    return random.choice(possible_exits)



def calculate_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def draw_coords(maze, filename):
    # Создаем копию лабиринта, чтобы не менять оригинальный
    maze_copy = [list(row) for row in maze]
    # Проходим по всем посещенным координатам и отмечаем их в лабиринте
    for position in a_star_path:
           maze_copy[position[0]][position[1]] = ','
    # Открываем файл для записи
    with open(filename, 'w') as f:
        # Записываем измененный лабиринт в файл
        for row in maze_copy:
            f.write(''.join(row))
            f.write('n')


def a_star_search(maze, start, goal, max_steps):
    open_list = [(start, 0, calculate_distance(start, goal))]
    closed_list = set()
    parent = {}
    g_scores = {start: 0}

    while open_list:
        current, g_score, f_score = min(open_list, key=lambda x: x[2])
        open_list.remove((current, g_score, f_score))
        closed_list.add(current)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        if len(closed_list) > max_steps:
            return None

        neighbours = get_neighbours(current, maze)
        for neighbour in neighbours:
            if neighbour in closed_list:
                continue

            tentative_g_score = g_score + 1
            if neighbour not in g_scores or tentative_g_score < g_scores[neighbour]:
                g_scores[neighbour] = tentative_g_score
                f_score = tentative_g_score + calculate_distance(neighbour, goal)
                open_list.append((neighbour, tentative_g_score, f_score))
                parent[neighbour] = current

    return None

exit_position = find_exit_position(maze)

# Находим оптимальный путь до выхода с помощью A*
a_star_path = a_star_search(maze, start_coord, exit_position, len(maze) * len(maze[0]))

if a_star_path is not None:
        draw_coords(maze,'A*ppp')
        print("Маршрут успешно найден и сохранен в файле 'maze-for-me-done.txt'.")
else:
        print("Невозможно найти маршрут до выхода.")




















