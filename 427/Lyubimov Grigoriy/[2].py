import random


# random.sample(range(1, 18), 4) Вернул [2, 10, 16, 17]

# Исходные данные
list_of_int_numbers = list(range(0, 100000))

list_of_random_numbers = []
for e in range(99999):
    list_of_random_numbers.append(random.uniform(-1, 1))

birth_day = 4
birth_month = 1
r = birth_day / birth_month
list_of_complex_numbers = []
while len(list_of_complex_numbers) != 42000:
    z = complex(random.uniform(0, r), random.uniform(0, r))
    if abs(z) <= r:
        if z not in list_of_complex_numbers:
            list_of_complex_numbers.append(z)

list_of_words = []
with open("lord_of_the_rings.txt", encoding="utf-8") as book:
    data = book.read().split()
    for d in data:
        list_of_words.append(d)


# bubble sort, сортировка пузырьком
def bubble_sort(a):
    index = True
    while index:
        index = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                c = a[i]
                a[i] = a[i+1]
                a[i+1] = c
                index = True


bubble_sort(list_of_int_numbers)
# print(list_of_int_numbers)


# Quicksort, быстрая сортировка
def quicksort(a):
    right_list = []
    left_list = []
    midl_list = []
    c = int(len(a) / 2)
    for i in range(len(a)):
        if a[i] < a[c]:
            left_list.append(a[i])
        elif a[i] > a[c]:
            right_list.append(a[i])
        else:
            midl_list.append(a[i])
    if all(a[i] < a[i+1] for i in range(len(a)-1)):
        return left_list + midl_list + right_list
    return quicksort(left_list) + midl_list + quicksort(right_list)


list_of_random_numbers = quicksort(list_of_random_numbers)
# print(list_of_random_numbers)


# most significant digit
# ??????


# bitonic sort, битонная сортировка
