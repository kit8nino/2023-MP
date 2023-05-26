import numpy as np
import random as rd
#print(random.sample(range(1, 18), 4)) #дало 9,11,3,4
# Num 9 - Heapsort, для массива от 0 до 9999999
def make_heap(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[i]<  arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          make_heap(arr, n, largest)
        
def Heapsort(arr):
    n = len(Num)
    for i in range(n//2-1,-1,-1):
        make_heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        make_heap(arr, i, 0)

Num=np.arange(0,1000000)
np.random.shuffle(Num)
Heapsort(Num)
#print(Num)
#Num 11 - Merge sort для массива 99999 чисел в [-1,1]
def Merge(B,C):
    D = []
    rB = len(B)
    lB = 0
    rC = len(C)
    lC = 0
    while (lB<rB) & (lC<rC):
        if B[lB]<=C[lC]:
            D.append(B[lB])
            lB += 1         
        else:
            D.append(C[lC])
            lC += 1
    if lB==rB:
        for i in range (lC,rC):
            D.append(C[i])
    else:
        for i in range (lB,rB):
            D.append(B[i])
    return (D)

def Divide(to_sort):
    count = 0
    A = []    
    for i in range(len(to_sort)):
        A.append([to_sort[i]])        
    m = len(to_sort)//2
    T = []  
    while m>0:
        count = 0
        for i in range(0,m):
            T.append(Merge(A[count],A[count+1]))
            count += 2
            
        if (len(A)%2)!=0:
            T[len(T)-1]=Merge(T[len(T)-1],A[len(A)-1])    
            
        A = T
        T=[]
        m = m//2             
    return (A)   

Num=np.zeros(99999)
for i in range(0,len(Num)):
    Num[i]=rd.uniform(-1, 1)
#print (Divide(Num))
#Num 3 - comb sort для комплексных числел
r = 10/8
Num =np.array([])
for i in range (0,42000):
    x=rd.uniform(-r, r)
    y=rd.uniform(-r, r)
    Num=np.append(Num,complex(x,y))

def Comb_sort(Num):
    n=len(Num)
    step=int(len(Num)/1.247331)
    flag=True
    while step > 1 or flag:
        flag=False
        i=0
        while i + step < n:
            if abs(Num[i]) > abs(Num[i+step]):
                Num[i],Num[i+step]= Num[i+step],Num[i]
                flag=True
            i=i+1
        if step>1:
            step = int(step/1.247331)
    return(Num)
#print(Comb_sort(Num))

#Num 4 - Insertion sort для слов
file = open('[2]_Text_For_4th_sort.txt',"r" )
words = []
line = file.readline().split()
while line:
    words.extend(line)
    line = file.readline().split()

print(words)
def InsertionSort(words):
    for i in range(1,len(words)):
        word = len(words[i])
        j=i

        while j>0 and word < len(words[j-1]):
            words[j],words[j-1] = words[j-1],words[j]
            j-=1
InsertionSort(words)
print(words)