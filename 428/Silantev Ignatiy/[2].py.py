#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
import string

# Сортировки
# 12 
# 2
# 13
# 8
# https://habr.com/en/post/335920/


# (12) Counting sort - это алгоритм сортировки, который работает 
# путем подсчета количества каждого элемента в массиве и затем использует 
# эту информацию для расположения элементов в отсортированном порядке.
# В коде выше мы создаем массив count длиной m, где m равно максимальному 
# значению в массиве arr плюс 1. Затем мы проходим по массиву arr и 
# увеличиваем значение в соответствующем индексе массива count на 1 для 
# каждого элемента в arr. Затем мы проходим по массиву count и используем 
# информацию о количестве каждого элемента для расположения элементов 
# в отсортированном порядке.

def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

arr = list(range(100))
result1 = counting_sort(arr)
print("1) ", result1)
print(" ")
        
# (2) Конечно! Этот код реализует алгоритм сортировки пузырьком. 
# Сначала он создает список из 100 случайных чисел в диапазоне от -1 до 1 
# с помощью генератора списка и функции random.uniform. Затем этот список 
# передается в функцию bubblesort, которая сортирует его в порядке возрастания.
# Функция bubblesort принимает список в качестве аргумента и сортирует его 
# путем сравнения каждого элемента со следующим и обмена их местами, если они 
# находятся в неправильном порядке. Этот процесс повторяется до тех пор, 
# пока все элементы не будут отсортированы. В конце функция возвращает 
# отсортированный список.

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [random.uniform(-1, 1) for i in range(100)]
result2 = bubblesort(arr)
print("2) ", result2)
print(" ")


# (13) Bucket sort - это алгоритм сортировки, который работает путем 
# распределения элементов в массиве по “ведрам” или “корзинам”, 
# а затем сортирует элементы в каждом ведре отдельно. создает 42000 разных 
# точек комплексной плоскости, лежащие внутри окружности 
# радиуса r = birth_day / birth_month, и сортирует их по модулю 
# числа с использованием метода Bucket sort:

birth_day = 13
birth_month = 11
r = birth_day / birth_month

def bucket_sort(arr):
    max_val = max([abs(x) for x in arr])
    size = max_val/len(arr)
    buckets = [[] for k in range(len(arr))]
    for i in range(len(arr)):
        j = int(abs(arr[i])/size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr)-1].append(arr[i])
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i], key=abs)
    result = []
    for i in range(len(arr)):
        result += buckets[i]
    return result

arr = []
while len(arr) < 100:
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if math.sqrt(x**2 + y**2) <= r:
        arr.append(complex(x,y))

result3 = bucket_sort(arr)
print("3) ", result3)
print(" ")


# (9) Конечно! Heapsort - это алгоритм сортировки, который использует 
# структуру данных под названием “куча” для сортировки элементов. Он 
# работает путем создания максимальной кучи из входного массива и затем 
# извлечения максимального элемента из кучи и помещения его в конец 
# отсортированного массива. Этот процесс повторяется до тех пор, 
# пока все элементы не будут отсортированы.

file = '2.txt'
book = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            book.append(i.strip(string.punctuation))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

text = book[:1000]
heapSort(text)
print("4) ", text)


# In[ ]:




