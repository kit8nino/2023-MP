#Исходные данные:
#1)список целых чисел от 0 до 999999;
#2)список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
#3)42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю числа;
#4)отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
#Random_Variable=random.sample(range(1, 18), 4) => [2, 7, 10, 11]
    #2)сортировка пузырьком;
    #7)Гномья сортировка;
    #10)быстрая сортировка;
    #11)сортировка слиянием.

import random

print("СОРТИРОВКА ПУЗЫРЬКОМ: ")
#Сортировка пузырьком — здесь нужно последовательно сравнивать значения соседних элементов и менять числа местами,
# если предыдущее оказывается больше последующего.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # последние i элементов уже отсортированы, поэтому их можно пропустить
        for j in range(0, n-i-1):
            # если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
numbers = list(range(999999))
random.shuffle(numbers)
bubble_sort(numbers)
print(numbers, "\n")


print("ГНОМЬЯ СОРТИРОВКА: ")
#мы начинаем с первого элемента и движемся вправо. Если текущий элемент больше или равен предыдущему, мы двигаемся еще правее.
# Если текущий элемент меньше предыдущего, мы меняем их местами и двигаемся на одну позицию влево.
# Мы продолжаем этот процесс до тех пор, пока не пройдем весь список.
def gnome_sort(arr):
    i = 1
    while i < len(arr):
        # если текущий элемент больше предыдущего, двигаемся вправо
        if arr[i-1] <= arr[i]:
            i += 1
        # если текущий элемент меньше предыдущего, меняем их местами и двигаемся влево
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            if i > 1:
                i -= 1
    return arr

numbers = []
for i in range(99999):
    numbers.append(random.uniform(-1, 1))
gnome_sort(numbers)
print(numbers, "\n")


print("БЫСТРАЯ СОРТИРОВКА: ")
#мы выбираем опорный элемент, разбиваем список на две части:
# элементы, меньшие опорного, и элементы, большие опорного, и рекурсивно сортируем каждую из этих частей.
# создаем список из 42000 случайных точек комплексной плоскости, лежащих внутри окружности радиуса 4.67

birth_day = 28
birth_month = 6
r = birth_day / birth_month

points = []
for i in range(500):
    real = random.uniform(-r, r)
    imag = random.uniform(-r, r)
    point = complex(real, imag)
    points.append(point)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    opor = arr[len(arr) // 2]#выбор опорного элемента
    left = []
    middle = []
    right = []
    for x in arr:
        if abs(x) < abs(opor):
            left.append(x)
        elif abs(x) == abs(opor):
            middle.append(x)
        else:
            right.append(x)
    return quicksort(left.copy()) + middle + quicksort(right.copy())

sorted_points = quicksort(points)
print(sorted_points,"\n")


print("СОРТИРОВКА СЛИЯНИЕМ: ")
#мы разбиваем массив на две примерно равные части, затем каждая половина сортируется рекурсивно.
# Затем отсортированные половины сливаются в новый массив в отсортированном порядке.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])#срез списка arr, который содержит элементы с начала списка до индекса mid-1
    right = merge_sort(arr[mid:])#срез списка arr, который содержит элементы с индекса mid до конца списка
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Чтение отрывка книги из файла и разобьём  список по словам
with open('sort.txt', 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()
sorted_words = merge_sort(words)
print(sorted_words)
