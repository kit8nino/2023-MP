import numpy as np
import random as rand
import math as mat
import string

celie_chisla=[]
for i in range(0,9999):
    celie_chisla.append(i)

vehestvennie_chisla=[]
for i in range(0,9999):
    vehestvennie_chisla.append(rand.uniform(-1,1))
    
b_dan=29
b_mesac=1
r=b_dan/b_mesac
plockost_chisla=[]
n=42000
def plockostchisla(r,n):
    return [(float(mat.cos(2*mat.pi/n*x)*r),float(mat.sin(2*mat.pi/n*x)*r)) for x in range(0,n+1)]
plockost_chisla = plockostchisla(r,n)
rand.shuffle (plockost_chisla)


slova = []
with open('Книга.txt', encoding='utf-8') as file:
    for line in file:
        for i in (line.split(" ")):
            if i != '\n' :
                slova.append(str(i))
book=slova[:10000]

#print(rand.sample(range(1, 18), 4) )
#[10, 3, 9, 4]


                                               #10
def bubble_sort(nums):  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# Проверяем, что оно работает
random_list_of_nums = celie_chisla
bubble_sort(random_list_of_nums)  
print("#10")
print(random_list_of_nums)

                                          #3
ls = vehestvennie_chisla
n = len(ls)
step = n
while step > 1 or flag:
   if step > 1:
       step -= 1
   flag, i = False, 0
   while i + step < n:
      if ls[i] > ls[i + step]:
          ls[i], ls[i + step] = ls[i + step], ls[i]
          flag = True
      i += step
print("#3")
print(*ls)

                                          #9
def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
 
alist = plockost_chisla
heapsort(alist)
print("#9")
print(alist)

                                          #4
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
alist = book
insertion_sort(alist)
print("#4")
print(alist)