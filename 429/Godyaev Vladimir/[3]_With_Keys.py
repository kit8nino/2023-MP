import numpy as np
import queue as Q 

wall=1
free=0
path=2
path_after_key=3
visited = -1
visited_after_key=-2
key = 5


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
def Next_Step(cord,maze,key_taken):
    if key_taken == True:
        if maze[cord[0]+1][cord[1]] == 0 or maze[cord[0]+1][cord[1]] == -1 or maze[cord[0]+1][cord[1]] == 2:
            cord[0]=cord[0]+1
            maze[cord[0]][cord[1]] = path_after_key
        elif maze[cord[0]][cord[1]+1] == 0 or maze[cord[0]][cord[1]+1] == -1 or maze[cord[0]][cord[1]+1] == 2:
            cord[1]=cord[1]+1
            maze[cord[0]][cord[1]] = path_after_key
            
        elif maze[cord[0]][cord[1]-1] == 0 or maze[cord[0]+1][cord[1]-1] == -1 or maze[cord[0]][cord[1]-1] == 2:
            cord[1]=cord[1]-1
            maze[cord[0]][cord[1]] = path_after_key
            
        elif maze[cord[0]-1][cord[1]] == 0 or maze[cord[0]-1][cord[1]] == -1 or maze[cord[0]-1][cord[1]] == 2:   
            cord[0]=cord[0]-1
            maze[cord[0]][cord[1]] = path_after_key      
        else: Backtrack(cord,maze,key_taken)   
    
    if key_taken == False:
        if  cord[0]+1<600 and maze[cord[0]+1][cord[1]] == 0 or maze[cord[0]+1][cord[1]] == 5:
            cord[0]=cord[0]+1
            if maze[cord[0]][cord[1]] == 5:
                key_taken = True
            else:     
                maze[cord[0]][cord[1]] = path
        elif maze[cord[0]][cord[1]+1] == 0 or maze[cord[0]][cord[1]+1] == 5 :
            cord[1]=cord[1]+1
            if maze[cord[0]][cord[1]] == 5:
                key_taken = True
            else:     
                maze[cord[0]][cord[1]] = path
            
        elif maze[cord[0]][cord[1]-1] == 0 or maze[cord[0]][cord[1]-1] == 5:
            cord[1]=cord[1]-1
            if maze[cord[0]][cord[1]] == 5:
                key_taken = True
            else:     
                maze[cord[0]][cord[1]] = path
            
        elif maze[cord[0]-1][cord[1]] == 0 or maze[cord[0]-1][cord[1]] == 5:    
            cord[0]=cord[0]-1
            if maze[cord[0]][cord[1]] == 5:
                key_taken = True
            else:     
                maze[cord[0]][cord[1]] = path           
        else: Backtrack(cord,maze,key_taken)
            
    
    
    return(cord,key_taken)
#Функция, которая в случае тупика возвращает назад
def Backtrack(cord,maze,key_taken):
    if key_taken == True:
        if maze[cord[0]-1][cord[1]] == 3:            
            maze[cord[0]][cord[1]] = visited_after_key
            cord[0]=cord[0]-1
            
        elif maze[cord[0]][cord[1]-1] == 3:    
            maze[cord[0]][cord[1]] = visited_after_key
            cord[1]=cord[1]-1
            
        elif maze[cord[0]][cord[1]+1] == 3:    
            maze[cord[0]][cord[1]] = visited_after_key
            cord[1]=cord[1]+1
        
        elif maze[cord[0]+1][cord[1]] == 3:    
            maze[cord[0]][cord[1]] = visited_after_key
            cord[0]=cord[0]+1

    
    
    if key_taken == False:
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
maze[416][482] = key
key_taken=False
maze[cord[0]][cord[1]]=2
while cord[0] != finish_y and cord[1] != finish_x or key_taken==False:      
    cord,key_taken = Next_Step(cord,maze,key_taken)
maze[cord[0]+1][cord[1]]=3
maze[cord[0]+2][cord[1]]=3#почему-то он отказыватеся рисовать последние 2 точки пути независимо от того, какое finish_y я поставлю
with open("[3]_depth_search_with_keys.txt", "w") as f:
    for line in maze:
        for elem in line:
            if elem == wall:
                f.write('#')
            elif elem == path:
                f.write('.')
            elif elem == key:
                f.write('*')
            elif elem == path_after_key:
                f.write(',')
            else:
                f.write(' ')
        f.write('\n')

