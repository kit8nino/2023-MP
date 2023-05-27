# [3] Алгоритмы поиска пути и структурное программирование
import numpy as np
from queue import PriorityQueue

#так как у меня др 9 августа, будем использовать метод поиска в глубину
def maze_to_array(file_name):
    with open(file_name, 'r') as f:
        maze = [i.rstrip() for i in f]
    for i in range(len(maze)):
        maze[i]=list(maze[i])
    return maze

def maze_to_file(path, file_name):
    with open(file_name, 'w') as f:   
        for i in maze_resh:
            for j in i:
                f.write(f"{j}")
            f.write(f"\n")

def data(maze):
    print(f"границы по столбцу [0,{len(maze[0])}], по строке [0,{len(maze[:])}]")
    x_a = int(input("координаты аватара по столбцу:  ")) -1
    y_a = int(input("координаты аватара по строке: ")) -1
    x_k = int(input("координаты ключа по столбцу: ")) -1
    y_k = int(input("координаты ключа по строке: ")) -1
    maze[y_a][x_a] = 'A' #взял наоборот, тк в блокноте неправильная СО
    maze[y_k][x_k] = '*'
    start = (y_a, x_a)
    key = (y_k, x_k)
    return start, key

def make_step(maze, lv, v, q): 
    coord = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ] 
    for x_step, y_step in coord:
        x, y = lv[0] + x_step, lv[1] + y_step 
        if 0 < x < len(maze) and 0 < y < len(maze[0]): 
            if v.get((x, y)) == None and maze[x][y] != '#':                                                             
                v[(x, y)] = (lv) 
                q.append((x, y))
    return q , v

def maze_way(maze, path, sign):
    way = np.copy(maze) 
    for i in path:
        if way[i[0],i[1]] != '*' and way[i[0],i[1]] != 'A':
            way[i[0],i[1]] = sign
    return way

def ro(end, c):
    return abs(end[0] - c[0]) + abs(end[1] - c[1])

# метод поиска в глубину
def search_vglubinu(maze, start, end):
    v = {} 
    v[start] = start
    q = [] 
    q.append(start)
    while len(q) != 0: 
        lv = q.pop() 
        step = make_step(maze, lv, v, q)
        q = step[0]
        v = step[1]
    path = reverse_path(v, start, end)
    return path

def reverse_path(v, start, end): 
    c, path = end, []
    while c != start:
        path.append(c)
        c = v[c]
    path.append(start)
    path.reverse()
    return path

def get_neighbors(maze, pos):
    row, col = pos
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])]

#метод поиска A*
def search_a(maze, start, end, max_cost):
    pq = PriorityQueue()
    pq.put(start, 0)
    c = {}
    cost = {}
    c[start] = None
    cost[start] = 0
    while not pq.empty():
        i = pq.get()
        if i == end:
            break
        for n in get_neighbors(maze, i):
            new_cost = cost[i] + 1
            if 0 <= n[0] < len(maze) and 0 <= n[1] < len(maze[0]) and maze[n[0]][n[1]] != '#' and (n not in cost or new_cost < cost[n]) and new_cost <= max_cost:
                cost[n] = new_cost
                p = new_cost + ro(end, n)
                pq.put(n, p)
                c[n] = i
    path = reverse_path(c, start, end)
    return path

maze = maze_to_array("maze-for-u.txt")
start, key = data(maze)
end_1 = (1,1)
end_2 = (len(maze[:])-2, len(maze[0])-2)
if ro(key, end_1) < ro(key, end_2):
    end = end_1
    print("\nближний выход - верхний")
else:
    end = end_2
    print("\nближний выход - нижний")

path_to_key = search_vglubinu(maze, start, key)
path_to_end = search_a(maze, key, end, 100000)

print("длина от аватара до ключа =", len(path_to_key)-1, "методом поиска в глубину")
print("длина от ключа до выхода =", len(path_to_end)-1, "методом A*")
print("длина от аватара до выхода =", len(path_to_key)+len(path_to_end)-1)

maze_resh = maze_way(maze, path_to_key , '.')
maze_resh = maze_way(maze_resh, path_to_end , ',')
maze_to_file(maze_resh, "maze-for-me-done.txt")
print("файл создан под названием 'maze-for-me-done.txt'")
print("'A'-аватар,'*'-ключ,'.'-путь от 'A' до  '*',','-путь от '*' до  выхода")
'''
границы по столбцу [0,800], по строке [0,600]
координаты аватара по столбцу:  790
координаты аватара по строке: 10
координаты ключа по столбцу: 10
координаты ключа по строке: 590

ближний выход - верхний
длина от аватара до ключа = 1442 методом поиска в глубину
длина от ключа до выхода = 2174 методом A*
длина от аватара до выхода = 3617
файл создан под названием 'maze-for-me-done.txt'
'A'-аватар,'*'-ключ,'.'-путь от 'A' до  '*',','-путь от '*' до  выхода
'''
