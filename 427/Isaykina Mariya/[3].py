import numpy as np
import codecs
import random
from collections import deque

#Проверяет, достиг ли цикл конца сверху или снизу
def exits(x,y,t):
    stopy=len(t)-1
    stopx=len(t[0])-2
    if ((x==stopx) and ((y+1)==stopy)) or ((x==len(t)-stopx-1) and (y==len(t)-stopy)):
        return True
    return False

#Генерирует координаты аватара и ключа вне стен
def coord(textik):
    x=random.randint(0, len(textik))
    y=random.randint(0, len(textik[0])-2)
    stena=True
    while stena==True:
        print(textik[x,y],x,y)
        if textik[x,y]==' ':
            stena=False
        else:
            x=random.randint(0, len(textik))
            y=random.randint(0, len(textik[0])-2)
    return x, y

#Функция поиска в ширину
def poisk(startx, starty, stopx, stopy, graph):
    q=deque()
    x=startx
    y=starty
    visited=[]
    visitedway=[[[]]*len(graph[0]) for i in range(0,len(graph))] #Массив, в которым данную координату (х,у) будет записан путь, который прошел аватар до прихода в данную точку
    pair=[x,y]
    Stop=False
    q.append(pair)
    while Stop!=True:
        x,y=q[0]
        pair=[x,y]
        visited.append(pair)
        if stopx==599:
            Stop=exits(x,y,graph)
            if x==599 or x==0:
                break
        q.popleft()
        if x==stopx and y==stopy:
            Stop=True
            break
        if y<799 and x>-1 and x<600 and y>-2:
            if graph[x][y+1]==' ':
                pair=[x,y+1]
                if pair not in visited:
                    q.append(pair)
                    visitedway[x][y+1]=visitedway[x][y]+[x,y] #Путь, записанный в предыдущей координате + сама предыдущая координата
        if x<599 and x>-2 and y<800 and y>-1:
            if graph[x+1][y]==' ':
                pair=[x+1,y]
                if pair not in visited:
                    q.append(pair)
                    visitedway[x+1][y]=visitedway[x][y]+[x,y]
        if x<600 and x>-1 and y<801 and y>0:
            if graph[x][y-1]==' ':
                pair=[x,y-1]
                if pair not in visited:
                    q.append(pair)
                    visitedway[x][y-1]=visitedway[x][y]+[x,y]
        if x<601 and x>0 and y<800 and y>-1:
            if graph[x-1][y]==' ':
                pair=[x-1,y]
                if pair not in visited:
                    q.append(pair)
                    visitedway[x-1][y]=visitedway[x][y]+[x,y]
    return visitedway, x
            
#Подключение файла
file=codecs.open("maze-for-u.txt","r","utf_8_sig")
text=file.readlines()
textt=[]
for i in range(0,len(text)):
    line=[]
    for j in range(0,len(text[i])-2):
        simv=text[i][j]
        line+=simv
    textt.append(line)
textik=np.array(textt)

#Генерация координат аватара и ключа
coord_avA, coord_avB=coord(textik)
coord_keyA, coord_keyB=coord(textik)


#Поиск в ширину
massiv1,k=poisk(coord_avA,coord_avB,coord_keyA,coord_keyB,textik) #Путь от аватара до ключа
not_way=massiv1[coord_keyA][coord_keyB]
way1=[]
y=1
while y<len(not_way):
    coord=[not_way[y-1],not_way[y]]
    way1.append(coord)
    y+=2
print(way1)


massiv2, endx=poisk(coord_keyA,coord_keyB,599,798,textik)
way2=[] #Путь аватара от ключа до выхода
y=1
if endx==0: #Проверка на то, в какой из выходов пришел аватар
    not_way=massiv2[endx][1]
    while y<len(not_way):
        coord=[not_way[y-1],not_way[y]]
        way2.append(coord)
        y+=2
elif endx==599:
    not_way=massiv2[endx][798]
    while y<len(not_way):
        coord=[not_way[y-1],not_way[y]]
        way2.append(coord)
        y+=2
print(way2)    

#Запись в файл
rezult=[]

for i in range(0,len(textt)):
    line=[]
    for j in range(0,len(textt[0])):
        simv=textik[i][j]
        pair=[i,j]
        if i==coord_keyA and j==coord_keyB:
            simv='*'
        elif pair in way1:
            simv='.'
        elif pair in way2:
            simv=','
        line+=simv
    rezult.append(line)

f=open('maze-for-me-done.txt',"w")
for lines in rezult:
    stroka=""
    for index in lines:
        stroka+=index
    f.write(stroka +'\n')