# 4 - сортировка вставкой
# 6 - сортировка деревом
# 17 - битонная сортировка
# 10 - быстрая сортировка
import random as rnd


arr_N = []
arr_R = []

for i in range(1000):
    arr_N.append(i)


rnd.shuffle(arr_N)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr





print(insertion_sort(arr_N))
