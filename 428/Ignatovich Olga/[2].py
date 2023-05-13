import random
import math
import string
#print(random.sample(range(1, 18), 4))
# 5 2 10 13

# 10000+ слов из отрывка книги


file="Алиса в Стране Чудес.txt"
with open(file) as file_input:
        mas_book = file_input.read().split()

#Сортировка пузырьком для слов

for i in range(len(mas_book)-1):
    for j in range(len(mas_book)-i-1):
        if mas_book[j] > mas_book[j+1]:
            mas_book[j], mas_book[j+1] = mas_book[j+1], mas_book[j]
 
print(mas_book)

#Cписок из 99999 случайных вещественных чисел в диапазоне [-1, 1]

k=0
n=10000
a=[]
while k<n:
    a.append(random.uniform(-1, 1))
    k+=1
a=list(a)
print(a)


#Cортировка Шелла для вещественных чисел

def shellSort(a):
    h = len(a)//2
    while h > 0:
        for i in range(h):
            h_Sort(a,i,h)
        h = h // 2	
def h_Sort(a,j,h):
    for i in range(j+h,len(a),h):
        znach = a[i]
        k = i
        while k>=h and a[k-h]>znach:
            a[k]=a[k-h]
            k-=h
        a[k]=znach
	
shellSort(a)
print(a)



#42000 разных точкек комплексной плоскости, лежащие на окружности радиуса r = birth_day / birth_month

n=10000
r=21/10
b=[]

for i in range(n):
    g=[r*math.cos(2*math.pi/n*i),r*math.sin(2*math.pi/n*i)]
    b.append(g)
random.shuffle (b)
print(b)


#Быстрая сортировка / Quicksort для комплексных чисел


def dell(mass, l, h):
    pi=mass[h]
    i=l - 1
    for j in range(l, h):
        if mass[j]<= pi:
            i+= 1
            mass[i], mass[j] = mass[j], mass[i]
    mass[i + 1], mass[h]=mass[h], mass[i + 1]
    return i+1
 
 
def quickSort(mass, l, h):
    if l<h:
        pi = dell(mass, l, h)
        quickSort(mass, l, pi - 1)
        quickSort(mass, pi + 1, h)
 
quickSort(b, 0, len(b) - 1)
print(b)


#Список целых чисел от 0 до 999999
n=100000
listt = list(range(n))
random.shuffle (listt)

#Блочная сортировка

def insertSort(mass):
    for i in range(1, len(mass)):
        posl_el = mass[i]
        while i > 0 and mass[i-1] > posl_el:
            mass[i] = mass[i-1]
            i-=1
        mass[i] = posl_el


def Min_Max(mass):
    if len(mass) == 0:
        return [0, 0]
    min_max = [mass[0], mass[0]]
    for el in mass:
        if el < min_max[0]:
            min_max[0] = el
        if el > min_max[1]:
            min_max[1] = el
    return min_max


def bucketSort(mass, n):
    buc = []
    for i in range(n):
        buc.append([])
    min_max = Min_Max(mass)
    if(min_max[0] == min_max[1]):
        return
    for i in mass:
        buc[(n * (i - min_max[0])) //
                (min_max[1]-min_max[0]+1)].append(i)
    for b in buc:
        if(len(b) <= 32):
            insertSort(b)
        else:
            bucketSort(b, n)
    hhh = 0
    for b in buc:
        for i in b:
            mass[hhh] = i
            hhh += 1
bucketSort(listt,8)
print(listt)
