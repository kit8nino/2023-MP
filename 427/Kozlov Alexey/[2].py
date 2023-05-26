# Алгоритмы сортировки

import random
random.sample(range(1, 18), 4)
# Код вернул: [14, 12, 7, 9]

# Поразрядная сортировка Radix Sort

# список целых чисел от 0 до 999999:
list_1 = []
for i in range(1000000):
    a = random.randint(0, 999999)
    list_1.append(a)

def radix_sort(arr):
    # Находим максимальное число в списке, чтобы определить количество разрядов
    max_num = max(arr)
    # Определяем количество разрядов
    num_digits = len(str(abs(max_num)))

    # Итерируемся по разрядам от младшего к старшему
    for digit in range(num_digits):
        # Создаем 10 корзин для каждой цифры (от 0 до 9)
        buckets = [[] for _ in range(10)]

        # Распределяем числа по корзинам на основе текущего разряда
        for num in arr:
            # Получаем значение текущего разряда
            current_digit = (num // 10 ** digit) % 10
            # Помещаем число в соответствующую корзину
            buckets[current_digit].append(num)

        # Обновляем список, объединяя числа из всех корзин
        arr = [num for bucket in buckets for num in bucket]

    return arr


# Применяем поразрядную сортировку к списку list_1
sorted_list = radix_sort(list_1)


# сортировка подсчётом

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
list_2 = []
for i in range(10):
    a = random.uniform(-1.0, 1.0)
    list_2.append(a)

# Находим минимальное и максимальное значение в списке
min_value = min(list_2)
max_value = max(list_2)

# Создаем словарь для подсчета
count = {}

# Подсчитываем количество вхождений каждого значения
for num in list_2:
    index = int((num - min_value) * 100000)
    if index in count:
        count[index] += 1
    else:
        count[index] = 1

# Создаем отсортированный список
sorted_list = []
for index, count_value in sorted(count.items()):
    num = (index / 100000) + min_value
    sorted_list.extend([num] * count_value)

print(sorted_list)

# Гномья сортировка 

#42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day/ birth_month
# (можно случайных, можно равномерно распределённых), сортировать по модулю числа;

points = []
for i in range(10):
# Генерируем случайные координаты x и y в диапазоне от -11/6 до 11/6

    x = random.uniform(-11/6, 11/6)
    y = random.uniform(-11/6, 11/6)
    point = complex(x, y)
    points.append(point)

def gnome_sort(arr):
    i = 0
    n = len(arr)

    while i < n:
        if i == 0 or abs(arr[i]) >= abs(arr[i - 1]):
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr

sorted_points = gnome_sort(points)
print("Отсортированный список ")
print(sorted_points)

# пирамидоидальная сортировка 

#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
# Чтение отрывка книги из файла и разобьём список по словам
import re

# функция разделения текстового файла по словам
def split_file_into_words(lines):
    words = []
    for line in lines:
        line_words = re.findall(r'\b\w+\b', line)
        words.extend(line_words)
    return words


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Открытие и чтение текстового файла
filename = 'Отцы и дети.txt'
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Удаление символа новой строки из каждой строки
lines = [line.strip() for line in lines]

# Разделение файла на слова
words = split_file_into_words(lines)

# Сортировка массива слов
heap_sort(words)

# Запись отсортированных слов в новый файл
output_filename = 'output.txt'
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write('\n'.join(words))

print('Файл успешно отсортирован и разделен на слова.')