import random as rand
import numpy as np
import pdb
#random.sample(range(1, 18), 4) #8,4,5,9
Spisok=list(range(0,999999))
Spisok1=[]
for i in range(999999):
    Spisok1.append(-1+rand.random()*2)
r=26/10
k=0
C=[]
while k<42000:
    x=rand.random()*r
    y=rand.random()*r
    if np.sqrt(x**2 + y**2)<r:
        C.append(complex(x,y))
        k+=1
T=[]
Text=[]
file=open('Text.txt' , 'r', encoding='utf-8')
for i in file.readlines():
    T.append(i.split())
file.close()
c=''
for i in T:
    if i!=[]:
        c=list(i)
        c=''.join(str(c).split('['))
        c=''.join(str(c).split(','))
        c=''.join(str(c).split(']'))
        c=''.join(str(c).split('.'))
        c=''.join(str(c).split(';'))
        c=''.join(str(c).split(':'))
        c=''.join(str(c).split('-'))
        Text+=c.split()
def FindSort(arr): # Сортировка выбором
    for i in range(len(arr)):
       m=min(arr[i:])
       ind=arr.index(m)
       if m<arr[i]:
           arr[i],arr[ind]=arr[ind],arr[i]
#FindSort(Text)

def insertionsSort(arr): #Сортировка вставкой
    N=len(arr)
    for i in range(1,N):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break



def ShellSort(arr): #Сортировка Шелла
    N=len(arr)
    h=N//2
    while h>0:
        for i in range(h,N):
            j=i
            while j-h>=0 and arr[j]<arr[j-h]:
                arr[j-h],arr[j]=arr[j],arr[j-h]
                j=j-h
                
        h=h//2

#ShellSort(Spisok1)
ModulCompl=[]
for i in C:
    ModulCompl.append(abs(i))
#insertionsSort(ModulCompl)

def sort(arr,i,N):
    Pravda=True
    while Pravda:
        left=2*i+1
        right=2*i+2
        i_old=i
        if left<=N and arr[left]>arr[i_old]:
            i_old=left
        if right<=N and arr[right]>arr[i_old]:
            i_old=right
        if i==i_old:
            Pravda=False
        else:
            arr[i_old],arr[i]=arr[i],arr[i_old]
            i=i_old
def build_derevo(arr):
    ind=len(arr)//2
    N=len(arr)
    for k in reversed(range(0,ind+1)):
        sort(arr,k,N-1)

def heap_sort(arr): #Пирамидальная сортировка
    build_derevo(arr)
    for j in reversed(range(0,len(arr))):
        arr[0],arr[j]=arr[j],arr[0]
        sort(arr,0,j-1)





heap_sort(Spisok1)
