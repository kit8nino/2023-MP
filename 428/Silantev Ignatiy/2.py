import random
import math
import string

# print(random.sample(range(1, 18), 4))
# 4, 1, 10, 8

# (4) insertion sort - это алгоритм сортировки, который работает путем 
# перемещения элементов в отсортированную часть массива по одному. Он 
# начинает с первого элемента массива и считает его отсортированным. 
# Затем он берет следующий элемент и перемещает его в отсортированную 
# часть массива, сравнивая его с каждым элементом в отсортированной части 
# и вставляя его на правильное место. Этот процесс повторяется для каждого 
# элемента в неотсортированной части массива.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

arr = list(range(100))
insertion_sort(arr)
print("1) ", arr, "\n")

# (1) shaker sort - проходит по массиву в обоих направлениях: сначала 
# слева направо, затем справа налево 

def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True):
        swapped = False
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if (not(swapped)):
            break
        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start_index = start_index + 1

arr2 = [random.uniform(-1, 1) for i in range(100)]
shaker_sort(arr2)
print("2) ", arr2, "\n")

# (10) Quicksort - работает путем выбора опорного элемента и разделения 
# массива на две части: элементы меньше опорного и элементы больше или 
# равны опорному. Затем алгоритм рекурсивно повторяет этот процесс для 
# каждой из двух частей, пока массив не будет отсортирован.

def quicksort(points):
    if len(points) <= 1:
        return points
    pivot = points[0]
    less = []
    equal = []
    greater = []
    for point in points:
        if abs(point) < abs(pivot):
            less.append(point)
        elif abs(point) == abs(pivot):
            equal.append(point)
        else:
            greater.append(point)
    return quicksort(less) + equal + quicksort(greater)

birth_day = 15
birth_month = 6
r = birth_day / birth_month

points = []
for i in range(1000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    point = complex(x, y)
    if abs(point) <= r:
        points.append(point)

sorted_points = quicksort(points)
print("3) ", sorted_points, "\n")

# (9) Heapsort - это алгоритм сортировки, который использует 
# структуру данных под названием “куча” для сортировки элементов. Он 
# работает путем создания максимальной кучи из входного массива и затем 
# извлечения максимального элемента из кучи и помещения его в конец 
# отсортированного массива. Этот процесс повторяется до тех пор, 
# пока все элементы не будут отсортированы.

file = '2.txt'
book = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            book.append(i.strip(string.punctuation))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

text = book[:1000]
heapSort(text)
print("4) ", text)