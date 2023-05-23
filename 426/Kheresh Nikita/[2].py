#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random
import cmath
import numpy as np


Number_list=[]
for i in range(100):
    Number_list.append(i)
random.shuffle(Number_list)

random_list_of_real = [random.uniform(-1,1) for i in range(100)]

R=21/4

MAX=(R**(2)/2)**(0.5)
complex_list=[]
for i in range(100):
    Re=np.random.uniform(-MAX,MAX)
    Im=np.random.uniform(-MAX,MAX)
    complex_list.append(complex(Re,Im))
lenght=len(complex_list)
start = 0
end = lenght - 1

with open("book.txt",encoding='utf-8') as textfile:
    text = textfile.read().lower()
words = text.split()


def selection_sort(numbers):
    lenght=len(numbers)
    while lenght>0:
        MAX=Number_list[0]
        for i in range(lenght):
            if Number_list[i]<MAX:
                MAX=numbers[i]
        numbers.remove(MAX)
        numbers.append(MAX)
        lenght-=1
    return numbers


def quick_sort(array):
    
    if len(array) <= 1:
        return array
    
    elem = array[0]
    left = list(filter( lambda x: x<elem, array))
    center = [i for i in array if i == elem]
    right = list(filter(lambda x: x>elem, array))

    return quick_sort(left) + center + quick_sort(right)

def shaker_sort(complex_list, start, end):
    while start <= end:
   
        for i in range(start,end, 1):
         
            if abs(complex_list[i]) > abs(complex_list[i + 1]):
                a=complex_list[i]
                complex_list[i] =complex_list[i+1]
                complex_list[i+1] =a
        end -= 1 
        for i in range(end, start, -1):
        
            if abs(complex_list[i - 1]) > abs(complex_list[i]):
                a=complex_list[i]
                complex_list[i] = complex_list[i-1]
                complex_list[i-1] =a
        start += 1 
        return complex_list

def bubble_sort(content):
    for i in range(len(content)):
        for j in range(0, len(content) - i - 1):
            if len(content[j]) > len(content[j + 1]):
                content[j], content[j + 1] = content[j + 1], content[j]
    return content

sortedint = selection_sort(Number_list)
print(sortedint)

sortedreal = quick_sort(random_list_of_real)
print(sortedreal)

sorted_complex = shaker_sort(complex_list, start, end)
print(sorted_complex)

sorted_book = bubble_sort(words)
print(sorted_book)


# In[ ]:




