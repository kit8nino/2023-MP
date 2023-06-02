#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random
import math
from pathlib import Path

#методы сортировки выбранные рандомом: 2,8,10,4
''' список целых чисел от 0 до 999999 '''
intg_num = np.random.randint(0,1000000,1000000)
''' список из 99999 случайных вещественных чисел в диапазоне [-1, 1] '''
real_num = []
for i in range(99999):
    real_num.append(random.uniform(-1, 1))

''' 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month 
(можно случайных, можно равномерно распределённых), сортировать по модулю числа '''
birth_day = 10
birth_month = 8
r = birth_day / birth_month

im_num = []
while len(im_num) < 42000:
    y = random.uniform(0, r)
    x = random.uniform(0, r)
    modl = np.sqrt(x**2 + y**2)
    if modl < r:
        im_num.append(complex(x, y))

''' отрывок из книги на 10000 слов, разбитый в список по словам '''
text = [i for i in Path('отрывок_книги.txt').read_text(encoding="utf-8").replace("\n", " ").split()]

# сортировка пузырьком

def b_sort(array):
    for i in range(1,len(array)):
        for k in range(len(array) - i):
            if array[k+1] < array[k]:
                array[k+1], array[k] = array[k], array[k+1]
    return(array)
print("сортировка пузырьком:\n" ,b_sort(intg_num))

# сортировка выбором

def select_sort(array):
    k = len(array)
    for i in range(k):
        n = i
        for j in range(i+1, k):
            if array[j] < array[n]:
                n = j
        array[i], array[n] = array[n], array[i]
    return array
print("сортировка выбором:\n",select_sort(real_num))

# быстрая сортировка
def quick_sort(array):
    num = array[len(array)//2] 
    a,b,c = [], [], [] 
    
    for i in array:
        if abs(i) < abs(num):
            a.append(i)
        elif abs(i) == abs(num): 
            b.append(i)
        else:
            c.append(i)
    
    return quick_sort(a) + b + quick_sort(c) if a and c else a + b + c 
print("быстрая сортировка:\n", quick_sort(im_num))

# сортировка вставкой

def insert_sort(array):
    for i in range(1, len(array)):
        t = array[i]
        j = i - 1
        while (j >= 0 and t < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = t
array=text        
print("сортировка вставкой:\n",insert_sort(array))

