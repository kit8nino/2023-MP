#
#Совместно с Фадин Владислав (Vortexcrab)
#
import random

#print(random.sample(range(1, 18), 4))      #11, 4, 10, 3
# int/float/compl_size я сделал маленьким, тк программа заполняет эти списки по 7-10 минут
# Когда запускал все сортировки сразу, ядро ломалось на сортировке вставками с s3_word_list
int_list = []
float_list = []
compl_list = []
word_list = []

birth_day = 24
birth_month = 9
r = birth_day / birth_month
#print(r)


# целые парни
int_size = 100 # количество целых чисел
int_list = [random.randint(0, 999999) for i in range(int_size)] 
#print(int_list)


# вещественные парни
float_size = 100 # количество вещественных чисел
float_list = [random.uniform(-1, 1) for _ in range(float_size)] 
#print('\n',float_list)


# комплексные парни
compl_size = 100 # количество комплексных чисел
for i in range(compl_size):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    z = complex(x, y)
    
    while abs(z) > r:
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = complex(x, y)
    compl_list.append(z)

# abs_compl_list = []
# for i in range(len(compl_list)):
#     a = abs(compl_list[i])
#     abs_compl_list.append(a)
# abs_compl_list.sort()
# #print(abs_compl_list)

# new_compl_list = []
# for i in range(len(compl_list)):
#     for j in range(len(compl_list)):
#         if (abs(compl_list[i]) == abs_compl_list[j]):
#             new_compl_list.append(compl_list[i])
#print(new_compl_list)


# отрывок из книги
with open('metro.txt', 'r') as file:
    word_list = file.read().split()
#print(word_list)
for i in range(len(word_list)):
    word_list[i] = word_list[i].replace("–", "").replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("«", "").replace("»", "").replace("…", "").replace("(", "").replace(")", "")
word_list = list(filter(None, word_list))
#print(word_list)


# -----------------Сортировка расчёской-----------------
def sort_ras(listt):
    sz = len(listt)
    gap = sz
    koef = 1.247
    sorted = False
    while not sorted:
        gap  = int(gap/koef)
        if gap <= 1:
            gap = 1
            sorted = True
        count = 0
        while count + gap < sz:
            if listt[count] > listt[count + gap]:
                listt[count], listt[count+gap] = listt[count+gap], listt[count]
                sorted = False
            count += 1
    return listt
# Сортировка расчёской для комплексных парней
def sort_ras_compl(listt):
    sz = len(listt)
    gap = sz
    koef = 1.247
    sorted = False
    while not sorted:
        gap  = int(gap/koef)
        if gap <= 1:
            gap = 1
            sorted = True
        count = 0
        while count + gap < sz:
            if abs(listt[count]) > abs(listt[count + gap]):
                listt[count], listt[count+gap] = listt[count+gap], listt[count]
                sorted = False
            count += 1
    return listt

s1_int_list = int_list
s1_float_list = float_list
s1_compl_list = compl_list
s1_word_list = word_list

print(sort_ras(s1_int_list))
print(sort_ras(s1_float_list))
print(sort_ras_compl(s1_compl_list))
print(sort_ras(s1_word_list))

print('------------------------------------------------------------------------------------------------------')
# -----------------Сортировка вставками-----------------
def sort_insert(listt):
    for i in range(1, len(listt)):
        key = listt[i]
        j = i - 1
        while j >= 0 and key < listt[j]:
            listt[j + 1] = listt[j]
            j -= 1
        listt[j + 1] = key
    return listt
# Сортировка вставками для комплексеных парней
def sort_insert_compl(listt):
    for i in range(1, len(listt)):
        key = listt[i]
        j = i - 1
        while j >= 0 and abs(key) < abs(listt[j]):
            listt[j + 1] = listt[j]
            j -= 1
        listt[j + 1] = key
    return listt

s2_int_list = int_list
s2_float_list = float_list
s2_compl_list = compl_list
s2_word_list = word_list

print(sort_insert(s2_int_list))
print(sort_insert(s2_float_list))
print(sort_insert_compl(s2_compl_list))
print(sort_insert(s2_word_list)) #довольно долго выполняет

print('------------------------------------------------------------------------------------------------------')
# -----------------Быстрая сортировка-----------------
def sort_quick(listt):
    if len(listt) <= 1:
        return listt
    
    elem = listt[0]
    left = list(filter(lambda x: x < elem, listt))
    right = list(filter(lambda x: x > elem, listt))
    center = list(filter(lambda x: x == elem, listt))
    
    return sort_quick(left) + center + sort_quick(right)
# Быстрая сортировка для комплексеных парней
def sort_quick_compl(listt):
    if len(listt) <= 1:
        return listt
    
    elem = listt[0]
    left = list(filter(lambda x: abs(x) < abs(elem), listt))
    right = list(filter(lambda x: abs(x) > abs(elem), listt))
    center = list(filter(lambda x: abs(x) == abs(elem), listt))
    
    return sort_quick_compl(left) + center + sort_quick_compl(right)
s3_int_list = int_list
s3_float_list = float_list
s3_compl_list = compl_list
s3_word_list = word_list

print(sort_quick(s3_int_list))
print(sort_quick(s3_float_list))
print(sort_quick_compl(s3_compl_list))
print(sort_quick(s3_word_list)) 

print('------------------------------------------------------------------------------------------------------')
#-----------------Сортировка слиянием-----------------
def tolist(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c

def sort_merge(listt):
    if len(listt) == 1:
        return listt
    center = len(listt)//2
    left = sort_merge(listt[:center])
    right = sort_merge(listt[center:])
    return tolist(left, right)
# Сортировка слиянием для комплексеных парней
def comp_tolist(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if abs(a[i]) < abs(b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c

def compl_sort_merge(listt):
    if len(listt) == 1:
        return listt
    center = len(listt)//2
    left = compl_sort_merge(listt[:center])
    right = compl_sort_merge(listt[center:])
    return comp_tolist(left, right)

s4_int_list = int_list
s4_float_list = float_list
s4_compl_list = compl_list
s4_word_list = word_list

print(sort_merge(s4_int_list))
print(sort_merge(s4_float_list))
print(compl_sort_merge(s4_compl_list))
print(sort_merge(s4_word_list)) 






















