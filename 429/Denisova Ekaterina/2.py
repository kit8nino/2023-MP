#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Делалось совместно с Дмитрием Прядко


import random
import numpy as np
#print(random.sample(range(1, 18), 4)) #-> 12,2,4,7

arr1 = np.random.randint(0,1000000,1000000)                                        # случайные целые числа
arr2 =  [np.random.uniform(-1,1) for i in range(99999)]                            # случайные вещественные числа от -1 до 1 

day = int(input("Ваш день рождения: "))
month = int(input("Ваш месяц рождения: "))                            

r = day / month                                                              # радиус окружности 

pn = [complex(random.uniform(-r, r), random.uniform(-r, r)) for i in range(42000)]   # точки комплексной плоскости ( на 42000 сортировал очень долго, на 1000 норм:))

with open("The Catcher in the Rye.txt", "r", encoding="utf-8") as f:                                       # отрывок из книги 
    text = f.read()
words = text[:-1].replace(',', '').replace('.', '').replace('«', '').replace('»', '').replace('?', '').replace('!', '').replace('-', '').replace('_', '').split()  

#12 Counting sort

def count_sort(arr):
    k=len(arr)
    count_arr = [0]*(k)                

    for i in arr:             
        count_arr[i]+=1

    index=0
    for i in range(k):                 
        while count_arr[i]>0:
            arr[index] =i
            index +=1
            count_arr[i] -=1
    return(arr)

print(count_sort(arr1))

#2 Bubble sort

def bubble_sort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr) - i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return(arr)

print(bubble_sort(arr2))

#4 insertion sort

def insert_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and abs(arr[j]) > abs(current): 
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current

    return arr

insertion = insert_sort(pn)
print(insertion)


#7 Gnome sort

def gnome_sort(arr):
    n = len(arr)
    i = 0

    while i + 1 < n:
        if arr[i + 1] >= arr[i]:
            i += 1
        else:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i -= 1 if i > 0 else  i + 1

    return(arr)

print(gnome_sort(words))




# In[ ]:




