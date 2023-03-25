#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
import string

# исходные данные
integers = [i for i in range(1000)]
random.shuffle(integers)

random_real = [random.uniform(-1,1) for i in range(1000)]

r = 1/11
n=1000
def PointsInCircum(r,n):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
points_in_circum = PointsInCircum(r,n)

file = 'book.txt'
book =[]
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            book.append(i.strip(string.punctuation))

# действия
#print(random.sample(range(1, 18), 4)) # => [7, 8, 1, 2]

#7.Gnome sort, гномья сортировка
def gnome_sort(seq):
    index = 1
    i = 0
    n = len(seq)
    while i < n-1:
        if seq[i] <= seq[i+1]:
            i, index = index, index + 1
        else:
            seq[i], seq[i+1] = seq[i+1], seq[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1

#8.selection sort, сортировка выбором
def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq

#1.shaker sort, сортировка перемешиванием
def shaker_sort(seq):
    l = 0 #left
    r = len(seq) - 1 #right
    control = r 
    while l < r:
        for i in range(l, r):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                control = i
        r = control
        for i in range(r, l, -1):
            if seq[i] < seq[i-1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
                control = i
        l = control
        
#2.bubble sort, сортировка пузырьком
def bubble_sort(seq):
    n = len(seq)
    for i in range(n):
        for j in range(n-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

# использование сортировок
sequence = []

print("gnome sort:")
print("до сортировки:", integers)
sequence = integers
sort = gnome_sort(sequence)
print("после сортировки:", sequence, "\n")

print("selection sort:")
print("до сортировки:", random_real)
sequence = random_real
sort = selection_sort(sequence)
print("после сортировки:", sequence, "\n")

print("shaker sort:")
print("до сортировки:", points_in_circum)
sequence = points_in_circum
sort = shaker_sort(sequence)
print("после сортировки:", sequence, "\n")

print("bubble sort:")
print("до сортировки:", book[:10000])
sequence = book[:10000]
sort = bubble_sort(sequence)
print("после сортировки:", sequence)


# In[ ]:




