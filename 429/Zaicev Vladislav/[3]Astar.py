import numpy as np
with open("maze-for-u.txt","r") as file:
    maze = []
    for line in file:
        stroka = []
        for i in line.strip():
            stroka.append(i)
        maze.append(stroka)

key = (350,360)
key1 = key[0]
key2 = key[1]

StartPoint = (0,1)
FinishPoint = [len(maze)-1 , len(maze[0])-2]




def GetCoord_tuple(point):
    y = point[1]
    x = point[0]
    return (x,y)

def GetCoord(point):
    y = point[1]
    x = point[0]
    return x,y


def manhattan_distance(StartPoint, FinishPoint):
    x1,y1 = GetCoord(StartPoint)
    x2,y2 = GetCoord(FinishPoint)
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(StartPoint, FinishPoint):
    not_visited = {StartPoint}
    
    visited = []
    
    g_score = {GetCoord_tuple(StartPoint): 0}
    f_score = {(GetCoord_tuple(StartPoint)): manhattan_distance(StartPoint, FinishPoint)}
    
    came_from = {}

    while len(not_visited) != 0 :
        x, y = min(not_visited, key=lambda cell: f_score[cell])
        StatPoint = [x,y]
        if StatPoint == FinishPoint:
            path = [(x, y)]
            while (x, y) in came_from:
                x, y = came_from[x, y]
                path.append((x, y))
            path.reverse()
            return path

        not_visited.remove((x, y))
        visited.append([x, y])

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = x + dx
            new_y = y + dy
            new_point = [new_x,new_y]
            if new_x >= 0 and new_x < len(maze) and new_y >= 0 and new_y < len(maze[0]) and maze[new_x][new_y] != '#':
                distance = g_score[(x, y)] + 1
                if distance < g_score.get((new_x, new_y), 9999):
                    came_from[(new_x, new_y)] = (x, y)
                    g_score[(new_x, new_y)] = distance
                    f_score[(new_x, new_y)] = distance + manhattan_distance(new_point, FinishPoint)
                    if (new_x, new_y) not in not_visited:
                        not_visited.add((new_x, new_y))

    return []


path = a_star(key, FinishPoint)


maze[key1][key2] = '*'

if path:
    for x, y in path:
        maze[x][y] = ','
    x,y = GetCoord(FinishPoint)
    maze[x][y] = ','

maze_str = ''
for row in maze:
    maze_str += ''.join(row) + '\n'

with open('maze.txt', 'w') as f:
    f.write(maze_str)