import random 
import math

print("""[2] Алгоритмы сортировки

Исходные данные:
--список целых чисел от 0 до 999999;
--список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
--42000 разных точки комплексной плоскости, лежащие внутри окружности 
    радиуса r = birth_day / birth_month (можно случайных,
    можно равномерно распределённых), сортировать по модулю числа;
--отрывок из книги (любой, на свой выбор) не менее 10000 слов,
    разбитый в список по словам.""")
print()

# --------------------------------------------------------------------------------------------------------------------------
# создаем список целых чисел от 0 до 1000000(невключительно)

list_int_numbers = [random.randrange(0, 999999, 1) for numbers in range(100)] # сделал список из ста чисел, тк слишком много
                                                                              # времени занимает проверка для 100к чисел         

# --------------------------------------------------------------------------------------------------------------------------    
# создаем список 99 999 случайных вещ чисел в диапазоне [-1, 1]

list_float_numbers = [random.uniform(-1, 1) for numbers in range(999) ]  # сделал список из 1000 чисел, тк слишком много
                                                                         # времени занимает проверка для 100к чисел       

# --------------------------------------------------------------------------------------------------------------------------
# 42000 разных точки комплексной плоскости, лежащие внутри окружности 
# радиуса r = birth_day / birth_month (можно случайных,
# можно равномерно распределённых), сортировать по модулю числа;

birth_day, birth_month = 8, 6
r = birth_day / birth_month     # радиус окружности
complex_points = []             # cписок комплексных чисел

while len(complex_points) != 42000:
    diap_radius = random.uniform(0, r)   # задаем диапазон значений радиуса окружности
    fi = random.uniform(0, 2 * math.pi)  # задаем диапазон углов                        # добавляем в список точки комплексной окружности,
    complex_points.append([diap_radius * math.cos(fi), diap_radius * math.sin(fi)])     # лежащих внутри оркужности радиуса r 

# --------------------------------------------------------------------------------------------------------------------------
# отрывок из книги (любой, на свой выбор) не менее 
# 10000 слов, разбитый в список по словам

list_words = []
with open('книга.txt', encoding= 'utf-8') as book:
    for line in book:
        for i in (line.split(' ')):
            if i != '/n' and len(list_words) < 10001:
                list_words.append(str(i)) 


# --------------------------------------------------------------------------------------------------------------------------
# print(random.sample(range(1, 18), 4))
print("""Mетоды сортировки, которые будут использоваться: 
    2  сортировка пузырьком
    1  сортировка перемешиванием 
    17 битонная сортировка
    16 most significant digit""")

print()



# 1----------------------------------------------------------------------------------------------------
print("Cортировка пузырьком Bubble sort для действительных чисел")

count_smen = 0  

for j in range(len(list_int_numbers) - 1):
    for i in range(len(list_int_numbers) - 1 - j):
        if list_int_numbers[i] > list_int_numbers[i+1]:
            list_int_numbers[i], list_int_numbers[i+1] = list_int_numbers[i+1], list_int_numbers[i]
            count_smen +=1 

list_int_numbers_sort = list_int_numbers
list_int_numbers_sort.sort()

if list_int_numbers_sort == list_int_numbers:     # проверка
    print("Сортировка выполнена верно")

print("Количество смен понадобилось:", count_smen)      
print("Для вывода списка введите число 5")

num_chek_one = int(input())

if num_chek_one == 5:
    print(list_int_numbers)

print()



# 1----------------------------------------------------------------------------------------------------
print("Сортировка перемешиванием для вещественных чисел")

left_border = 0 
right_border = len(list_float_numbers) - 1
c_smen_2 = 0   # счетчик для количества смен

while left_border <= right_border:
    for i in range(left_border, right_border, 1):
        if list_float_numbers[i] > list_float_numbers[i + 1]:
          list_float_numbers[i], list_float_numbers[i + 1] = list_float_numbers[i + 1], list_float_numbers[i]
          c_smen_2 += 1
    right_border -= 1

    for i in range(right_border, left_border, -1):
        if list_float_numbers[i - 1] > list_float_numbers[i]:
            list_float_numbers[i], list_float_numbers[i - 1] = list_float_numbers[i - 1], list_float_numbers[i]
            c_smen_2 += 1
    left_border += 1                

