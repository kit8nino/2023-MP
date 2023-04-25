import random
import numpy as np
import codecs
import re
#print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне

#12, 1, 9, 7

def swap(Mas,i):
    t=Mas[i]
    Mas[i]=Mas[i-1]
    Mas[i-1]=t

#Генерация случайных исходных данных

a=[]
a=random.sample(range(0, 999999), 999999)
b=[]
for j in range(0,999999):
    b.append(random.uniform(-1,1))
r=20/4
compl=[]
j=1
while j<=42000:
    real=random.uniform(0, r)
    im=random.uniform(0, r)
    if (np.sqrt(real**2+im**2))<r:
        compl.append(complex(real,im))
        j+=1
file = codecs.open("text.txt", "r", "utf_8_sig" )
text = file.readlines()
c=[]
i=0
t=len(text)
while (i<t):
    line=text[i]
    line=re.sub("[^А-Яа-я]"," ",line)
    c+=line.split()
    i+=1  



#12 Сортировка подсчетом
print("Сортировка подсчетом массива целых чисел:")
cut=[0]*(len(a))
for i in range(0,len(a)):
    for k in range(0,len(a)):
        if i == a[k]:
            cut[i]+=1
for i in range(0,len(a)):
    if cut[i]!=0:
        for j in range(0,cut[i]):
            print(i, end=" ")  


#1 Сортировка перемешиванием

def shaker(Mas,Left,Right):
    j=0
    Right-=1
    while Left<Right:
        min=Mas[Right-j]
        max=Mas[j]
        for i in range(Left,Right+1):
            if max>Mas[i]:
                swap(Mas,i)
            elif (max<Mas[i]):
                max=Mas[i]
        min=Mas[Right-j]
        for i in range(Left,Right+1):
            if min<Mas[Right-i]:
                swap(Mas,Right-i+1)
            elif (min>Mas[Right-i]):
                min=Mas[Right-i]
        j+=1
        Left+=1
        Right-=1
    return Mas

b1=b.copy()
P1 = shaker(b1, 0, len(b1))
print("/nСортировка перемешиванием массива вещественных чисел:",P1)



#9 Пирамидальная сортировка

def headcompl(Mas,i,End):
    headd=i
    left=2*i+1
    right=2*i+2
    
    if left<End and abs(Mas[headd])<abs(Mas[left]):
        headd=left
    if right<End and abs(Mas[headd])<abs(Mas[right]):
        headd=right
    if headd!=i:
        t=Mas[i]
        Mas[i]=Mas[headd]
        Mas[headd]=t
        headcompl(Mas,headd,End)
def headsortcompl(Mas,Start,End):
    i=len(Mas)
    while i>=Start:
        headcompl(Mas,i,len(Mas))
        i-=1
    i=len(Mas)-1
    while i>Start:
        t=Mas[i]
        Mas[i]=Mas[0]
        Mas[0]=t
        headcompl(Mas,0, i)
        i-=1
    return Mas

compl1=compl.copy()
P2 = headsortcompl(compl1,0,len(compl1))
print("Пирамидальная сортировка массива комплексных чисел:", P2)



#7 Гномья сортировка
def gnome(Mas,Start,End):
    i=Start+1
    while Start < End:
        if Mas[Start-1]<Mas[Start]:
            Start=i
            i+=1
        else:
            swap(Mas,Start)
            Start-=1
            if Start == 0:
                Start=i
                i+=1
    return Mas  

#a=[34,4,22,5,7,0,2,66,111,3]
c1=c.copy()
P3 = gnome(c1,0,len(c1))
print("Гномья сортировка текста из книги:", P3)


