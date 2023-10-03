import random
import math
import string

list_int = list(range(0,1000000)) 

numbers_real = [random.uniform(-1, 1) for _ in range(99999)] 

birth_day = 2
birth_month = 12
r = birth_day / birth_month
points = [(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(42000)]


words = []
with open('book.txt', encoding='utf-8') as book:
    for line in book:
        for i in (line.split(" ")):
            if i != '\n' and len(words) < 11000:
                words.append(str(i))

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def Gnome_sort(list):
    index = 1
    i = 0
    n = len(list)
    while i < n - 1:
        if len(list[i]) <= len(list[i + 1]):
            i = index
            index = index + 1
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i = index
                index = index + 1


def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list


def quicksort(nums, fst, last):
   if fst >= last: return
 
   i, j = fst, last
   pivot = nums[random.randint(fst, last)]
 
   while i <= j:
       while nums[i] < pivot: i += 1
       while nums[j] > pivot: j -= 1
       if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   quicksort(nums, fst, j)
   quicksort(nums, i, last)
    

print(bubbleSort(list_int))

print(Gnome_sort(numbers_real))

print(selection_sort(points))

print(quicksort(words))
