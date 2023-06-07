import string
import heapq as hp
from collections import deque

tab = str.maketrans(' ', '.')
file = open('maze-for-u.txt',encoding=('UTF-8'))
text = file.read()
l = text.translate(tab).split()
file.close()

lab=[]
for i in range(len(l)):
    lab.append(list(l[i]))
    
    
    
def AtS(arr,height,width):
    Str=''
    for i in range(height):
        for j in range(width):
             Str += str(arr[i][j])
        Str += '\n'
    return Str



start=(0,1)
lab[start[0]][start[1]]='S'

finish=(599,798)
lab[finish[0]][finish[1]]='F'

#print(lab[500][300])

key=(500,300)
lab[key[0]][key[1]]='*'

width=len(lab[0])
height=len(lab)

def uslovia(y,x,wasHere,field):
    if 0 < y < height and 0 < x < width and not wasHere[y][x] and field[y][x] != '#':
        return True    

def h(finish,x):
    return abs(finish[0]-x[0])+abs(finish[1]-x[1])

def poiskVglub(field,start,finish):
    bigNum = -1
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    distance = [[bigNum] * width for i in range(height)]
    p = [[None] * width for i in range(height)]
    wasHere = [[False] * width for i in range(height)]
    queue  = deque()
    
    distance[start[0]][start[1]] = 0
    wasHere[start[0]][start[1]] = True
    queue.append(start)
    
    while len(queue) != 0 :
        y , x = queue.pop()
        for dx , dy in delta:
            nx = x + dx
            ny = y + dy
            if uslovia(ny,nx,wasHere,field):
               distance[ny][nx] = distance[y][x] + 1
               wasHere[ny][nx] = True
               p[ny][nx] = (y,x)
               queue.append((ny,nx))
#    print(AtS(distance,n,m))
    if distance[finish[0]][finish[1]] == -1:
        print('Маршрута не существует')
    else:
        print('Длина маршрута:', distance[finish[0]][finish[1]]-1)
    cur = finish
    path = []
    while cur is not None:
        path.append(cur)
        cur = p[cur[0]][cur[1]]
    path.reverse()
    return path

toKey=poiskVglub(lab,start,key)
for i in range(1,len(toKey)-1):
    lab[toKey[i][0]][toKey[i][1]] = '$'
    



def Astar(field,start,finish):
    bigNum = -1
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    openList = [(0,start)]
    closedList = [[False]* width for i in range(height)]
    g=[[bigNum]* width for i in range(height)]
    f=[[bigNum]* width for i in range(height)]
    p = [[None] * width for i in range(height)]
    g[start[0]][start[1]] = 0
    f[start[0]][start[1]] = h(finish,start)
    closedList[start[0]][start[1]]=True
    while openList != []:
        arr = hp.heappop(openList)
        y = arr[1][0]
        x = arr[1][1]
        for dx , dy in delta:
            nx = x+dx
            ny= y+dy
            if  uslovia(ny,nx,closedList,field):
                g[ny][nx] = g[y][x] + 1
                f[ny][nx] = g[ny][nx]+h(finish,(ny,nx))
                hp.heappush(openList,(g[ny][nx],(ny,nx)))
                p[ny][nx] = (y,x)
                closedList[ny][nx] = True
        if (y,x) == finish:
            c=finish
            path = []
            while c is not None:
                path.append(c)
                c = p[c[0]][c[1]]
            path.reverse()
            return path
            break
        
        
toFinish=Astar(lab,key,finish)
for i in range(1,len(toFinish)-1):
    lab[toFinish[i][0]][toFinish[i][1]] = '@'
    

c=AtS(lab,height,width)
tab = str.maketrans('.$@', ' .,')


t = open('maze-for-me.txt', 'w')
text = t.writelines(c.translate(tab))
t.close()
   
    

























