import random
from heapq import heappop, heappush

def read_maze(filename):
    maze = []
    
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip()
            maze.append(list(row))
    height = len(maze)
    width = len(maze[0])
    return maze,height,width


maze,height,width = read_maze('maze-for-u.txt')


start_coord = (1,0)
exit_coord = (width-2,height-1)



def get_key():
    upper_limit = 100
    counter =0
    while counter < upper_limit+1:  
        counter +=1
        x= random.randint(1,width-1)
        y= random.randint(1,height-1)
        key=(x,y)
        if key != "#":
            maze[x][y] = '*'
            return key 
        if counter >= upper_limit:
            print("insert key position -> ")
            print("x = ")
            x=int(input())
            print("y = ")
            y=int(input())
            key=(x,y)
            maze[x][y] = '*'
            return key 

key = get_key()
#print("Координаты ключа: ", key)


def dfsSearch(maze, start_coord, goal):
    visited = set()
    path = []
    def dfs(current):
        if current == goal:
            return True
        visited.add(current)
        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != "#" and neighbor not in visited):
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                path.pop()
        return False
    if dfs(start_coord):
        return path
    else:
        return 0
    
def aSearch(maze, start_coord, goal, max_steps):
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue = [(heuristic(start_coord, goal), 0, start_coord, [])]
    visited = set()

    while queue:
        _, cost, current, path = heappop(queue)
        if current == goal:
            return path + [current]

        visited.add(current)

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != "#" and neighbor not in visited):
                new_cost = cost + 1
                priority = new_cost + heuristic(neighbor, goal) 
                if priority <= max_steps:
                    heappush(queue, (priority, new_cost, neighbor, path + [current]))
    return 0



print("2 task(поиск в глубину):")
d = dfsSearch(maze, start_coord, key)
print("Длина пути:", len(d))
print(d)



print("3 task (A*):")
a = aSearch(maze, key, end, 10000)
print("Длина пути:", len(a))
print(a)
    
def markPath(maze, path, marker):
    markedMaze = [row.copy() for row in maze]
    for position in path:
        row, col = position
        markedMaze[row][col] = marker
    return markedMaze

#4 task

LastOnefile = "maze-for-me-done.txt"
with open(LastOnefile, "w") as file:
    for row in markPath(maze, d, "."):
        file.write("".join(row) + "\n")
    for row in markPath(maze, a, ","):
        file.write("".join(row) + "\n")

