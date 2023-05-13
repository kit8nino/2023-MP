import numpy as np
import queue as Q 

wall=1
free=0
path=2
visited = -1

#_______________________________________Поиск в глубину___________________________________________________________________________
def Read_File(file_name = 'maze-for-u.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height =len(maze_raw)
    length =len(maze_raw[0])
    maze = np.array([])
    maze = np.append(maze,[wall if x[i]=='#' else free for x in maze_raw for i in range(length)])
    maze = np.reshape(maze,(height,length))   
    return maze,height,length

#Функция, отвечающая за следующий шаг
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
#Функция, которая в случае тупика возвращает назад
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
maze[cord[0]+2][cord[1]]=2#почему-то он отказыватеся рисовать последние 2 точки пути независимо от того, какое finish_y я поставлю
with open("[3]_depth_search.txt", "w") as f:
    for line in maze:
        for elem in line:
            if elem == wall:
                f.write('#')
            elif elem == path:
                f.write('.')
            else:
                f.write(' ')
        f.write('\n')

#________________________________Алгоритм А*______________________________________________________________________________________

#считает растояние до конечной точки по прямой
def Dist_to_End(x,y):
    end_x,end_y=length-2,height-1
    return(abs(end_x-x)+abs(end_y-y))

#работа с соседями точки
def Neighbor_get(cord,cost,maze):

   # maze[cord[0],cord[1]]=-1
    
    cordT=[cord[0],cord[1]]
    cordT2=[cord[0],cord[1]]#если я не ввожу эту переменную, то питон будит менять переменную current, что мне очень не надо
     #Граница, которую будем использовать
    if maze[cord[0]+1][cord[1]] == 0:            
        maze[cord[0]][cord[1]] = visited
        cordT2[0]=cord[0]+1
        maze[cordT2[0]][cordT2[1]] = visited

            
    elif maze[cord[0]][cord[1]+1] == 0:    
        maze[cord[0]][cord[1]] = visited
        cordT2[1]=cord[1]+1
        maze[cordT2[0]][cordT2[1]] = visited
            
    elif maze[cord[0]][cord[1]-1] == 0:    
        maze[cord[0]][cord[1]] = visited
        cordT2[1]=cord[1]-1
        maze[cordT2[0]][cordT2[1]] = visited
        
    elif maze[cord[0]-1][cord[1]] == 0:    
        maze[cord[0]][cord[1]] = visited
        cordT2[0]=cord[0]-1
        maze[cordT2[0]][cordT2[1]] = visited
        
    #добавление неиспользованных границ в border
    if maze[cordT[0]+1][cordT[1]] == 0:
        cord1=cordT[0]+1
        cost=cost
        border.put([cord1,cordT[1]],cost+Dist_to_End(cordT[1], cord1)*weight_g)
        
        Path_Back[(cord1,cordT[1])] = cord
        Current_Cost[(cord1,cordT[1])]=cost + 1
        
    if maze[cordT[0]][cordT[1]+1] == 0:
        cord1=cordT[1]+1
        cost=cost
        border.put([cordT[0],cord1],cost+Dist_to_End(cord1, cordT[0])*weight_g)
        
        Path_Back[(cordT[0],cord1)] = cord
        Current_Cost[(cordT[0],cord1)]=cost + 1
        
    if maze[cordT[0]][cordT[1]-1] == 0:
        cord1=cordT[1]-1
        cost=cost
        border.put([cordT[0],cord1],cost+Dist_to_End(cord1, cordT[0])*weight_g)
        
        Path_Back[(cordT[0],cord1)] = cord
        Current_Cost[(cordT[0],cord1)]=cost + 1
        
    if maze[cordT[0]-1][cordT[1]] == 0:    
        cord1=cordT[0]-1
        cost=cost
        border.put([cord1,cordT[1]],cost+Dist_to_End(cordT[1], cord1)*weight_g)    
        
        Path_Back[(cord1,cordT[1])] = cord
        Current_Cost[(cord1,cordT[1])]=cost + 1
        
    return cordT2




maze,height,length = Read_File()
finish_x,finish_y = length-2,height-1
start_x,start_y = 1,0
cord = [start_y,start_x]
maze[cord[0]][cord[1]]=2
weight_g,weight_h=1,0.1

border = Q.PriorityQueue()
border.put([start_y,start_x],0)
#maxsize-ограничение для очереди
Path_Back={}
Current_Cost={}
Path_Back[start_y,start_x]=[None]
Current_Cost[start_y,start_x]=0

while not border.empty():
    current=border.get()
    current_tuple=(current[0],current[1])#чтоб обращаться к ключу
    
#    print(current,current_tuple,Current_Cost[current_tuple])   
    
    if current == [finish_y,finish_x]:
        break
    #print(current)
    next = Neighbor_get(current,Current_Cost[current_tuple],maze)  
   # print(current,current_tuple,next)
    next_tuple=(next[0],next[1])
    new_cost = Current_Cost[current_tuple]*weight_g + 1
        
    if next_tuple not in Current_Cost or new_cost < Current_Cost[next_tuple]:
        Current_Cost[next_tuple]=new_cost
        priority = new_cost + Dist_to_End(current[1], current[0])*weight_h
        border.put([next[0],next[1]], priority)
        #print(next_tuple,current)
        Path_Back[next_tuple] = current


current = [finish_y,finish_x]
current_tuple=(finish_y,finish_x)

path = [current]
while current != [start_y,start_x]: 
   current = Path_Back[current_tuple]
   current_tuple=(current[0],current[1])
   path.append(current)

with open("[3]_A.txt", "w") as f:
    for i in range(height):
        for j in range(length):
            if maze[i][j] == wall:
                f.write('#')
            elif [i,j] in path:
                f.write('.')
            else:
                f.write(' ')
        f.write('\n')




    
    

    