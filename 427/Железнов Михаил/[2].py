import random

print(random.sample(range(1, 18), 4))
# 11 Сортировка слиянием (Merge sort)
# 4 Сортировка вставкой (Insertion sort)
# 12 Сортировка подсчетом (Counting sort)
# 9 Пирамидальная сортировка (Heapsort)


# 12 Counting sort
def counting_sort(arr):
    # определяем диапазон значений списка
    max_value = max(arr) + 1
    # список счетчиков
    count = [0] * max_value
    # считаем количество вхождений каждого элемента в списке
    for i in arr:
        count[i] += 1
    # перезаписываем список значений, отсортированных по возрастанию
    k = 0
    for i in range(max_value):
        for j in range(count[i]):
            arr[k] = i
            k += 1
    return arr


# список целых чисел от 0 до 999999
integers_numbers = list(range(10 ** 6))
random.shuffle(integers_numbers)
counting_sort(integers_numbers)
for number in integers_numbers:
    print(number)


# 9 Heapsort
# Max Heap - это структура данных, в которой значение каждого узла больше или равно значению его потомков.
def heap_sort(arr):
    n = len(arr)
    # проходим по дереву от родительских элементов до корня и выстраиваем Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # извлекаем элементы из Max Heap
    for i in range(n - 1, 0, -1):
        # Перемещяем максимальный элемент в конец массива
        arr[0], arr[i] = arr[i], arr[0]
        # выстраиваем max-heap для оставшихся элементов
        heapify(arr, i, 0)


def heapify(arr, n, i):
    # инициализируем корневой элемент
    largest = i
    # вычисляем индекс левого потомка
    left = 2 * i + 1
    # вычисляем индекс правого потомка
    right = 2 * i + 2
    if left < n and arr[left] >= arr[largest]:
        largest = left
    if right < n and arr[right] >= arr[largest]:
        largest = right
    # если самый большой элемент не является корневым элементом, то меняем местами корневой и наибольший элменты
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


float_numbers = []
for i in range(999999):
    float_numbers.append(random.uniform(-1, 1))
heap_sort(float_numbers)
for number in float_numbers:
    print(number)


# 4 Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and abs(key) < abs(arr[j]):
            # на каждой итерации мы сравниваем тек. эл. со всеми предыдущими эл. и вставляем его в правильное место
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 42000 разных точки комплексной плоскости
r = 30 / 7
complex_points = []
for i in range(42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if abs(x + y * 1j) < r:
        complex_points.append(x + y * 1j)
insertion_sort(complex_points)
for point in complex_points:
    print(point)


# 11 Merge sort
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    # вычислим индекс середины списка и разобьем его на две части (левую и правую)
    average_index = n // 2
    left = []
    for i in range(average_index):
        left.append(arr[i])
    right = []
    for i in range(average_index, n):
        right.append(arr[i])
    # рекурсивно вызываем функцию для левой и правой половин списков, чтобы отсортировать их
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # создаем новый список, который будет заполняться отсортированными элементами из двух половин исходного списка
    result = []
    # указатель для прохода по левому списку
    i = 0
    # указатель для прохода по правому списку
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i].lower() < right_sorted[j].lower():
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1
    # если один из списков закончился, то добавляем оставшиеся элементы из другого списка
    while i < len(left_sorted):
        result.append(left_sorted[i])
        i += 1
    while j < len(right_sorted):
        result.append(right_sorted[j])
        j += 1
    return result


# отрывок из книги не менее 10000 слов, разбитый в список по словам
with open("отрывок.txt", "r", encoding="utf-8") as file:
    text = file.read()
words = text.split()
merge_sort(words)
for word in words:
    print(word)
