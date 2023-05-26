import numpy as np
import random
import re

# Входные данные

int_spisok = list(range(1000000))
random.shuffle(int_spisok)

random_spisok = [random.uniform(-1.,1.) for i in range(99999)]

r = 9. / 4.
complex_spisok = [complex(random.uniform(-r, r), random.uniform(-r, r)) for i in range(42000)]
a = sorted(complex_spisok, key = abs)

with open("Text.txt",'r') as file:
    text = file.read()
words = re.findall(r'\b\w+\b', text)



random.sample(range(1, 18), 4) # [10, 14, 7, 2]

# Сортировки 



""" РАБОТАЕТ """

# 2

NumToSort = int_spisok

def LSD_sort(NumToSort):
    print(int_spisok)
    # Подготовка массива к сортировке
    max_len = len(str(max(NumToSort)))
   

    
    for i in range(max_len):
        spiski = [[] for k in range(10)]
        for j in NumToSort:
            i_razrad =  (j // 10**i)  % 10
            spiski[i_razrad].append(j)
            
        # Слияние списоков
        
        NumToSort = []
        for n in spiski: # Перебираем каждый список
            for m in n: # Перебираем числа в i-ом списке
                NumToSort.append(m)
    return NumToSort
            
   
        
    
    



# 1

nums = [[] for i in range(30)]
for i in words:
    nums[len(i)].append(i)
lens = []

for i in words:
    lens

def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or len(arr[i]) >= len(arr[i-1]):
            i += 1 
        else:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i -= 1
    return arr







def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



    
   
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        opora = arr[0]
        left = [x for x in arr[1:] if x < opora]
        right = [x for x in arr[1:] if x >= opora]
        return quicksort(left) + [opora] + quicksort(right)    

Moduls = []

for i in complex_spisok:
    Moduls.append((i.real)**2 + (i.imag)**2)    
    

 
    
def interface():
    v = int(input("1.Radix sort\n2.Gnome sort\n3.bubble_sort(долго)\n4.quicksort\n Ответ: "))
    if v == 1:
        print(LSD_sort(NumToSort))
        interface()
    elif v == 2:
        print(gnome_sort(words))
        interface()
    elif v == 3:
        print(bubble_sort(Moduls))
        interface()
    elif v == 4:
        res = quicksort(random_spisok)
        print(res)
        interface()
    
    
interface()   
    
    
    
    
 