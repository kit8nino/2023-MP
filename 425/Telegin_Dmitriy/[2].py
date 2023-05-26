 #Исходные данные
import math
import random

numbers = list(range(0,10000)) #список целых чисел от 0 до 9999

r_l=[] #список из 10000 случайных вещественных чисел в диапазоне [-1, 1]
n=10000
for i in range(n):
    r_l.append(random.randint(-1,1))
    
r=24/12 # радиус окружности
c_p=[] # список комплексных точек
while len(c_p) != 5000:
    radius = random.uniform(0, r) #задаём диапазон значений радиуса окружности 
    angle = random.uniform(0, 2 * math.pi) #задаём диапазон значений углов окружности
    c_p.append([radius * math.cos(angle),
                           radius * math.sin(angle)])

spisok=[]
with open('book.txt', encoding='utf-8') as file:
    for line in file:
        for i in (line.split(" ")):
            if i != '\n' and len(spisok) < 10000:
                spisok.append(str(i))

#random.sample(range(1, 18), 4) 
#[1, 2, 4, 10] выпали методы: 1-сортировка перемешиванием; 2-сортировка пузырьком; 4-сортировка вставкой; 10-быстрая сортировка

                              #Сортировка перемешиванием
def coctail_sort(numbers):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        for i in range (left,right):
            if numbers[i] > numbers[i+1]:
                numbers[i] , numbers[i+1] = numbers[i+1], numbers[i]
        right-=1
       
        
        for i in range (right,left,-1):
            if numbers[i-1] > numbers[i]:
                numbers[i] , numbers[i-1] = numbers[i-1] , numbers[i] 
        left+=1
        return numbers
print('Сортировка перемешиванием:', coctail_sort(numbers))

                              #Сортировка пузырьком
def mySort(r_l):
    noSorted = True
    while noSorted:
        noSorted = False
        for i in range(0, len(r_l)-1):
            if (r_l[i] > r_l[i+1]):
                noSorted = True
                r_l[i], r_l[i+1] = r_l[i+1], r_l[i]       
    return r_l

print('Сортировка пузырьком:', mySort(r_l))

                              #Сортировка вставкой
    
def v_sort(c_p):
    for i in range(1, len(c_p)):
        while (i > 0 and c_p[i] < c_p[i-1]):
            c_p[i], c_p[i-1] = c_p[i-1], c_p[i]
            i -= 1
    return c_p

print('Сортировка вставкой:', v_sort(c_p))

                              #Быстрая сортировка
    
def partition(spisok, low, high):
    pivot = spisok[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while spisok[i] < pivot:
            i += 1

        j -= 1
        while spisok[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        spisok[i], spisok[j] = spisok[j], spisok[i]

def quick_sort(spisok):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(spisok, 0, len(spisok) - 1)


quick_sort(spisok)
print('Быстрая сортировка:', spisok)