#_______________________________________A*___________________________________________________________________________
def Read_File(file_name = 'maze-for-u.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height =len(maze_raw)
    length =len(maze_raw[0])
    maze = np.array([])
    maze = np.append(maze,[wall if x[i]=='#' else free for x in maze_raw for i in range(length)])
    maze = np.reshape(maze,(height,length))   
    return maze,height,length


#считает растояние до конечной точки по прямой
def Dist_to_End(x,y):
    end_x,end_y=length-2,height-1
    return(abs(end_x-x)+abs(end_y-y))

#работа с соседями точки
def Neighbor_get(cord,cost,maze,path,visited,key_taken):

   # maze[cord[0],cord[1]]=-1
    
    cordT=[cord[0],cord[1]]
    cordT2=[cord[0],cord[1]]#если я не ввожу эту переменную, то питон будит менять переменную current, что мне очень не надо
     #Граница, которую будем использовать
    if cord[0]-1 > 0 and ( maze[cord[0]-1][cord[1]] != 1 and maze[cord[0]-1][cord[1]] != path and maze[cord[0]-1][cord[1]] != visited ):    
                
        maze[cord[0]][cord[1]] = visited
        cordT2[0]=cord[0]-1
        if maze[cordT2[0]][cordT2[1]] ==key:
            key_taken=  True
            Current_Cost[current_tuple]=0
        else:
            maze[cordT2[0]][cordT2[1]] = visited

            
    elif cord[1]-1 > 0 and maze[cord[0]][cord[1]-1] != 1  and maze[cord[0]][cord[1]-1] != path and maze[cord[0]][cord[1]-1] != visited :    
        maze[cord[0]][cord[1]] = visited
        cordT2[1]=cord[1]-1
        if maze[cordT2[0]][cordT2[1]] ==key:
            key_taken=  True

            Current_Cost[current_tuple]=0
        else:
            maze[cordT2[0]][cordT2[1]] = visited
            
    elif cord[1]+1 <800 and maze[cord[0]][cord[1]+1] != 1 and maze[cord[0]][cord[1]+1] != path and maze[cord[0]][cord[1]+1] != visited :    
        maze[cord[0]][cord[1]] = visited
        cordT2[1]=cord[1]+1
        if maze[cordT2[0]][cordT2[1]] ==key:
            key_taken=  True
            Current_Cost[current_tuple]=0
        else:
            maze[cordT2[0]][cordT2[1]] = visited
        
    elif cord[0]+1 <600 and maze[cord[0]+1][cord[1]] != 1 and maze[cord[0]+1][cord[1]] != path and maze[cord[0]+1][cord[1]] != visited :    
        maze[cord[0]][cord[1]] = visited
        cordT2[0]=cord[0]+1
        if maze[cordT2[0]][cordT2[1]] ==key:
            key_taken=  True
            Current_Cost[current_tuple]=0
        else:
            maze[cordT2[0]][cordT2[1]] = visited
        
    #добавление неиспользованных границ в border
    if cord[0]+1 <600 and maze[cord[0]+1][cord[1]] != 1 and maze[cord[0]+1][cord[1]] != path and maze[cord[0]+1][cord[1]] != visited :
        cord1=cordT[0]+1
        cost=cost
        border.put([cord1,cordT[1]],cost+Dist_to_End(cordT[1], cord1)*weight_g)
        
        Path_Back[(cord1,cordT[1])] = cord
        Current_Cost[(cord1,cordT[1])]=cost + 1
        
    if  cord[1]+1 <800 and maze[cord[0]][cord[1]+1] != 1 and maze[cord[0]][cord[1]+1] != path and maze[cord[0]][cord[1]+1] != visited : 
        cord1=cordT[1]+1
        cost=cost
        border.put([cordT[0],cord1],cost+Dist_to_End(cord1, cordT[0])*weight_g)
        
        Path_Back[(cordT[0],cord1)] = cord
        Current_Cost[(cordT[0],cord1)]=cost + 1
        
    if  cord[1]-1 > 0 and maze[cord[0]][cord[1]-1] != 1  and maze[cord[0]][cord[1]-1] != path and maze[cord[0]][cord[1]-1] != visited :
        cord1=cordT[1]-1
        cost=cost
        border.put([cordT[0],cord1],cost+Dist_to_End(cord1, cordT[0])*weight_g)
        
        Path_Back[(cordT[0],cord1)] = cord
        Current_Cost[(cordT[0],cord1)]=cost + 1
        
    if cord[0]-1 > 0 and maze[cord[0]-1][cord[1]] != 1 and maze[cord[0]-1][cord[1]] != path and maze[cord[0]-1][cord[1]] != visited :   
        cord1=cordT[0]-1
        cost=cost
        border.put([cord1,cordT[1]],cost+Dist_to_End(cordT[1], cord1)*weight_g)    
        
        Path_Back[(cord1,cordT[1])] = cord
        Current_Cost[(cord1,cordT[1])]=cost + 1
        
    return cordT2,key_taken




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
maze[402][487] = key
key_taken=False
current_path=path
current_visited=visited

while not border.empty():
    current=border.get()
    current_tuple=(current[0],current[1])#чтоб обращаться к ключу
    
#    print(current,current_tuple,Current_Cost[current_tuple])   
    
    if key_taken==True:
        current_path=path_after_key
        current_visited =visited_after_key 
    if current == [finish_y,finish_x]:
        break
    
    #print(current)
    next,key_taken = Neighbor_get(current,Current_Cost[current_tuple],maze,current_path,current_visited,key_taken)  
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
path_2=[]
reached=False
maze[402][487] = key
while current != [start_y,start_x]: 
   current = Path_Back[current_tuple]
   current_tuple=(current[0],current[1])
   if reached == False:
       path.append(current)
   if reached == True:
       path_2.append(current)       
   if maze[current[0],current[1]]==key:
        reached == True
    

with open("[3]_A_with_keys.txt", "w") as f:
    for i in range(height):
        for j in range(length):
            if maze[i][j] == wall:
                f.write('#')
            elif maze[i][j] == key:
                f.write('*')               
            elif [i,j] in path:
                f.write(',')
            elif [i,j] in path_2:
                f.write('.')   
            else:
                f.write(' ')
        f.write('\n')