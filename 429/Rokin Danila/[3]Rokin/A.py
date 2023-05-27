import string
import heapq as hp


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

def h(finish,x):
    return abs(finish[0]-x[0])+abs(finish[1]-x[1])

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
            if  0 < nx < width and 0 < ny < height and not closedList[ny][nx] and lab[ny][nx] != '#' :
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
a=Astar(lab,s,k)
for i in range(1,len(a)-1):
    lab[a[i][0]][a[i][1]] = '@'
    
b=Astar(lab,k,f)
for i in range(1,len(b)-1):
    if lab[b[i][0]][b[i][1]] == "@":
        lab[b[i][0]][b[i][1]] = 'W'
    else:
        lab[b[i][0]][b[i][1]] = '$'
    
c=AtS(lab,height,width)



t = open('OtvetASTAR.txt', 'w')
text = t.writelines(c)
t.close()
   
    

























