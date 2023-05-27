
import string
import random
import numpy as np
N=100000
#import random
#print(random.sample(range(1, 18), 4)) --> [10, 11, 8, 6]
#6) --> tree sort, сортировка деревом
#8) --> selection sort, сортировка выбором
#10) --> Quicksort, быстрая сортировка
#11) --> Merge sort, сортировка слиянием

mas_int = [i for i in range(N)] #массив целых чисел от 0 до 999999
mas_rand = [random.random()*(1+1)-1 for i in range(N)] #999999 случайных чисел от -1 до +1
r = 8/8
mas_complex=[]
mas_abs_complex=[]
k=0
while k < 42000:
    
    a = random.random()*r
    b = random.random()*r
    if abs(complex(a, b))<r:
        mas_complex.append(complex(a,b))
        mas_abs_complex.append(abs(complex(a, b)))
        k+=1
    
words=[]
file = open('Malenkiy_princ.txt')
for row in file:
    
    row_no_punct = row.translate(str.maketrans('', '', string.punctuation))
    s = row_no_punct[:-1].split(' ')
    for word in s:
        if word =='':
            continue
        words.append(word)
words = words[:N] #100000 слов из книги
# ---------------------- сортировка деревом -----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.count=[]
 
 
class Tree:
    def __init__(self):
        self.root = None
 
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
 
        if value == node.data:
            return node, parent, True
 
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
 
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
 
        return node, parent, False
 
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
 
        s, p, fl_find = self.__find(self.root, None, obj.data)
 
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
 
        return obj

    def show_tree(self, node):
        if node is None:
            return
        
        self.show_tree(node.right)
        
        print(node.data)
        
        self.show_tree(node.left)
# ----------------------- сортировка выбором ---------------------
def viborsort(datalist):
   for i in range(len(datalist)):
       for j in range(i, len(datalist)):
           if datalist[j] < datalist[i]:
               t = datalist[j]
               datalist[j]=datalist[i]
               datalist[i]=t
   return datalist
# ---------------------- сортировка слиянием ---------------

def merge_sort(datalist, start, end):
    mid = (start + end)//2
    if end - start > 1:
        
        merge_sort(datalist, start, mid)
        merge_sort(datalist, mid, end)
        merge_list(datalist, start, mid, end)
 
def merge_list(datalist, start, mid, end):
    left = datalist[start:mid]
    right = datalist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            datalist[k] = left[i]
            i = i + 1
        else:
            datalist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            datalist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            datalist[k] = right[j]
            j = j + 1
            k = k + 1
    return datalist


# ---------------------- быстрая сортировка ---------------


def quicksort(datalist):
    if len(datalist)<1:
        return datalist
    point = datalist[0]
    left = list(filter(lambda x: x<point, datalist))
    right = list(filter(lambda x: x>point, datalist))
    middle = [i for i in  datalist if i==point]
    return quicksort(left) + middle + quicksort(right)



#выбор сортировки
print("6) --> tree sort, сортировка деревом\n", 
"8) --> selection sort, сортировка выбором\n", 
"10) --> Quicksort, быстрая сортировка\n"
"11) --> Merge sort, сортировка слиянием\n")
ind = int(input("Введите номер сортирвки (по порядку) "))
if ind ==6 :
    print("\nСОРТИРОВКА ДЕРЕВОМ: \nМодуль комплексных чисел")
    t = Tree()
    for x in mas_abs_complex:
       t.append(Node(x))
    t.show_tree(t.root)
    ind = int(input("Введите номер сортирвки (8, 10, 11)"))
if ind ==8 :
    print("\nСОРТИРОВКА ВЫБОРОМ: \nОтрывок из книги")
    print(viborsort(words)) 
    ind = int(input("Введите номер сортирвки (10, 11)"))
if ind == 10:  
    print("\nБЫСТРАЯ СОРТИРОВКА: \n рандомные числа --->")
    print(quicksort(mas_rand))
    ind = int(input("Введите номер сортирвки (11)"))
if ind == 11:
    print("\nСОРТИРОВКА СЛИЯНИЕМ: \nСлучайные числа  --->")
    merge_sort(mas_rand, 0, len(mas_rand))
    print( mas_rand)
else:
    print("Завершено")