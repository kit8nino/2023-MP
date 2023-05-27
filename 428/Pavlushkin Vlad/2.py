#!/usr/bin/env python
# coding: utf-8

# In[57]:


import random
import math
import string

# создание списка целых чисел от 0 до 999999
i_list = list(range(100000))

# создание списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
f_list = [random.uniform(-1, 1) for _ in range(99999)]

#42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых);
birth_day = 4
birth_month = 6
r = birth_day/birth_month
n=10000
def picircum(r,n):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
pointsc = picircum(r,n)
random.shuffle (pointsc)
print("Точки на комлексной плоскости:", pointsc)
#отрывок изfile = 'два капитана.txt'
file = 'два капитана.txt'
sp = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            k=sp.append(i.strip(string.punctuation))
#print("Отрывок из книги:", sp[:10000])
with open("два капитана.txt",encoding='utf-8') as textfile:
    text = textfile.read().lower()
tw = text.split()
print("Отрывок из книги:",tw)


# In[58]:


#Быстрая сортировка для целых чисел
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        greater_or_equal = [x for x in arr if x >= pivot]
        return quick_sort(less) + quick_sort(greater_or_equal)
print(quick_sort(i_list))    


# In[59]:


#Сортировка слиянием для вещественных чисел в диапазоне(-1,1)
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
print(merge_sort(f_list))


# In[60]:


def bubbles(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

sortedsh=bubbles(tw)
print(sortedsh)


# In[61]:


#сортировка выбором кточек на комплексной плоскости
def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selectionsort(pointsc))


# In[ ]:





# In[ ]:




