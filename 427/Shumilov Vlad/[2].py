# 4 - сортировка вставкой
# 6 - сортировка деревом
# 17 - битонная сортировка
# 10 - быстрая сортировка
import random as rnd
import numpy as np


arr_N = []
arr_R = []

# №1 список целых чисел от 0 до 999999 (ну почти)
for i in range(1000):
    arr_N.append(i)
rnd.shuffle(arr_N)

# №2 список из (почти) 99999 случайных вещественных чисел в диапазоне [-1, 1]
for i in range(-1000, 1000):
    arr_R.append(i / 1000)
rnd.shuffle(arr_R)


# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr


# Быстрая сортировка
def quick_sort(arr, low, high):
    if low >= high:
        return
    else:
        rnd_start = rnd.choice(arr[low:high + 1])
        i = low
        j = high
        while i <= j:
            while arr[i] > rnd_start:
                i += 1
            while arr[j] < rnd_start:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                quick_sort(arr, low, j)
                quick_sort(arr, i, high)


# Битонная сортировка
def bitonic_sort(arr):
    mid = len(arr) // 2
    first = bitonic_sort(arr[:mid])
    second = bitonic_sort(arr[mid:])
    arr = bitonic_merge(first + second)
    return arr


def bitonic_merge(arr):
    bitonic_compare(arr)
    mid = len(arr) // 2
    first = bitonic_merge(arr[:mid])
    second = bitonic_merge(arr[mid:])
    arr = first + second
    return arr


def bitonic_compare(arr):
    dist = len(arr) // 2
    for i in range(dist):
        if arr[i] > arr[i + dist]:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]


arr1 = [3, 7, 4, 8, 6, 2, 1, 5]

print(bitonic_sort(arr_N))
# print(quick_sort(arr_R, 0, len(arr_R) - 1))
