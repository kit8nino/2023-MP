import numpy as np
wall=1
free=0
path=2
visited = -1


def Read_File(file_name = 'maze-for-u.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height =len(maze_raw)
    length =len(maze_raw[0])
    maze = np.array([])
    maze = np.append(maze,[wall if x[i]=='#' else free for x in maze_raw for i in range(length)])
    maze = np.reshape(maze,(height,length))   
    return maze,height,length

def Next_Step(cord,maze):
    if maze[cord[0]+1][cord[1]] == 0:
        cord[0]=cord[0]+1
        maze[cord[0]][cord[1]] = path
        
    elif maze[cord[0]][cord[1]+1] == 0:
        cord[1]=cord[1]+1
        maze[cord[0]][cord[1]] = path
        
    elif maze[cord[0]][cord[1]-1] == 0:
        cord[1]=cord[1]-1
        maze[cord[0]][cord[1]] = path
        
    elif maze[cord[0]-1][cord[1]] == 0:    
        cord[0]=cord[0]-1
        maze[cord[0]][cord[1]] = path
        
    else: Backtrack(cord,maze)
    
    return(cord)

def Backtrack(cord,maze):
    if maze[cord[0]-1][cord[1]] == 2:            
        maze[cord[0]][cord[1]] = visited
        cord[0]=cord[0]-1
        
    elif maze[cord[0]][cord[1]-1] == 2:    
        maze[cord[0]][cord[1]] = visited
        cord[1]=cord[1]-1
        
    elif maze[cord[0]][cord[1]+1] == 2:    
        maze[cord[0]][cord[1]] = visited
        cord[1]=cord[1]+1
    
    elif maze[cord[0]+1][cord[1]] == 2:    
        maze[cord[0]][cord[1]] = visited
        cord[0]=cord[0]+1
            

maze,height,length = Read_File()
finish_x,finish_y = length-2,height-1
start_x,start_y = 1,0
cord = [start_y,start_x]
maze[cord[0]][cord[1]]=2
while cord[0] != finish_y and cord[1] != finish_x:    
    cord = Next_Step(cord,maze)
maze[cord[0]+1][cord[1]]=2
maze[cord[0]+2][cord[1]]=2#почему-то он отказыватеся рисовать последние 2 звёздочки независимо от того, какое finish_y я поставлю
with open("depth_search.txt", "w") as f:
    for line in maze:
        for elem in line:
            if elem == wall:
                f.write('#')
            elif elem == path:
                f.write('*')
            else:
                f.write(' ')
        f.write('\n')








    
    

    