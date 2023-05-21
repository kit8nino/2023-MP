#[2] Алгоритмы сортировки

import random
import numpy as np
import re
#int_list = list(range(0,385000))#(0,999999)) #1  (больше этого числа jupyter ошибку выдает, но разницы особой нет)
n = 1000000
int_list = [random.randint(0,n-1) for i in range(n)]
float_list = [random.uniform(-1, 1) for i in range(99999)] #2
r = 1.125 #birth_day / birth_month (9 / 8 =1.125)
pts = [] #3
for i in range(42000):
    p = np.random.rand() * r * np.exp(2j * np.pi * np.random.rand())
    pts.append(p)
sorted_points_list = sorted(pts, key=np.abs)
with open("uzhas_danvicha.txt", 'r') as file:
    text = file.read()
words = re.split(r'\W+', text)
words_list = [] #4
for word in words:
    if word != '':
        words_list.append(word)

random_sample = random.sample(range(1, 18), 4) #[7, 11, 1, 8]
print('выполняется')

# ГНОМЬЯ СОРТИРОВКА 7
def sort_gnom(arr):
    l=len(arr)
    i=1
    while i<l:
        if arr[i-1]<=arr[i]:
            i+=1
        else:
            a=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=a
            i-=1
            if i==0:
                i=1
    return print(arr)
sort_gnom(int_list)

# СОРТИРОВКА СЛИЯНИЕМ 11
def sort_slianiem(arr):
    l = len(arr) // 2
    arr1 = arr[:l]     
    arr2 = arr[l:]
    if len(arr1) > 1:
        arr1 = sort_slianiem(arr1)
    if len(arr2) > 1:
        arr2 = sort_slianiem(arr2)
    i,j,arr = 0,0,[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    arr += arr1[i:] + arr2[j:]
    return arr
#print(sort_slianiem(float_list))

# СОРТИРОВКА ПЕРЕМЕШИВАНИЕМ 1
def sort_peremesh(arr):
    l = len(arr)
    f = 1
    start = 0
    end = l - 1
    while f == 1:
        f = 0
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f = 1
        if f == 0:
            break
        end -= 1
        f = 0
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f = 1
        start += 1
    return print(arr)
#sort_peremesh(pts)

# СОРТИРОВКА ВЫБОРОМ 8
def sort_viborom(arr):
    l=len(arr)
    while l>0:
        max=arr[0]
        for i in range(l):
            if arr[i]<max:
                max=arr[i]
        arr.remove(max)
        arr.append(max)
        l-=1
    return print(arr)
#sort_viborom(words_list)
print('выполнилось')
