import numpy as np

with open("maze-for-u.txt","r") as file:
    maze = []
    for line in file:
        stroka = []
        for i in line.strip():
            stroka.append(i)
        maze.append(stroka)
        
n = len(maze) - 1
m = len(maze[0]) - 1       


# Входные данные

StartPoint = [0,1]
KeyPoint = [395,400]
FinishPoint = [len(maze),len(maze[0])-1]
distance = np.zeros([len(maze),len(maze[0])])
stack = []
visited = np.zeros([n+1,m+1])

def DoVisited(point):
    #visited.append(point)
    y,x = GetCoord(point)
    visited[y][x] = 1
    
def isVisited(point):
    for i in visited:
        if i == point:
            return True
    return False

def ChangeDistance(new_point,point_value):
    y = new_point[0]
    x = new_point[1]
    
    distance[y][x] = point_value + 1
        
def GetCoord(point):
    y = point[0]
    x = point[1]
    return y,x

def WriteToStack(point):
    stack.append(point)
    
def DeleteFromStack(point):
    stack.pop(0)
    
    
def do_look(point):
    y = point[0]
    x = point[1]
    point_value = distance[y][x]
    
    
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        y_new, x_new = y + dy, x + dx
        if maze[y_new][x_new] != "#" and visited[y_new][x_new] != 1 and y_new >= 0 and y_new < len(maze):
            new_point = [y_new, x_new]
            DoVisited(new_point)
            WriteToStack(new_point)
            ChangeDistance(new_point, point_value)
    
def is_exit(point,FinishPoint):
    if point == FinishPoint:
        return True 
    else:
        return False
     
def BFS(StartPoint,FinishPoint):  
    stack.append(StartPoint)     
    while len(stack) != 0:
        point = stack[0]
        
        if is_exit(point,FinishPoint):
            break
        
        DoVisited(point)
        do_look(point)
        DeleteFromStack(point)
  
def DoPath(FinishPoint):
# Прокладываем путь до Финиша
    StatPoint = FinishPoint
    y,x = GetCoord(StatPoint)
    
    y1,x1 = GetCoord(StartPoint)
    distance[y1][x1] = -1  
    
    while StatPoint != StartPoint:
        y,x = GetCoord(StatPoint)
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            y_new, x_new = y + dy, x + dx

            if distance[y_new][x_new] != 0 and distance[y_new][x_new] < distance[y][x]:
                maze[y_new][x_new] = "."
                StatPoint = [y_new, x_new]
                break

BFS(StartPoint,KeyPoint)
DoPath(KeyPoint)

y,x = GetCoord(KeyPoint)
maze[y][x] = "*"

maze_str = ''
for row in maze:
    maze_str += ''.join(row) + '\n'
        
with open('maze.txt', 'w') as f:
    f.write(maze_str)   
    

    
    
    
    
    
    
