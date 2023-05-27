#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Быстрая сортировка
import random

def quick(arr):
    if len(arr) <= 1:
        return arr
    p = arr[random.randint(0, len(arr) - 1)] # выбираю опорный элемент
    l = []  # списки для элементов
    e = []   # списки для элементов
    g = []   # списки для элементов
    
    for n in arr:      # распределяю элементы по спискам
        if n < p:
            l.append(n)
        elif n == p:
            e.append(n)
        else:
            g.append(n)
    return quick(l) + e + quick(g)  # рекурсивно сортируем списки меньших и больших элементов
arr = list(range(1000))  # созание списка целых чисел от 0 до 999999

random.shuffle(arr)  # перемешиваем список случайным образом
# сортируем список 
sort_arr = quick(arr)
print(sort_arr)






#Пузырьковый метод
import random

arr = [random.uniform(-1, 1) for i in range(999)] # список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
# Сортируем список 
for i in range(len(arr)):  #проходим по всем элементам списка
    for j in range(len(arr) - i - 1): # проходим по парам элементов соседних индексов
        if arr[j] > arr[j + 1]: #Если первый элемент пары больше второго элемента, то они меняются местами с помощью кортежей
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)





#Метод Шелла
import random
import math

# генерируем случайную точку внутри окружности заданного радиуса
def point(rad):
    r = rad * math.sqrt(random.uniform(0, 1))
    fi = random.uniform(0, 2 * math.pi)
    x = r * math.cos(fi)
    y = r * math.sin(fi)
    return complex(x, y)

# Генерируем список
rad = 22 / 5
p = [point(rad) for i in range(4200)]

# функция для сортировки
def sort(array):
    n = len(array)
    g = n // 2
    while g > 0:
        for i in range(g, n):
            t = array[i]
            j = i
            while j >= g and abs(array[j - g]) > abs(t):
                array[j] = array[j - g]
                j -= g
            array[j] = t
        g //= 2

sort(p)  # Сортируем точки
for k in p:  # Вывод точек
    print(k)
    

    
    
    
    
    #Сортиртирока текста гибридом    
def hybrid(words):
    if len(words) <= 1:
        return words

    # Разделение списка на две половины
    mid = len(words) // 2
    l_h = words[:mid]
    r_h = words[mid:]

    # Рекурсивная сортировка каждой половины
    l_h = hybrid(l_h)
    r_h = hybrid(r_h)

    # Слияние отсортированных половин
    sort = merge(l_h, r_h)

    return sort

def merge(l, r):
    m = []
    l_i = 0
    r_i = 0

    # Сравнение элементов из обеих половин и добавление их в результирующий список
    while l_i < len(l) and r_i < len(r):
        if l[l_i] < r[r_i]:
            m.append(l[l_i])
            l_i += 1
        else:
            m.append(r[r_i])
            r_i += 1

    # Добавление оставшихся элементов из левой половины
    while l_i < len(l):
        m.append(l[l_i])
        l_i += 1

    # Добавление оставшихся элементов из правой половины
    while r_i < len(r):
        m.append(r[r_i])
        r_i += 1

    return m

# Чтение текста из файла
file = 'м_и_м.txt'  

with open(file, 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()

sort = hybrid(words)
print(sort)


# In[ ]:




