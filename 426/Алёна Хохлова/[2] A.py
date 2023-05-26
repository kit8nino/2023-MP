#!/usr/bin/env python
# coding: utf-8

# In[33]:


import random
import math
import re

### Исходные данные

#Список целых чисел от 0 до 999999(Задаем и перемешиваем)
numbers = [i for i in range(999999)]
random.shuffle(numbers)

#Список из случайных вещественных чисел в диапазоне от -1 до 1
rnumbers = [random.uniform(-1, 1) for _ in range(99999)]

#42000 точки на комплексной площади(случайные)

day = 16
month = 9
radius = day / month 

complexpoints = []

while len(complexpoints) < 42000:
    x = random.uniform(-radius, radius) #Случайное значение для x
    yr = math.sqrt(radius**2 - x**2) #находим максимальное и минимальное значение y
    y = random.uniform(-yr, yr)
    
    point = complex(x, y)
    complexpoints.append(point)

#Отрывок из книги, разбитый в список по словам.(Книга - "Квентин Дорвард"(Quentin Durward) за автортсвом Вальтера Скотта)

book = 'book.txt'
with open(book, 'r', encoding='utf-8') as file:
    text = file.read()
    wordlist = re.findall(r'\b[A-Za-z]+\b', text)
    
### Действия
# путем использования random.sample(range(1, 18), 4) были получены следующие алгоритмы сортировки:
#  Shaker Sort(1), Selection Sort(8), QuickSort(10), Least Significant Digit(15)


#Shaker Sort для чисел (0, 999999).
#Суть в том, чтобы идти не только слева направо, но и справа налево. Продолжается пока указатели "лево" и "право" не пересекутся. 
#Асимптотика: в худшем и среднем случаях O(n^2), в лучшем O(n)
    
def shaker(numbers):
    left = 0
    right = len(numbers) - 1
    swap = True
    
    while left < right and swap:
        swap = False
        
        for i in range(left, right): #Идем справа налево
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap = True
                
        right -= 1
        
        if not swap: #Сортировка завершается если не было перестановки
            break
            
        for i in range(right, left, -1): #Идем слева направо
            if numbers [i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                swap = True
        left +=1
    return numbers

sorted_numbers = shaker(numbers)
print("Отсортированные числа: ", sorted_numbers)

#Selection Sort для 99999 чисел в диапазоне [-1, 1].
#Суть в том, чтобы на каждой итерации находить минимум в массиве после текущего элемента и менять их местами
#После i-ой итерации, i первых элементов стоят на своих местах
#Асимптотика во всех случаях O(n^2)

def selection(rnumbers):
    n = len(rnumbers)
    
    for i in range(n): #Задаем текущий индекс как минимальный
        mini = i
        
        for j in range(i+1, n): #Ищем индекс минимального элемента в оставшейся части массива
            if rnumbers[j] < rnumbers[mini]:
                mini = j
                
        rnumbers[i], rnumbers[mini] = rnumbers[mini], rnumbers[i] #меняем их местами
        
    return rnumbers

sorted_rnumbers = selection(rnumbers)
print("Отсортированные вещественные числа: ", sorted_rnumbers)

#Quicksort для комплексных точек.
#Идея заключается в выборе "опорного" элемента и разделении массива на элементы меньши и большие
# проходим по всем элементам и помещаем в соответствующие массивы.
#Асимптотика: O(nlogn) в среднем и лучшем случаях. При неудачном выборе элемента возможно O(n^2)
#Комплексные числа сортируем по их модулю.

def quicksort(points):
    pivot = points[len(points) // 2] # задаем опорный элемент
    le, eq, gr = [], [], [] #списки для разделения массива
    
    for point in points:
        if abs(point) < abs(pivot):
            le.append(point)
        elif abs(point) == abs(pivot): # на случай существования такой же точки
            eq.append(point)
        else:
            gr.append(point)
    
    return quicksort(le) + eq + quicksort(gr) if le and gr else le + eq + gr 

sorted_complex_numbers = quicksort(complexpoints)
print("Отсортированные комплексные точки: ", sorted_complex_numbers )

#Least Significant Digit для сортировки слов
#Сортируем слова, начиная с младших позиций(least significant digit) и двигаемся к старшим.
#Асимптотика: O(n)


def least_sd(words):
    max_len = max(len(word) for word in words)
    
    for i in range(max_len -1, -1, -1):
        buckets = [[] for k in range(256)]
        
        for word in words:
            if i < len(word):
                letter = ord(word[i])
                buckets[letter].append(word)
            else:
                buckets[0].append(word)
                
        word_list = []
        for bucket in buckets:
            word_list.extend(bucket)
            
    return word_list


    
    
    
    
sorted_words = least_sd(wordlist)
print("Отсортированные слова: ")
for word in sorted_words:
    print(word)




# In[ ]:





# In[ ]:




