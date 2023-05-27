#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:46:43 2023

@author: pro
"""
import random
import codecs
import numpy as np
from collections import deque

def x_y(text_mas,k):
    x=random.randint(0, k)
    y=random.randint(0, len(text_mas[0])-2)
    stena=True
    while stena==True:
        if text_mas[x,y]==' ':
            stena=False
        else:
            x=random.randint(0, k)
            y=random.randint(0, len(text_mas[0])-2)
    return x, y

def bfs(field, robot, key):
    n=len(field)
    m=len(field[0])
    oo=10**10
    delta=[(0,-1),(0,1),(1,0),(-1,0)]
    d=[[oo]* m for _ in range (n)]
    p=[[None]* m for _ in range(n)]
    used=[[False]* m for _ in range(n)]
    q=deque()
    d[robot[0]][robot[1]]=0
    used[robot[0]][robot[1]]=True
    q.append(robot)
    while len(q)!=0:
        x, y =q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<nx<n and 0<ny<m and not used[nx][ny] and field[nx][ny]!='#':
                    d[nx][ny]= d[x][y]+1
                    p[nx][ny]= (x,y)
                    used[nx][ny]=True
                    q.append((nx,ny))
    cur=key
    path=[]
    while cur is not None:
        path.append(cur)
        cur= p[cur[0]][cur[1]]
    path.reverse()
    return path, d[key[0]][key[1]]
        

    

fin=codecs.open("maze-for-u.txt","r","utf_8_sig")
field=fin.readlines()

#Записываем лабиринт в массив

n=len(field)
stroka=len(field[0])
text=[]
for i in range(0,n): 
    line=[]
    for j in range(0,len(field[i])-1): 
        line+=field[i][j]
    text.append(line) 
text_mas=np.array(text)
k=len(text_mas)

#Поиск выходов

exit_1=[]
exit_2=[]

for i in range(0,stroka):
    if text_mas[0][i]==' ':
        exit_1=[0,i]
        break
for i in range(0, stroka):
    if text_mas[n-1][i]==' ':
        exit_2=[n-1,i]
        break
print('Выходы',exit_1,exit_2)

#Генерация координат аватара и ключа
robot_x, robot_y=x_y(text_mas, k)
robot=[robot_x, robot_y]
key_x, key_y=x_y(text_mas, k)
key=[key_x, key_y]
text_mas[key_x][key_y]='*'
print("Начальная точка",robot)
print('Ключ',key)

#Ближайший выход
if abs(key[0]-exit_1[0])+abs(key[1]-exit_1[1])< abs(key[0]-exit_2[0])+abs(key[1]-exit_2[1]):
    exit_=exit_1
else:
    exit_=exit_2
print("Ближайший выход", exit_) 

#Запись маршрутов в массив
path_key, l=bfs(field,robot,key)
print('Длина пути от робота до ключа', l)
for i in range(len(path_key)):
    a,b=path_key[i]
    text_mas[a][b]='.'
path_end, l=bfs(field,key,exit_)
print('Длина пути от ключа до ближайшего выхода', l)
for i in range(len(path_end)):
    c,d=path_end[i]
    text_mas[c][d]=','

#Вывод массива в блокнот
f=open('maze-for-me-done.txt',"w")
for l in text_mas:
    st=""
    for i in l:
        st+=i
    f.write(st +'\n') 