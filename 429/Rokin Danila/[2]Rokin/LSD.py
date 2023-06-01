'''Поразрядная сортировка для целых чисел'''
'''Сначала печатает массив целых чисел, потом отсортированный'''
import random as rnd
import numpy as np

colvoRaz=6

arrSize = 999999
arr = []
for i in range(0,arrSize):
    arr.append(rnd.randint(0,999999))
print(arr,len(arr))


arrRaz=[]
for i in range(1,colvoRaz+1):
    arrRaz.append(10**i)    
#print(arrRaz)
    
    
arrSort = []
for i in range (0,10):
    arrSort.append([])    
#print(arrSort)


for j in range(arrSize):
    arrSort[int(str(arr[j])[-1])].append(arr[j])   
#print(arrSort,len(arrSort))      


dublicat=[]
for i in range(colvoRaz-2,-1,-1):
    dublicat=[[],[],[],[],[],[],[],[],[],[]]
    for j in range(0,10):
        for k in range(len(arrSort[j])):
            chislo=str(arrSort[j][k])
            if len(chislo) < colvoRaz:
               raznica = colvoRaz-len(chislo)
               chislo='0'*raznica+chislo
            dublicat[int(chislo[i])].append(int(chislo))           
    arrSort=dublicat
print(sum(arrSort,[]),len(sum(arrSort,[])),len(arr)) 
            
            
            
            
            
            
            