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

# Расположение ключа :  [350,360] 

key = [350,360]
key1 = key[0]
key2 = key[1]


def obhod(start,finish,maze,simvol):        

    
    karta = np.zeros([n+1,m+1])
    visited = np.zeros([n+1,m+1])
    
    # Начальные условия
    #start = [0,1]
    #finish = [n,m-1]
    #start = [0,1]
   # finish = [n,m-1]
    maze[finish[0]][finish[1]] = "F"
    stack = [start]
    
    
    visited[start[0],start[1]] = 1
    karta[start[0],start[1]] = 0
    
    path = []
    
    while len(stack) != 0 :
        first = stack[0]
        if first == finish:
            break
        y = first[0]
        x = first[1]
        visited[y][x] = 1
        
        left = None
        right = None
        down = None
        up = None
        
        if maze[y][x-1] != "#" and visited[y][x-1] != 1 :
            left = [y,x-1]
            karta[y][x-1] = karta[y][x] + 1 
            visited[y][x-1] = 1
            path.append([y,x-1])
        
            
            
        if maze[y][x+1] != "#" and visited[y][x+1] != 1:
            right = [y,x+1]
            karta[y][x+1] = karta[y][x] + 1
            visited[y][x+1] = 1
            path.append([y,x+1])
            
          
        if maze[y+1][x] != "#" and visited[y+1][x] != 1 :
            
            down = [y+1,x]
            karta[y+1][x] = karta[y][x] + 1
            visited[y+1][x] = 1
            path.append([y+1,x])
            
            
        if maze[y-1][x] != "#" and visited[y-1][x] != 1:
            up = [y-1,x]
            karta[y-1][x] = karta[y][x] + 1
            visited[y-1][x] = 1
            path.append([y-1,x])
            
            
        stack.pop(0)
        a = [left,right,down,up]
        
        for i in a:
            if i is not None:
                stack.append(i)
                
                
    karta[start[0],start[1]] = -1            
    new_path = []
    freeze = finish
    y = freeze[0]
    x = freeze[1]
    
    while freeze != start:
        y = freeze[0]
        x = freeze[1]
        new_path.append(freeze)
        if karta[y,x+1] < karta[y][x] and karta[y,x+1] != 0 :
            freeze = [y,x+1]
            continue
        if karta[y,x-1] < karta[y][x] and karta[y,x-1] != 0:
            freeze = [y,x-1]
            continue
        if karta[y-1,x] < karta[y][x] and karta[y-1,x] != 0:
            freeze = [y-1,x]
            continue
        if karta[y+1,x] < karta[y][x] and karta[y+1,x] != 0:
            freeze = [y+1,x] 
            continue
    maze[start[0]][start[1]] = simvol        
    for y,x in new_path:
        maze[y][x] = simvol
    return maze

maze = obhod([0,1],key,maze,".")
      
maze = obhod(key,[n,m-1],maze,",")
maze[key1][key2] = "*"  
    
maze_str = ''
for row in maze:
    maze_str += ''.join(row) + '\n'
        
with open('maze.txt', 'w') as f:
    f.write(maze_str)   
        
    
        