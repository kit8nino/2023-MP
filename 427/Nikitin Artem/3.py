import pdb
import heapq
def maze_cout(file_name='maze-for-u.txt'):
    maze=open(file_name).read().split('\n')[:-1]
    height=len(maze)
    weight=len(maze[0])
    A=[[0 for i in range(weight)]for j in range(height)]
    #pdb.set_trace()
    for i in(range(height)):
        for j in range(weight):
            if maze[i][j]=='#':
                A[i][j]=1
    return(A, weight, height)

maze,weight,height=maze_cout()
y0,x0=220,328 #начальные координаты аватара
while maze[y0][x0]==1:
    x0+=1
    y0+=1
print("Начальные координаты аватара по у ",y0 ,"по х ",x0)
start=(y0,x0)
ykey,xkey=421,300 #координаты ключа
while maze[ykey][xkey]==1:
    ykey+=1
    xkey+=1
print("Координаты ключа по у ",ykey,"по х ",xkey)
key_cord=(ykey,xkey)
def find_greedy_sort(maze,start,key_cord):
    path=[start]
    vizited=[]
   #pdb.set_trace()
    while path[-1] != key_cord:
        y_cord, x_cord=path[-1]
        steps=[(y_cord+1,x_cord),(y_cord-1,x_cord),(y_cord,x_cord+1),(y_cord,x_cord-1)]
        movies=[]
        for move in steps:
            y_cord,x_cord=move
            if x_cord>=0 and x_cord<=weight and y_cord>=0 and y_cord<=height and maze[y_cord][x_cord]==0 and move not in vizited:
                movies.append(move)
        if movies:
            short=[]
            for move in movies:
                short.append(abs(move[0]-key_cord[0])+abs(move[1]-key_cord[1]))
            ind=short.index(min(short))
            path.append(movies[ind])
            vizited.append(movies[ind])
        else:
            path.pop()
    return(path)
pathgreedy=(find_greedy_sort(maze, start, key_cord)) #путь жадным алгоритмом(p.s вычисляется в среднем за 30 секунд)
def distanse(start,end):
    return(abs(start[0]-end[0])+abs(start[1]-end[1]))

start=key_cord
y_exit=len(maze)-1
x_exit=len(maze[0])-2
exitcord=(y_exit,x_exit) #координата выхода
print("Длинна маршрута от аватара до ключа жадным алгоритмом ",len(pathgreedy))

def A_star_sort(maze, start, exitcord, max_path):
    stack = [(0, start, [start])]
    visited = set()
    while stack:
        f, point, summ = heapq.heappop(stack)
        y0 = point[0]
        x0 = point[1]
        if point == exitcord:
            print("Длинна маршрута от ключа до выхода == ", len(summ))
            return summ
        if point in visited:
            continue
        visited.add(point)
        for xstep, ystep in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = x0 + xstep, y0 + ystep
            new_point = (y, x)
            if 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != 1 and (y, x) not in visited:
                new_summ = summ + [new_point]
                g = len(new_summ)
                h = distanse(new_point, exitcord)
                f = g + h
                if len(stack) < max_path:
                    heapq.heappush(stack, (f, new_point, new_summ))
                else:
                    heapq.heappushpop(stack, (f, new_point, new_summ))
    return None
pathA_star=A_star_sort(maze, start, exitcord,10000)
print("Общий маршрут ", len(pathgreedy)+len(pathA_star))

def paint(maze,path1,path2):
    ykey,xkey=path1[-1]
    maze[ykey][xkey]='*'
    for point in path1:
        y=point[0]
        x=point[1]
        maze[y][x]='.'
    for point in path2:
        y=point[0]
        x=point[1]
        maze[y][x]=','

paint(maze,pathgreedy,pathA_star)
f=open('maze-for-me-done.txt','w')
for line in maze:
    for row in line:
        f.write(str(row))
    f.write("\n")
f.close()



