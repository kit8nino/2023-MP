#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

random.sample(range(1, 18), 4) # вернет список из 4 случайных значений в заданном диапазоне


# In[41]:


import random as rnd
import re # чтобы не мешали кавычки и знаки препинания.
import math

# 7 - gnome sort
# 13 - bucket sort
# 9 - Heapsort
# 15 - least significant digit

# Целые числа (0, 999999) и гномья сортировка.
# В худшем случае может потребовать времени, пропорционального квадрату размера списка(O(n^2)) (АДСКИ МНОГО)
numbers = list(range(1000000))
rnd.shuffle(numbers)

def gnome(arr):
    i = 0
    n = len(arr)
    
    while i<n:
        if i == 0 or arr[i - 1] <= arr[i]:
            i +=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            
    return arr

sorted_numbers = gnome(numbers)

print(sorted_numbers)

#99999 случайных действительных чисел в диапазоне [-1;1] и bucket sort.
#Время работы зависит от входных данных и количества блоков.
#Разбиваем массив на вёдра(блоки), сортируем каждое ведро, "собираем" числа из вёдер.
realNumbers = [random.uniform(-1, 1) for i in range (99999)]

def bucket(realNumbers):
    buckets_num = 10
    buckets = [[] for _ in range (buckets_num)]
    
    for number in realNumbers:
        ind = int((number + 1) * buckets_num / 2)
        buckets[ind].append(number)
        
    for bucket in buckets:
        bucket.sort()
        
    sorted_realNumbers = []
    for bucket in buckets:
        sorted_realNumbers.extend(bucket)
        
    return sorted_realNumbers

sorted_realNumbers = bucket(realNumbers)
print(sorted_realNumbers)

#42000 разных точки комплексной плоскости, лежащие внутри окружности, радиус которой равен отношению дня и месяца рождения, и Heapsort.
#гарантированно выполняется за O(nlogn) операций при сортировке n элементов.
#Необходимо выстроить элементы массива в виде сортирующего дерева, что требует O(n) операций, затем удалять элементы
# из корня по одному за раз и перестравивать дерево, пока в сортирующем дереве не останется 1 элемент, что требует O(nlogn) операций.
bday = 1
bmoth = 8
r = bday / bmoth

points = []
for i in range(42000):
    angle = random.uniform(0, 2*math.pi)
    
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    
    point = complex(x, y)
    points.append(point)

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and abs(arr[i]) < abs(arr[l]):
        largest = l
    
    if r < n and abs(arr[largest]) < abs(arr[r]):
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapsort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr
        
sorted_points = heapsort(points)
print(sorted_points)

#отрывок из книги, разбитый в список и least significant digit


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[A-Za-z]+\b', text) #убираем числа и отделяем слова от кавычек и знаков препинания, чтобы не получить в списке слов по типу ""hello!"
        return words
filename = 'book.txt'

words = read(filename)

def LSD(words):
    max_len = max(len(word) for word in words)
    
    for i in range(max_len -1, -1, -1):
        blocks = [[] for k in range(256)]
        
        for word in words:
            if i < len(word):
                letter = ord(word[i])
                blocks[letter].append(word)
            else:
                blocks[0].append(word)
                
        word_list = []
        for block in blocks:
            word_list.extend(block)
            
    return word_list

sorted_words = LSD(words)

print(sorted_words)




# In[ ]:




