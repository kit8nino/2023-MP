import csv
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import math as mt
import random
#ЗАДАНИЕ №1(список целых чисел от 0 до 999999)(БЫСТРАЯ СОРТИРОВКА)
#изменяя n можно поменять количество чисел
n=10000
numbers=list(range(n))
random.shuffle(numbers)
print('НЕОТСОРТИРОВАННЫЙ СПИСОК = ',numbers)#НЕОТСОРТИРОВАННЫЙ СПИСОК
def quick_sort(numbers):
    if len(numbers)<=1:
        return numbers
    elem=numbers[0]
    left = list(filter(lambda x:x<elem,numbers))
    center = [i for i in numbers if i==elem]
    right = list(filter(lambda x:x>elem,numbers))
    return quick_sort(left)+ center +quick_sort(right)
print('ОТСОРТИРОВАННЫЙ СПИСОК = ',quick_sort(numbers))#ОТСОРТИРОВАННЫЙ СПИСОК
print('\n')

#ЗАДАНИЕ №2(список из 99999 случайных вещественных чисел в диапазоне [-1, 1])(СОРТИРОВКА ПУЗЫРЬКОМ)
numbers2=[random.uniform(-1, 1) for numbers2 in range(n)]
print('НЕОТСОРТИРОВАННЫЙ СПИСОК = ',numbers2)
print('************************************************')
for run in range(n-1):   
    for i in range (n-1):
        if numbers2[i]>numbers2[i+1]:
            numbers2[i],numbers2[i+1]=numbers2[i+1],numbers2[i]
print('ОТСОРТИРОВАННЫЙ СПИСОК = ',numbers2)

#Задание №3(42000 разных точек комплексной плоскости,лежащей внутри окружности)(МЕТОД РАСЧЁСТКИ)
count = 42000
birth_day=2
birth_month=7
R=birth_day/birth_month
r=[random.uniform(0, R) for r in range(count)]
phi=[random.uniform(0,2*mt.pi) for phi in range(count)]
a=[]

'''compl_onestring = [random.uniform(0, R) * 
                  (2.718281828**(1j*random.uniform(0, 6.28)))
                                 for x in range(42000)]'''
for i in range(count):
    a.append(r[i]*mt.cos(phi[i]))

b=[]
for i in range(count):
    b.append(r[i]*mt.sin(phi[i]))

compl=[]
for i in range(count):
    compl.append(complex(a[i],b[i]))

modul=[]
for i in range(count):
    modul.append(mt.sqrt((a[i])**2+(b[i])**2))

'''print(abs(compl_onestring[0]))'''

def comb_sort(modul):
    step = int(len(modul)/1.247)
    swap=1
    while step > 1 or swap > 0:
        swap = 0
        i=0
        while i+step<len(modul):
            if modul[i]>modul[i+step]:
                modul[i],modul[i+step]=modul[i+step],modul[i]
                swap+=1
            i = i + 1
        if step > 1:
            step = int(step/1.247)
comb_sort(modul)
print(modul)

#ЗАДАНИЕ №4(отрывок из книги разбитый в список по словам.)(insertion sort, сортировка вставкой)
file=open('Обломов..txt',encoding='utf8')
file.readline
massiv=file.read().split()   
def insertion_sort(massiv):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(massiv)):
        item_to_insert = massiv[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and massiv[j] > item_to_insert:
            massiv[j + 1] = massiv[j]
            j -= 1
        # Вставляем элемент
        massiv[j + 1] = item_to_insert

insertion_sort(massiv)
print((massiv))















        