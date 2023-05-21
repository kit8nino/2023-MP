import random
import cmath
#random.sample(range(1, 18), 4) # вернет список из 4 случайных значений в заданном диапазоне

# Зададим список целых чисел от 0 до 999999;
a = []
a = random.sample(range(0, 999999), 999999)
#print(a)

# Создаем список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
b = []
b = [random.uniform(-1, 1) for i in range(99999)]
#print(b)

# Создадим 42000 разных точки комплексной плоскости
compl = []
compl = [complex(random.uniform(-2, 2), random.uniform(-2, 2)) for i in range(42000)]
#print(compl)


#12 Counting sort, cортировка подсчетом для целочисленных значений массива a
def counting_sort(a):
    # Определяем минимальное и максимальное значение в списке
    min_val = min(a)
    max_val = max(a)

    # Создаем список счетчиков и заполняем его нулями
    count = [0] * (max_val - min_val + 1)

    # Считаем количество вхождений каждого элемента в список
    for val in a:
        count[val - min_val] += 1

    # Создаем отсортированный список
    sorted_a = []
    for i in range(len(count)):
        sorted_a += [i + min_val] * count[i]

    return sorted_a

sorted_a=counting_sort(a)
#print(sorted_a)


#10 Quicksort, быстрая сортировка для вещественных чисел
def quick_sort(b):
    # Базовый случай: список пуст или состоит из одного элемента
    if len(b) <= 1:
        return b

    # Выбираем опорный элемент и разбиваем список на элементы, меньшие и большие опорного
    pivot = b[0]
    lesser = []
    greater = []
    for num in b[1:]:
        if num < pivot:
            lesser.append(num)
        else:
            greater.append(num)

    # Рекурсивно сортируем элементы, меньшие и большие опорного, и объединяем их с опорным элементом
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

quick_sorted_b=quick_sort(b)
#print(quick_sorted_b)


#11 Merge sort, сортировка слиянием для комплексных чисел
def merge_sort(compl):
    # Разбиваем список на две половины
    if len(compl) > 1:
        mid = len(compl) // 2
        left_half = compl[:mid]
        right_half = compl[mid:]

        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)

        # Слияние отсортированных списков
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if abs(left_half[i]) < abs(right_half[j]):
                compl[k] = left_half[i]
                i += 1
            elif abs(left_half[i]) == abs(right_half[j]):
                if cmath.phase(left_half[i]) < cmath.phase(right_half[j]):
                    compl[k] = left_half[i]
                    i += 1
                else:
                    compl[k] = right_half[j]
                    j += 1
            else:
                compl[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            compl[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            compl[k] = right_half[j]
            j += 1
            k += 1

    return compl

merge_sorted_compl=merge_sort(compl)
#print(merge_sorted_compl)


# Разобьем отрывок из книги в список по словам
def read_file(book):
    with open(book, 'r', encoding='utf-8') as file: #Без этой штуки(encoding='utf-8') выдает ошибку: "UnicodeDecodeError"
        text = file.read()
        words = text.split()
        return words
book = 'Text.txt'
words = read_file(book)
#print(words)

#2 bubble sort, сортировка пузырьком для списка слов
def bubble_sort(words):
    n = len(words)
    # Мы используем два цикла `for`, чтобы пройти по списку и сравнить каждую пару соседних слов.
    # Если слова находятся в неправильном порядке, мы меняем их местами.
    for i in range(n):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
    return words

sorted_words=bubble_sort(words)
print(sorted_words)


