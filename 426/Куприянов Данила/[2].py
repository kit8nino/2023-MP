import random
import math
import string

# Исходные данные
integers = [i for i in range(1000)]
random.shuffle(integers)

random_real = [random.uniform(-1, 1) for i in range(1000)]

r = 1 / 11
n = 1000


def PointsInCircum(r, n):
    return [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r) for x in range(0, n + 1)]


points_in_circum = PointsInCircum(r, n)

file = 'book.txt'
book = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            book.append(word.strip(string.punctuation))


# Действия
def gnome_sort(seq):
    index = 1
    i = 0
    n = len(seq)
    while i < n - 1:
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
        else:
            i, index = index, index + 1


def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq


def shaker_sort(seq):
    l = 0  # left
    r = len(seq) - 1  # right
    control = r
    while l < r:
        for i in range(l, r):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                control = i
        r = control
        for i in range(r, l, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                control = i
        l = control


def bubble_sort(seq):
    n = len(seq)
    for i in range(n):
        for j in range(n - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


# Использование сортировок
sequence = []

print("shaker sort:")
print("до сортировки:", integers)
sequence = integers.copy()
shaker_sort(sequence)
print("после сортировки:", sequence, "\n")

print("bubble sort:")
print("до сортировки:", random_real)
sequence = random_real.copy()
bubble_sort(sequence)
print("после сортировки:", sequence, "\n")

print("gnome sort:")
print("до сортировки:", points_in_circum)
sequence = points_in_circum.copy()
gnome_sort(sequence)
print("после сортировки:", sequence, "\n")

print("selection sort:")
print("до сортировки:", book[:10000])
sequence = book[:10000].copy()
selection_sort(sequence)
print("после сортировки:", sequence)