#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import time

## Functions
# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells

## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 50
width = 50
maze = []


# Denote all cells as unvisited
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])


			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)



# Mark the remaining unvisited cells as walls
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
	if (maze[1][i] == 'c'):
		maze[0][i] = 'c'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == 'c'):
		maze[height-1][i] = 'c'
		break

# Print final maze
#printMaze(maze)

f = open('maze-for-u.txt', 'w')
for i in range(len(maze)):
	for j in range(len(maze[0])):
		if maze[i][j] == 'w':
			f.write('#')
		else:
			f.write(' ')
	f.write('\n')
f.close()




# In[ ]:
#%%
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
#%%

maze_num=np.zeros((height,width))
    
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'w'):
            maze_num[i,j]=1
			
#%%



#%%

# Начало тут

# -------------------------------------------------------

# Создадим список вершин графа
# Для этого запишем все пары (i,j) в массиве, которые являются ячейками

V=[]  # Вершины

for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'c'):
            V.append((i,j))

Inf=np.Inf
d=np.zeros(len(V))
d[:]=Inf   # Хранит расстояния до вершин

Ways={}  # Тут храним маршруты, ключ в словаре это номер вершины в V, значение это последовательность вершин


# Сгенерируем координаты аватара и ключа
Avatar=V[np.random.randint(len(V))]
Key=V[np.random.randint(len(V))]

Exits=[]

i=0
for j in range(0, width):
    if (maze[i][j] == 'c'):
        print(f'({i},{j}) - выход')
        Exits.append((i,j))

i=height-1
for j in range(0, width):
    if (maze[i][j] == 'c'):
        print(f'({i},{j}) - выход')
        Exits.append((i,j))

plt.imshow(maze_num)
plt.plot([Avatar[1]],[Avatar[0]],'ro')
plt.plot([Key[1]],[Key[0]],'r*')
#%%

# Алгоритм Дейкстры 

# Создаем массив флагов, где 1- посещенные вершины, 0 - не посещенные

start=time.time()


flag_visits=np.zeros((len(V)))  # Все вершины назначаем не посещенными
Inf=np.Inf
d=np.zeros(len(V))
d[:]=Inf    # Тут храним расстояния до вершины по номеру

# Теперь отметим посещенной начальную вершину

index=V.index(Key)
print(f' Начальная координата алгоритма {V[index]}')
#flag[index]=1
d[index]=0    
Ways={}
Ways[V[index]]=[index]


def Near_d_update(index):
    
    global Ways,d,flag_visits
    i0=V[index][0]
    j0=V[index][1]
    
    near_vertex=[(i0+1,j0),(i0-1,j0),(i0,j0+1),(i0,j0-1)] # четыре соседние вершины
    
    for vertex in near_vertex:
        if vertex in V:
            index2=V.index(vertex)
            l=d[index]+1
            #print(index2)
            if flag_visits[index2]==0 and d[index2]>l:
             
                d[index2]=l
                way=(Ways[V[index]].copy())
                way.append(index2)
                Ways[V[index2]]=way
                

def Check_vertex(index):
    
    global Ways,d,flag_visits
    
    if flag_visits[index]==0:
        return -1
    
    i0=V[index][0]
    j0=V[index][1]
    n_vertex=0
    n_visited_vertex=0
    near_vertex=[(i0+1,j0),(i0-1,j0),(i0,j0+1),(i0,j0-1)] # четыре соседние вершины
    for vertex in near_vertex:
        if vertex in V:
            n_vertex+=1  #считаем число соседних вершин
            index2=V.index(vertex)
            if flag_visits[index2]==1:
                n_visited_vertex+=1   # считаем число соседних посещенных вершин
    
    if n_visited_vertex==n_vertex:
        # если все соседние вершины посещены, то путь к этой вершине можно удалять
        print(f'удаляем вершину {V[index]}')
        way=Ways.pop(V[index],[]) # Возвращаем пустой список, если такой вершины уже нет
        # Вернем индекс вершины, из которой мы попали в эту, чтобы её тоже проверить
        if len(way)>1:
            index_previous=way[-2]
            
            return index_previous
        
            
    return -1    


flag_Avatar=0
flag_Exit=0
way_Avatar=0
way_Exit=0
Count_Max=len(flag_visits)
#Count_Max=10
Count=0
while flag_Avatar*flag_Exit==0 and Count<Count_Max:
    
    Count+=1
    # Находим следующую вершину 
    D_min=d[flag_visits<1].min() # Ищем только среди не посещённых 
    indexes=np.where(d==D_min)[0] # Находим индексы с этим значением
    for i in indexes:   # Из всех найденных индексов берём первый не посещенный
        if flag_visits[i]<1:
            index=i
            break
    
    # Найденыый index это номер вершины в которую мы переходим
    
    # Проверяем ни одна ли это из искомых вершин
    if V[index]==Avatar:
        print(f'Найден минимальный путь до Аватара\n')
        way_Avatar=Ways[V[index]]
        flag_Avatar=1
    if V[index] in Exits:
        print(f'Найден минимальный путь до Выхода \n')
        way_Exit=Ways[V[index]]
        flag_Exit=1
    # Отмечаем ее посещенной    
    flag_visits[index]=1
    
    print(f'Посетили вершину {V[index]}, итерация номер {Count}, вес словаря путей {sys.getsizeof(Ways)//1024} Мб')
    # Обновляем расстояния для соседних вершин
    Near_d_update(index)
    # Проверяем можно ли удалять вершину и путь к ней
    while index>0:
        index=Check_vertex(index)
        
    #Повторяем процедуру
end=time.time()
print(f'\n -------------------------------- \n time = {end-start} ')
#%%
plt.imshow(maze_num)
plt.plot([Avatar[1]],[Avatar[0]],'ro')
plt.plot([Key[1]],[Key[0]],'r*')    
X=[]
Y=[]    
for v in way_Exit:
    y,x=V[v]
    X.append(x)
    Y.append(y)
plt.plot(X,Y,'r-')

X=[]
Y=[]    
for v in way_Avatar:
    y,x=V[v]
    X.append(x)
    Y.append(y)
plt.plot(X,Y,'g--')    

#%%

    
for v in way_Avatar:
    i,j=V[v]
    maze[i][j] = '.'


for v in way_Exit:
    i,j=V[v]
    maze[i][j] =','
    
i,j=Key

maze[i][j] = '*'



#%%

f = open('maze-for-u.txt', 'w')
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'w':
            f.write('#')
        if maze[i][j] == '.':
            f.write('.')
        if maze[i][j] == ',':
            f.write(',')
        if maze[i][j] == '*':
            f.write('*')
        else:
            f.write(' ')
    f.write('\n')

f.close()


# In[ ]:





# In[ ]:




