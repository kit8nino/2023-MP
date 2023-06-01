#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


from collections import deque
import random

def place(maze_file):
    with open(maze_file, 'r+') as file:
        maze = [list(line.strip()) for line in file]

        empty_cells = [(i, j) for i, row in enumerate(maze) for j, cell in enumerate(row) if cell == ' ']

        if not empty_cells:
            return False

        key_pos = random.choice(empty_cells)
        maze[key_pos[0]][key_pos[1]] = '*'

        file.seek(0)
        file.writelines([''.join(row) + '\n' for row in maze])
        file.truncate()

        return True

def find(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == '*':
                return i, j
    return None

def read_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze


def breadth_first_search(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [])])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

    while queue:
        current, path = queue.popleft()
        row, col = current

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for direction in directions:
                n_row = row + direction[0]
                n_col = col + direction[1]

                if 0 <= n_row < rows and 0 <= n_col < cols and maze[n_row][n_col] == ' ' and (n_row, n_col) not in visited:
                    queue.append(((n_row, n_col), path + [current]))

    return None

maze_file = "maze.txt"  

place(maze_file)

maze = read_maze(maze_file)

start = (5, 8) 
end = (19, 18) 

print("Координаты входа и выхода: ", start, end)

key = find(maze)
print("Координаты ключа: ", key)

breadth_first_path_start_to_key = breadth_first_search(maze, start, key)

if breadth_first_path_start_to_key:
    print("Кратчайший путь от входа до ключа (поиск в ширину):")
    print("Длина пути:", len(breadth_first_path_start_to_key))
else:
    print("Путь от входа до ключа не найден (поиск в ширину).")


# In[ ]:




