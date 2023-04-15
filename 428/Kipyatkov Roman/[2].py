# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:40:39 2023

@author: Роман
"""
import random
import numpy as np
N=10**3
_0_1kk=[N-i-1 for i in range(N)]
rand_1kk=[random.random() for i in range(N)]
r=26/7
_42k=[]
_42k_abs=[]
for i in range(420):
    r=random.random()*26/7
    a=complex(r*np.cos(rand_1kk[i]),r*np.sin(rand_1kk[i]))
    _42k.append(a)
    _42k_abs.append(np.sqrt((r*np.cos(rand_1kk[i])*r*np.cos(rand_1kk[i]))+(r*np.sin(rand_1kk[i])*r*np.sin(rand_1kk[i]))))
filename="Толстой Лев. Война и мир. Том 1.txt"
r_file=[]
with open(filename) as f_input:
        list_data = f_input.read().split()
        list_data_words=[]
        for j in list_data:
            if 1040 <=ord(j[0]) and ord(j[0])<=1104:
                list_data_words.append(j)
print("число слов:",len(list_data_words))
print(list_data_words)
list_data_for_test=["Мне только справку отдать!","Кря","Гав-Гав","Му-Му","Мне только справку отдать","Лада Надежда","Й"]
#
print("[13, 8, 1, 10] -номера сортировок из функции: random.sample(range(1, 18), 4)")
#Блочная сортировка / Bucket sort
def bucket_sort(input_list):
    max_value = max(input_list) #Максимальное значение в массивые
    size = max_value/len(input_list)
    buckets_list= [] #Создание пустых блоков
    for x in range(len(input_list)):
        buckets_list.append([]) 
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

#Сортировка элементов внутри блока происходит сортировкой вставкой
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

sorted_list = bucket_sort(rand_1kk)
print("Блочная сортировка:  Отсортированный список вещественных чисел(Нажмите пробел чтобы увидеть):")
choise=input()
if choise==" ":
    print(sorted_list)

#selection sort, сортировка выбором;
def selection_sort(arr):
    for i in range(len(arr)):
        minz, ind = i, i
        for j in range(i, len(arr)):
            if arr[j] < arr[minz]:
                minz = j
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]
    return arr
print('')
print("Сортировка выбором: Отсортированный список слов(Space to show):")
choise=input()
if choise==" ":    
    print(selection_sort(list_data_words))

#shaker sort, сортировка перемешиванием;
def shaker_sort(input_array,array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, +1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                input_array[i],input_array[i + 1]=input_array[i + 1], input_array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                input_array[i],input_array[i - 1]=input_array[i - 1], input_array[i]
        left += 1
    return(input_array)
print('')
print("Сортировка перемешиванием: Отсортированный список комплексных чисел по модулю(Space to show):")
sorted_list=shaker_sort(_42k,_42k_abs)
choise=input()
if choise==" ":
    print(sorted_list)
print("")

    
#Quicksort, быстрая сортировка;
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
a={}
print("Быстрая сортировка: Отсортированный список чисел от 0 до 1кк(Space to show): ")
sorted_list=quicksort(_0_1kk)
choise=input()
if choise==" ":
    print(sorted_list)