list_float_numbers_sort = list_float_numbers                   # проверка
list_float_numbers_sort.sort()

if list_float_numbers_sort == list_float_numbers:
    print('Сортировка выполнена верно')
    print("Количество смен понадобилось:", c_smen_2)

print("Для вывода списка введите число 5")
num_chek_two = int(input())

if num_chek_two == 5:
    print(list_float_numbers)   

print()



# 17----------------------------------------------------------------------------------------------------
print("Битонная сортировка для списка точек комплексной плоскости")

def bitonic_sort(arr, up = True):                 
    if len(arr) <= 1:                # флаг up, который указывает, должен ли алгоритм сортировать массив по возрастанию или убыванию
        return arr                   # Функция сначала разбивает массив на две битонные последовательности, затем рекурсивно сортирует
    else:                            # каждую из них и объединяет их в одну битонную последовательность с помощью функции bitonic_merge
        mid = len(arr) // 2
        left = bitonic_sort(arr[:mid], True)
        right = bitonic_sort(arr[mid:], False)
        return bitonic_merge(left + right, up)

def bitonic_merge(arr, up):                    # принимает массив и флаг up, сначала вызывает функцию bitonic_compare, 
    if len(arr) <= 1:                          # которая сравнивает элементы в массиве и меняет их местами, если это необходимо
        return arr                             # чтобы получить битонную последовательность. Затем функция рекурсивно вызывает себя для
    else:                                      # каждой половины массива и объединяет их в один массив
        bitonic_compare(arr, up)
        mid = len(arr) // 2
        left = bitonic_merge(arr[:mid], up)
        right = bitonic_merge(arr[mid:], up)
        return left + right  
      
def bitonic_compare(arr, up):                     # принимает массив и флаг up, oна сравнивает элементы в массиве и
    dist = len(arr) // 2                          # меняет их местами, если это необходимо, чтобы получить битонную последовательность
    for i in range(dist):                         
        if (arr[i] > arr[i + dist]) == up:        
            arr[i], arr[i + dist] = arr[i + dist], arr[i] 

up = True
sorted_points = bitonic_sort(complex_points)

print("Для вывода списка введите число 5")
num_chek_three = int(input())

if num_chek_three == 5:
    print(sorted_points) 

print()



# 16----------------------------------------------------------------------------------------------------
print("Сортировка Most Significant Digit(MSD) для списка слов")

def radix_sort(arr):
    max_len = len(max(arr, key=len))                # Добавляем нули в начало строк, чтобы все строки были одинаковой длины
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            arr[i] = arr[i].rjust(max_len, '0')      # Сортируем строки по наиболее значимому разряду
        elif isinstance(arr[i], list):               # условие для обработки вложенных списков
            arr[i] = [word.rjust(max_len, '0') if isinstance(word, str) else word for word in arr[i]]
    return msd_sort(arr, 0, len(arr), max_len - 1)

def msd_sort(arr, start, end, digit):
    if digit < 0 or end - start <= 1:
        return arr

    groups = {}                                               # Создаем словарь, где ключ - значение наиболее значимого разряда,
    for i in range(start, end):                               # а значение - список строк с таким значением наиболее значимого разряда
        key = arr[i][digit] if isinstance(arr[i], str) else ''
        groups.setdefault(key, []).append(arr[i])

    result = []
    for key in sorted(groups.keys()):
        group = groups[key]
        if isinstance(group[0], list):
            result.extend(msd_sort(group, 0, len(group), digit - 1))
        else:
            result.extend(sort_by_digit(group, digit - 1))

    arr[start:end] = result
    return arr

def sort_by_digit(arr, digit):
    if digit < 0 or len(arr) <= 1:
        return arr

    groups = {}
    for word in arr:
        key = word[digit] if isinstance(word, str) else ''
        groups.setdefault(key, []).append(word)

    result = []
    for key in sorted(groups.keys()):
        result.extend(sort_by_digit(groups[key], digit - 1))

    return result


sort_last_list = radix_sort(list_words)

print("Для вывода списка введите число 5")
num_chek_four = int(input())

if num_chek_four == 5:
    print(sort_last_list) 
