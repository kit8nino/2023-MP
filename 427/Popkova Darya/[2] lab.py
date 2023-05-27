from tqdm import tqdm

# Shaker Sort - сортировка перемешиванием
def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    swap = True
    while swap:
        swap = False
        for i in tqdm(range(left, right)):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            break
        swap = False
        right -= 1
        for i in tqdm(range(right, left, -1)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swap = True
        left += 1
    return arr

# Bubble Sort - сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in tqdm(range(n)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Comp Sort - сортировка расческой
def comp_sort(arr):
    gap = len(arr)
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i + gap < len(arr):
            if abs(arr[i]) > abs(arr[i+gap]):
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True
            i += 1
    return arr

# Insertion Sort - сортировка вставкой
def insertion_sort(arr):
    n = len(arr)
    for i in tqdm(range(1, n)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Список целых чисел от 0 до 999999
arr1 = list(range(1000000))
arr1 = shaker_sort(arr1)
print(arr1[:10]) # выводим первые 10 элементов, чтобы проверить работу алгоритма

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
import random
# arr2 = [random.uniform(-1, 1) for i in range(99999)]
arr2 = [random.uniform(-1, 1) for i in range(99)]
arr2 = bubble_sort(arr2)
print(arr2[:10]) # выводим первые 10 элементов, чтобы проверить работу алгоритма

# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
birth_day = 15
birth_month = 8
r = birth_day / birth_month
points = [(random.uniform(-r, r) + 1j*random.uniform(-r, r)) for i in range(42000)]
points = comp_sort(points)
print(abs(points[0])) # выводим первый элемент по модулю, чтобы проверить работу алгоритма

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
text = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
words = text.split()
words = insertion_sort(words)
print(words[:10]) # выводим первые 10 слов, чтобы проверить работу алгоритма