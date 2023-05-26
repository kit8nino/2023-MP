import random
import numpy as np
import re

                                # Исходные данные

int_list = list(range(1000000))


float_list = [random.uniform(-1, 1) for i in range(99999)]


r = 14 # r = birth_day / birth_month = 28 / 2 = 14
points = []
for i in range(42000):
    point = np.random.rand() * r * np.exp(2j * np.pi * np.random.rand())
    points.append(point)
sorted_points_list = sorted(points, key=np.abs)


with open('C:\\Users\\User\\Desktop\\fight_club.txt', 'r') as file:
    text = file.read()
words = re.split(r'\W+', text)
words_list = []
for word in words:
    if word != '':
        words_list.append(word)

# print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне
# Вернуло [1, 9, 8, 11]



                            # Сортировка перемешиванием: 

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        # Проход по массиву слева направо
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # Если не было перестановок, массив отсортирован
        if not swapped:
            break
        # Уменьшаем диапазон справа, так как самое большое число уже на своем месте
        end -= 1
        # Проход по массиву справа налево
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # Увеличиваем диапазон слева, так как самое маленькое число уже на своем месте
        start += 1
    return arr



                                # Пирамидальная сортировка

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи

def heapify(arr, n, i): #
    
    largest = i # самое большое число - корень
    left = 2 * i + 1   
    right = 2 * i + 2  

  # Проверяем существует ли левый дочерний элемент больший, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        # Применяем heapify к корню
        heapify(arr, n, largest)

def pyramid_sort(arr):
    n = len(arr)
    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
    return arr



                                # Сортировка выбором

def selection_sort(arr):
    
    N = len(arr)      
    for i in range(N-1):
        m = arr[i]          # минимальное значение
        p = i               # индекс минимального значения
        for j in range(i+1, N):  # поиск минимального среди оставшихся 
            if m > arr[j]:
                m = arr[j]
                p = j
        if p != i:          # обмен значениями, если был найден минимальный не в i-й позиции
            t = arr[i]
            arr[i] = arr[p]
            arr[p] = t
    return arr
    
    
def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c



                                # Сортировка слиянием 


# функция деления списка и слияния списков в общий отсортированный список
def merge_sort(a):
    N1 = len(a) // 2
    a1 = a[:N1]     
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)

    return merge_list(a1, a2)   # слияние двух отсортированных списков в один
 
    
    
    
    
    
#print(cocktail_sort(int_list))                       # < 1 секунды
#print(cocktail_sort(float_list))                     # Вывод списка занял 770 секунд (!)
#print(cocktail_sort(sorted_points_list))             # 147 секунд 
#print(cocktail_sort(words_list))                     # 10 секунд 

#print(pyramid_sort(int_list))                        # < 1 секунды
#print(pyramid_sort(float_list))                      # 2 секунды
#print(pyramid_sort(sorted_points_list))              # 1 секунду
#print(pyramid_sort(words_list))                      # < 1 секунды

#print(selection_sort(int_list))                      # < 1 секунды
#print(selection_sort(float_list))                    # 236 секунд
#print(selection_sort(sorted_points_list))            # 52 секунды
#print(selection_sort(words_list))                    # 4 секунды

#print(merge_sort(int_list))                          # 3 секунды
#print(merge_sort(float_list))                        # 1 секунду
#print(merge_sort(sorted_points_list))                # < 1 секунды
#print(merge_sort(words_list))                        # < 1 секунды

