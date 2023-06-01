import numpy as np
with open("maze-for-u.txt","r") as file:
    maze = []
    for line in file:
        stroka = []
        for i in line.strip():
            stroka.append(i)
        maze.append(stroka)

key = [350,360]
key1 = key[0]
key2 = key[1]

StartPoint = [0,1]
finish_x, finish_y = len(maze) - 1, len(maze[0]) - 2




def GetCoord(point):
    y = point[1]
    x = point[0]
    return x,y


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(start_x, start_y, exit_x, exit_y, maze, g=1, h=1, max_steps=10000):
    open_set = {(start_x, start_y)}
    closed_set = set()
    g_score = {(start_x, start_y): 0}
    f_score = {(start_x, start_y): manhattan_distance(start_x, start_y, exit_x, exit_y)}
    came_from = dict()

    for i in range(max_steps):
        curr_x, curr_y = min(open_set, key=lambda cell: f_score[cell])
        if curr_x == exit_x and curr_y == exit_y:
            path = [(curr_x, curr_y)]
            while (curr_x, curr_y) in came_from:
                curr_x, curr_y = came_from[(curr_x, curr_y)]
                path.append((curr_x, curr_y))
            path.reverse()
            return path

        open_set.remove((curr_x, curr_y))
        closed_set.add((curr_x, curr_y))

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = curr_x + dx
            ny = curr_y + dy
            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == ' ':
                tent_g_score = g_score[(curr_x, curr_y)] + 1
                if tent_g_score < g_score.get((nx, ny), float('inf')):
                    came_from[(nx, ny)] = (curr_x, curr_y)
                    g_score[(nx, ny)] = tent_g_score
                    f_score[(nx, ny)] = tent_g_score * g + manhattan_distance(nx, ny, exit_x, exit_y) * h
                    if (nx, ny) not in open_set:
                        open_set.add((nx, ny))

    return []


path_to_exit = a_star(key1, key2, finish_x, finish_y, maze, g=1, h=1, max_steps=100000)


maze_with_path = [row.copy() for row in maze]
maze_with_path[key1][key2] = '*'

if path_to_exit:
    for x, y in path_to_exit:
        maze_with_path[x][y] = ','
    maze_with_path[finish_x][finish_y] = ','

maze_str = ''
for row in maze_with_path:
    maze_str += ''.join(row) + '\n'

with open('maze.txt', 'w') as f:
    f.write(maze_str)