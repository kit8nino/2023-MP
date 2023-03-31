import random
import math
import string

###########Исходные данные#################

#список целых чисел от 0 до 999999;
list_of_integers = [i for i in range(10000)]
random.shuffle (list_of_integers)
print("Список целых чисел:", list_of_integers)

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
random_list_of_real = [random.uniform(-1,1) for i in range(10000)]
print("Список случайных вещественных чисел:", random_list_of_real)

#42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых);
birth_day = 11 #11 число
birth_month = 11 #ноябрь
r = birth_day/birth_month
n=10000
def PointsInCircum(r,n):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
points_in_circum = PointsInCircum(r,n)
random.shuffle (points_in_circum)
print("Точки на комлексной плоскости:", points_in_circum)

#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
file = 'book.txt'
book = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            book.append(i.strip(string.punctuation))
print("Отрывок из книги:", book[:10000])

#################Действия######################

####Реализовать для каждого из исходных списков один из представленных алгоритмов сортировки####
####Выбор тех четырех алгоритмов, которые будут использованы конкретно у вас:#####
#print("Выбранные сортировки:", random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне
print("Выбранные сортировки: [5, 13, 2, 8] \n")

#----5.Shellsort, сортировка Шелла----#
    #1. Выбирается начальное значение шага сортировки. От выбора шага зависит средняя сложность сортировки.
    #2. Начиная от первого элемента выполняется сравнение элементов стоящих друг от
    #друга на расстоянии выбранного шага. Для значения элемента (в дальнейшем X)
    #выбирается место в последовательности таких элементов, что ai≤X≤ai+h,
    #где h - используемый шаг ai, ai+h - значение элемента на i индексе, и на i+h индексе соответственно.
    #3. После окончания прохода с текущим шагом, шаг уменьшают. Если текущий шаг равен
    #1 алгоритм заканчивают, если нет его уменьшают согласно выбранному закону его изменения и возвращаются к пункту 2.

def shell_sort(sequence):
    n = len(sequence)
    step = n//2
    while step > 0:
        for i in range(step, n):
            j = i
            while j >= step and sequence[j] < sequence[j-step]:
                sequence[j], sequence[j-step] = sequence[j-step], sequence[j]
                j = j - step
        step = step // 2
    print("Отсортированный список:", sequence)
        
#----13.Bucket sort, блочная (карманная) сортировка----#
    #1.Определяем значение минимального и максимального значения ключей сортировки.
    #Разбиваем полученный диапазон на нужное количество блоков(в дальнейшем n). Для этого нужно создать массив списков размером n.
    #2.Заполняем блоки данными из базовой последовательности. Для определения индекса блока используется функция соответствия.
    #3.Выполняем проход по полученным блокам. Если размер блока равен или меньше 32, провести его сортировку используя
    #сортировку вставкой (или любую иную оптимальную). Если размер больше то рекурсивно перейти к пункту 1.
    #4.Выполнить сборку отсортированных блоков в отсортированную последовательность.

#Функция для сортировки вставкой выше#
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        paste_element = sequence[i]
        while i > 0 and sequence[i-1] > paste_element:
            sequence[i] = sequence[i-1]
            i = i-1
        sequence[i] = paste_element

#Функция для поиска минимума и максимума#
def find_min_max(sequence):
    if len(sequence) == 0:
        return [0, 0]
    min_max = [sequence[0], sequence[0]]
    for element in sequence:
        if element < min_max[0]:
            min_max[0] = element
        if element > min_max[1]:
            min_max[1] = element
    return min_max

#Функция для блочной сортировки#
def bucket_sort(sequence, n):
    buckets = []
    for i in range(n):
        buckets.append([])
    min_max = find_min_max(sequence)
    if(min_max[0] == min_max[1]):
        return
    for element in sequence:
        buckets[(n * (element - min_max[0])) //
                (min_max[1]-min_max[0]+1)].append(element)
    for bucket in buckets:
        if(len(bucket) <= 32):
            insertion_sort(bucket)
        else:
            bucket_sort(bucket, n)
    insert_index = 0
    for bucket in buckets:
        for element in bucket:
            sequence[insert_index] = element
            insert_index += 1

#----2.Bubble sort, сортировка пузырьком----#
    #Сортировка пузырьком проходит по массиву несколько раз.
    #На каждом этапе алгоритм сравнивает два соседних элемента и,если левый элемент больше правого — меняет их местами.
    #Такой проход гарантирует что самое больше число будет в конце массива.
    #Этот процесс попарного сравнения повторяется до тех пор, пока каждый элемент не будет на своем месте.

def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n):
        for j in range(n-i-1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence

#----8.Selection sort, сортировка выбором----#
    #Основная идея — рассматривать последовательность как две части: первая включает отсортированные элементы, вторая — неотсортированные.
    #Алгоритм находит наименьшее число из неотсортированной части и помещает его в конец отсортированной.
def selection_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if sequence[j] < sequence[min_index]:
                min_index = j
        if min_index != i:
            sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
    return sequence

####Выбор списков и сортировок###
sequence = []
print("Выберите список, который хотите отсориторовать:\n 1 - Список целых чисел \n 2 - Список случайных вещественных чисел \n 3 - Точки на комлексной плоскости \n 4 - Отрывок из книги")
number_1 = int(input())

if number_1 == 1:
    sequence = list_of_integers
elif number_1 == 2:
    sequence = random_list_of_real
elif number_1 == 3:
    sequence = points_in_circum
else:
    sequence = book[:10000]

print("Был выбран список:",sequence,"\n")

print("Выберите способ сортировки: \n 1 - Shellsort, сортировка Шелла \n 2 - Bucket sort, блочная сортировка \n 3 - Bubble sort, сортировка пузырьком \n 4 - Selection sort, сортировка выбором")
number_2 = int(input())
print("Обработка... \n")

if number_2 == 1:
    funk = shell_sort(sequence)
elif number_2 == 2 and number_1 == 1:
    find_min_max(sequence)
    funk = bucket_sort(sequence, 4)
    print("Отсортированный список:", sequence)
elif number_2 == 3:
    funk = bubble_sort(sequence)
    print("Отсортированный список:", sequence)
else:
    funk = selection_sort(sequence)
    print("Отсортированный список:", sequence)