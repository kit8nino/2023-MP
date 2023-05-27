#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import copy
import random as rn
numbers_compl=[]
while len(numbers_compl)<42000:
    coef=rn.uniform(0,3/4)
    compl_numb=complex(coef,coef)
    numbers_compl.append(compl_numb)

simple_numbers=np.linspace(0,99999,100000)  
small_numbers=np.linspace(-1,1,1000000) 
with open('Внимание_Аннекдоты.txt', 'r', encoding='utf-8') as file: 
    data = file.read().replace('\n', ' ')
    words = data.split()
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)] 
    for num in arr:
        bucket_index = int(num ) 
        buckets[bucket_index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket) 
    return sorted_arr

def gnome_sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        if arr[i-1] <= arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            if i > 1:
                i -= 1
    return arr

def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        j = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[j] = i
                j += 1

        placement *= RADIX

    return arr

def comp_sort(arr, key=lambda a: a):
    n = len(arr)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and key(temp) < key(arr[j - gap]):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def gnome_sort_compl(arr):
    n = len(arr)
    i = 1
    while i < n:
        if (arr[i-1].real**2+arr[i-1].imag**2)**(1/2) <= (arr[i].real**2+arr[i].imag**2)**(1/2):
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            if i > 1:
                i -= 1
    return arr

sort1=gnome_sort_compl(numbers_compl)
sort2=bucket_sort(simple_numbers)
sort3=radix_sort(small_numbers)
sort4=comp_sort(words)
print(sort1)
print(sort2)
print(sort3)
print(sort4)

