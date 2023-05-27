# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:36:19 2023

@author: Кирилл
"""

import random
import math
import string

#**********Блок исходных данных*********#

#список целых чисел от 0 до 999999
list_of_int = [i for i in range(1000000)]
random.shuffle(list_of_int)
#print('Список целых чисел от 0 до 999999:', list_of_int)
print('                           ')

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
list_of_real = [random.uniform(-1,1) for i in range(10000)]
#print('Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:', list_of_real)
print('                           ')

#42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса 
#r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю числа
birth_day = 25 
birth_month = 6
r = birth_day / birth_month
n=42000
def PointsInCircum(r,n):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
list_of_complex = PointsInCircum(r,n)
random.shuffle(list_of_complex)
#print('Точки комплексной плоскости:', list_of_complex)
print('                           ')

#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
file = 'text.txt'
excerpt = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            excerpt.append(i.strip(string.punctuation))
#print('Отрывок из книги:', excerpt[:10000])


#**********Задания*********#

#Выбор четырех алгоритмов, которые будут использованы:
#print('Выбранные сортировки:', random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне
#Выбранные сортировки: 5,7,2,10

#5. Shellsort, сортировка Шелла
def Shell_sort(_list_):
    n = len(_list_)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            j = i
            while j >= step and _list_[j] < _list_[j-step]:
                _list_[j], _list_[j-step] = _list_[j-step], _list_[j]
                j = j - step
        step = step // 2
    return _list_
print('Загрузка...')
print('Отсортированный список целых чисел от 0 до 999999 сортировкой Шелла:\n', Shell_sort(list_of_int) )

#7. Gnome sort, гномья сортировка
def Gnome_sort(_list_):
    length = len(_list_)
    i = 1
    while i < length:
        if _list_[i-1] <= _list_[i]:
            i += 1
        else:
            a = _list_[i]
            _list_[i] = _list_[i-1]
            _list_[i-1] = a
            i -= 1
            if i == 0:
                i = 1
    return _list_
print('Загрузка...')            
print('Отсортированный список из 99999 случайных вещественных чисел в диапазоне [-1, 1] гномьей сортировкой:\n', Gnome_sort(list_of_real))

#2. bubble sort, сортировка пузырьком

def bubble_sort(_list_):
    n = len(_list_)
    for i in range(n):
        for j in range(n-i-1):
            if _list_[j] > _list_[j+1]:
                _list_[j], _list_[j+1] = _list_[j+1], _list_[j]
    return _list_

print('Загрузка...')
print('Отсортированный список из 42000 разных точки комплексной плоскости сортировкой пузырьком:\n', bubble_sort(list_of_complex) )

#10. Quicksort, быстрая сортировка
def Quick_sort(_list_):
    right_list = []
    left_list = []
    midl_list = []
    c = int(len(_list_) / 2)
    for i in range(len(_list_)):
        if _list_[i] < _list_[c]:
            left_list.append(_list_[i])
        elif _list_[i] > _list_[c]:
            right_list.append(_list_[i])
        else:
            midl_list.append(_list_[i])
    if all(_list_[i] < _list_[i+1] for i in range(len(_list_)-1)):
        return left_list + midl_list + right_list
    return Quick_sort(left_list) + midl_list + Quick_sort(right_list)

print('Загрузка...')
print('Отсортированный отрывок из книги быстрой сортировкой:\n', bubble_sort(excerpt[:10000]) )
























