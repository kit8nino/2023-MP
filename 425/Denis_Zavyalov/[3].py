import numpy as np
from collections import deque

maze = []
with open("maze-for-u.txt") as file:
    for item in file:
        maze.append(item[:800])

graph = {}

for i in range(600):
    for j in range(800):
        if maze[i][j] != "#":
            a = []
            if (i - 1 >= 0) and (maze[i - 1][j] != "#"):
                a.append((i - 1, j))

            if (j - 1 >= 0) and (maze[i][j - 1] != "#"):
                a.append((i, j - 1))

            if (i + 1 < 600) and (maze[i + 1][j] != "#"):
                a.append((i + 1, j))
            if (j + 1 < 800) and (maze[i][j + 1] != "#"):
                a.append((i, j + 1))

            graph[(i, j)] = a

start = (0, 1)
end = (599, 798)


def bfs(start, end, graph):
    queue = deque([start])
    visited = {start: None}
    while queue:
        next_node = queue.popleft()
        if next_node == end:
            break
        adjacent_nodes = graph[next_node]
        for adjacent_node in adjacent_nodes:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
                visited[adjacent_node] = next_node
    return visited


visited = bfs(start, end, graph)

next_node = end
while next_node != start:
    next_node = visited[next_node]
    new_text = maze[next_node[0]][:next_node[1]] + "," + maze[next_node[0]][next_node[1] + 1:]
    maze[next_node[0]] = new_text
#    print(f'---> {next_node} ', end='')


with open("'maze-for-me-done.txt", "w") as file:
    for i in range(600):
        file.write(maze[i] + '\n')
