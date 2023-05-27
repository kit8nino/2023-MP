import string
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



s=(0,1)
lab[s[0]][s[1]]='S'

f=(599,798)
lab[f[0]][f[1]]='F'

#print(lab[500][300])

k=(500,300)
lab[k[0]][k[1]]='*'

width=len(lab[0])
height=len(lab)

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
            if 0 < ny < height and 0 < nx < width and not wasHere[ny][nx] and field[ny][nx] != '#':
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

a=poiskVglub(lab,s,k)
for i in range(1,len(a)-1):
    lab[a[i][0]][a[i][1]] = '@'
    
b=poiskVglub(lab,k,f)
for i in range(1,len(b)-1):
    if lab[b[i][0]][b[i][1]] == "@":
        lab[b[i][0]][b[i][1]] = 'W'
    else:
        lab[b[i][0]][b[i][1]] = '$'
    
c=AtS(lab,height,width)



t = open('Otvet.txt', 'w')
text = t.writelines(c)
t.close()

