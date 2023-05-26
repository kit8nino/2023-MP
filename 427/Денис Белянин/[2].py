# Исходные данные:
# 1)список целых чисел от 0 до 999999;
# 2)список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
# 3)42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю числа;
# 4)отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.

# import random
#
# random.sample(range(1, 18), 4) - выпало [1, 4, 11, 14]
# 1)shaker sort, сортировка перемешиванием;
# 4)insertion sort, сортировка вставкой;
# 11)Merge sort, сортировка слиянием;
# 14)Radix sort, поразрядная сортировка;


import random
import math

print("Shaker sort, сортировка перемешиванием:")

#Алгоритм перебирает список в обе стороны и меняет местами соседние элементы, если они стоят в неправильном порядке.
def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        #Проход слева направо
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        #Проход справа налево
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

arr = [i for i in range(100)]
random.shuffle(arr) #Случайное перемешивание массива
sorted_arr = shaker_sort(arr)
print(sorted_arr)

print("Insertion sort, сортировка вставкой:")

#Алгоритм начинает с первого элемента и сравнивает его со всеми элементами в отсортированной части списка.
#Если элемент меньше, чем предыдущий, то он вставляется в правильную позицию в отсортированной части списка.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #Вставка элемента в отсортированную часть массива
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [random.uniform(-1, 1) for i in range(100)] #Создание массива случайных чисел
sorted_arr = insertion_sort(arr)
print(sorted_arr)


print("Radix sort, поразрядная сортировка:")

#Он используется для сортировки чисел, которые состоят из нескольких разрядов. Алгоритм сначала сортирует
#числа по последнему разряду, затем по предпоследнему и т.д., пока все числа не будут отсортированы.

birth_day = 7
birth_month = 6

r = birth_day / birth_month
n = 420

#Создаем список комплексных чисел
complex_list = [complex(random.uniform(-r, r), random.uniform(-r, r)) for i in range(n)]

#Определяем функцию для поразрядной сортировки по модулю
def sort_by_magnitude(arr):
    max_magnitude = int(math.log10(max(abs(num) for num in arr))) + 1 #Вычисляем максимальное значение разрядов

    for d in range(max_magnitude):
        count = [0] * 10
        #Подсчитываем количество чисел для каждого разряда
        for num in arr:
            digit_val = int(abs(num) / 10 ** d) % 10
            count[digit_val] += 1
        #Вычисляем сумму количества чисел, которые будут находиться в каждом разряде
        for i in range(1, 10):
            count[i] += count[i - 1]

        sorted_arr = [0] * len(arr)
        #Проходим по списку в обратном порядке и добавляем числа в соответствующие разряды
        for num in reversed(arr):
            digit_val = int(abs(num) / 10 ** d) % 10
            count[digit_val] -= 1
            index = count[digit_val]
            sorted_arr[index] = num

        arr = sorted_arr

    return arr


#Сортируем список комплексных чисел по модулю
sorted_complex_list = sort_by_magnitude(complex_list)
print(sorted_complex_list)


print("Merge sort, сортировка слиянием:")

#Алгоритм делит список пополам, пока каждый элемент не будет в отдельной части списка, затем он
#сливает эти части, сравнивая элементы и вставляя их в отсортированный список

#Чтение отрывка из книги
with open("десять негритят.txt", "r", encoding="utf-8") as f:
    words = f.read().split()


#Определяем функцию для сортировки слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    #Рекурсивно вызываем функцию merge_sort для левой и правой половинок списка
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    sorted_arr = []
    i = j = 0

    #Слияние левой и правой половинок в отсортированный список
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted_arr.append(left_sorted[i])
            i += 1
        else:
            sorted_arr.append(right_sorted[j])
            j += 1

    #Добавляем оставшиеся элементы из левой и правой половинок в отсортированный список
    sorted_arr += left_sorted[i:]
    sorted_arr += right_sorted[j:]

    return sorted_arr

#Cортируем список слов
sorted_words = merge_sort(words)
print(sorted_words)

