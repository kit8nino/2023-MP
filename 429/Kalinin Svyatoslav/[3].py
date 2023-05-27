import heapq
import random

maze_filename = 'maze-for-u.txt'
maze = []

with open(maze_filename, 'r') as file:
    for line in file:
        maze.append(line.strip())
maze_height = len(maze)
maze_width = len(maze[0])

#reading maze from file "maze.txt" 
#file should be in same directory as .py file
with open(maze_filename, 'r') as f:
    lines = f.readlines()

width = max(len(line) for line in lines)-1 # считывает пробел после границы

height = len(lines)

walls_f = []

for j in range(height):
    for i in range(width):
        if lines[j][i] == '#':
            walls_f.append((i, j))


def get_key(walls_f, width, height):
    upper_limit = 100
    counter =0
    while counter < upper_limit+1:  
        counter +=1
        x= random.randint(1,width-1)
        y= random.randint(1,height-1)
        k=(x,y)
        if k not in walls_f:
            return k
        if counter >= upper_limit:
            print("insert key position -> ")
            print("x = ")
            x=int(input())
            print("y = ")
            y=int(input())
            k=(x,y)
            return k

def write_path(height,width,start_coordinates,key_coordinates,exit_coordinates ,walls,maze_filename):
    print("start processing output file -> ", maze_filename)
    counter = 0
    with open(maze_filename, 'w') as f:
        for i in range(height):
            counter+=1
            if counter %10 ==0:
                print("created line ->", counter)
            for j in range(width):
                point =(j,i)
                if point in walls:
                   f.write('#')                 
                elif point == key_coordinates:                    
                    f.write('*')
                else:
                    f.write(' ')
            f.write('\n')

start_coordinates = (1,0)
key_coordinates = get_key(walls_f, width, height)
exit_coordinates = (19,17)
write_path(maze_height,maze_width,start_coordinates,key_coordinates,exit_coordinates ,walls_f,maze_filename)
print(key_coordinates)

# Проверка наличия всех необходимых элементов в лабиринте
assert start_coordinates is not None, 'Не найден аватар'
assert key_coordinates is not None, 'Не найден ключ от выхода'
assert exit_coordinates is not None, 'Не найден выход'

def find_path_to_key(maze, start_coordinates, key_coordinates):
    x, y = start_coordinates
    while (x, y) != key_coordinates:
        min_dist = float('inf')
        next_x, next_y = x, y
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == ' ':
                dist = (new_x - key_coordinates[0]) ** 2 + (new_y - key_coordinates[1]) ** 2
                if dist < min_dist:
                    min_dist = dist
                    next_x, next_y = new_x, new_y
        # перемещение аватара в новую ячейку
        maze[x] = maze[x][:y] + ' ' + maze[x][y+1:]
        maze[next_x] = maze[next_x][:next_y] + 'A' + maze[next_x][next_y+1:]
        x, y = next_x, next_y
    return maze

# Построение списка соседей для конкретной точки в лабиринте
def get_neighbors(maze, coordinates):
    x, y = coordinates
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == ' ':
            neighbors.append((new_x, new_y))
    return neighbors

# Расчет эвристического расстояния от конкретной точки до выхода
def heuristic(point, exit_coordinates):
    return ((point[0] - exit_coordinates[0]) ** 2 + (point[1] - exit_coordinates[1]) ** 2) ** 0.5

def find_optimal_path(maze, start_coordinates, exit_coordinates):
    heap = [(0, start_coordinates)]
    came_from = {start_coordinates: None}
    cost_so_far = {start_coordinates: 0}
    while heap:
        current = heapq.heappop(heap)[1]
        if current == exit_coordinates:
            break
        for neighbor in get_neighbors(maze, current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, exit_coordinates)
                heapq.heappush(heap, (priority, neighbor))
                came_from[neighbor] = current
                
    # Составление оптимального пути из точки А в точку B
    path = []
    current = exit_coordinates
    while current != start_coordinates:
        path.append(current)
        current = came_from[current]
    path.append(start_coordinates)
    path.reverse()
    
    # Замена точек пути на символы и сохранение результата в файл
    for point in path[:-1]:
        maze[point[0]] = maze[point[0]][:point[1]] + '.' + maze[point[0]][point[1]+1:]
    maze[key_coordinates[0]] = maze[key_coordinates[0]][:key_coordinates[1]] + '*' + maze[key_coordinates[0]][key_coordinates[1]+1:]
    with open('maze-for-me-done.txt', 'w') as file:
        for line in maze:
            file.write(line + '\n')

    return maze

# Выполнение поиска пути до ключа и до выхода и сохранение результата в файл
maze = find_path_to_key(maze, start_coordinates, key_coordinates)
find_optimal_path(maze, key_coordinates, exit_coordinates)