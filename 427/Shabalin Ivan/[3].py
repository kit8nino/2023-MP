#!/usr/bin/env python
# coding: utf-8

# In[59]:


from random import shuffle
import numpy as np
from random import randint
import heapq
from collections import deque

wall, path, visited = 1, 0, 3
a, b = 1, 1
max_path_length = 1000

def read_maze(file_name='maze-for-u.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height = len(maze_raw)
    width = len(maze_raw[0])
    return [wall if x[i] == '#' else path for x in maze_raw
            for i in range(width)], width, height


def check_init_coord(x, y, maze=read_maze()[0]):
    return True


def init_values(max_x, max_y):
    x = int(input(f"Avatar coord, x < {max_x}: "))
    y = int(input(f"Avatar coord, y < {max_y}: "))
    check_init_coord(x, y)
    x_e = int(input(f"Exit coord, x < {max_x}: "))
    y_e = int(input(f"Exit coord, y < {max_y}: "))
    check_init_coord(x_e, y_e)
    return (x, y), (x_e, y_e)



maze, width, height = read_maze()
start_coord, exit_coord = init_values(width, height)

mazepov=np.zeros((600,800))
k=0
for j in range(600):
    for i in range(800):
        mazepov[j][i]=maze[k]
        k+=1
#Задаём координаты ключа     
x_k=randint(0, 800)
y_k=randint(0, 600)
if mazepov[y_k][x_k]!=1:
        mazepov[y_k][x_k]=3 
        


def get_neighbors(maze, curr):
    # Функция, которая возвращает список соседей текущей вершины
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = curr[0] + dx, curr[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
            neighbors.append((x, y))
    return neighbors
def bfs(maze, start, key):
    # Инициализируем очередь для поиска в ширину
    queue = deque([start])
    # Инициализируем словарь, который будет хранить дерево пути
    tree = {start: None}
    path=[]
    while queue:
        # Извлекаем следующую вершину из очереди
        curr = queue.popleft()
        
        if curr == key:
            # Если мы нашли ключ, то возвращаем дерево пути
            while curr != start:
                    path.append(curr)
                    maze[curr[1]][curr[0]]=5
                    curr = tree[curr]
            maze[start[1]][start[0]]=5        
            path.append(start)
            path.reverse()
            return path
        
        # Для каждого соседа текущей вершины
        for neighbor in get_neighbors(maze, curr):
            if neighbor not in tree:
                # Если сосед еще не был посещен, то добавляем его в дерево и в очередь
                tree[neighbor] = curr
                queue.append(neighbor)
    
    # Если ключ не был найден, то возвращаем None
    return None

def heuristic(a, b):
    # Манхэттенское расстояние между точками a и b
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(maze, start, end):
    
    def search_end(start):
        
    
    
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, end)}
    oheap = []
    
    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == end:
            data = []
            while current in came_from:
                data.append(current)
                maze[current[1]][current[0]]=5
                current = came_from[current]
             
            data.append(start)
            return data[::-1]
        
        close_set.add(current)
        for neighbor in get_neighbors(maze, current):
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
                    
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    
    return None
# Находим стартовую точку и ключ
start = start_coord
key= (x_k, y_k)
end= exit_coord
print(key)
print(type(key))
  # Ищем путь от стартовой точки до ключа
path = bfs(mazepov, start, key)

# Выводим дерево пути в виде связного списка
print(mazepov)
print(path)
#key=(1, 0)
end= exit_coord
path1 = astar(mazepov, key, end)
print(path1)
curr = key


print(mazepov) 
#Возвращаем 'maze-for-me-done.txt'
f = open('maze-for-me-done.txt', 'w')
for i in range(len(mazepov)):
    for j in range(len(mazepov[0])):
        if mazepov[i][j] == 1:
            f.write('#')
        elif  mazepov[i][j] == 5:
            f.write(',')
        elif mazepov[i][j] == 3:
            f.write('*')
        else:
            f.write(' ')
    f.write('\n')
f.close()  


# Так как я сгенерировал лаберинт с одинм только входом и выходом (до нижнего входа не дойти, тк где-то стоит стена, а смотреть ,где она тяжело, мной было принято решение не искать ближайший выход, а задавать его в ручную. Лаберинт менять не хочу, тк к этому уже прикипел.

# In[ ]:




