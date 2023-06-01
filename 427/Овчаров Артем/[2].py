import random
import math

# Пусть массив будет от 999999 и до 0 
numbers = []
for i in range (0,1000000):
    numbers.append(999999-i)
    
rand_numbers = []
for i in range (0,99999):
    rand_numbers.append(random.uniform(-1, 1))

birth_day = 25
birth_month = 1
r = birth_day / birth_month

complex_numbers = []
while len(complex_numbers) != 42000:
    z = complex(random.uniform(0, r), random.uniform(0, r))
    if z.real**2 + z.imag**2 < r**2:
        if z not in complex_numbers:
            complex_numbers.append(z)



words = []
with open("dog's_heart.txt", encoding="utf-8") as file:     
    for line in file:
        for word in line.split():       
            words.append(word)  
            
            
#  Выпавшие мне сортировки: 5, 11, 13, 8.

# 5 Сортировка Шелла 
def shell_sort(arr):
    step = len(arr) // 2

    while step > 0:
        for i in range(step, len(arr)):
            current_val = arr[i]
            position = i

            while position >= step and arr[position - step] > current_val:
                arr[position] = arr[position - step]
                position -= step
                arr[position] = current_val

        step //= 2
    return arr
numbers=shell_sort(numbers)
print("Результат сортировки: ",numbers)

# 11 Merge sort, сортировка слиянием


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    
    def merge(left_part, right_part):
        res = []
        
        while len(left_part) != 0 and len(right_part) != 0:
            if left_part[0] < right_part[0]:
                res.append(left_part[0])
                left_part.remove(left_part[0])
                
            elif left_part[0] > right_part[0] :
                res.append(right_part[0])
                right_part.remove(right_part[0])
                
        if len(left_part) == 0:
            res += right_part
            
        elif len(right_part) == 0:
            res += left_part
            
        return res    
    return merge(left_arr, right_arr)

rand_numbers = merge_sort(rand_numbers)
print("Результат сортировки: ", rand_numbers)


# 13 Bucket sort, блочная (карманная) сортировка , 
# в качестве сортировки самих блоков используются сортировка вставкой (insertion sort)

def insertion_sort(arr,arr1 ):
    for i in range(1, len(arr)):
        paste_element = arr[i]
        paste_element1 = arr1[i]
        while i > 0 and arr[i-1] > paste_element:
            arr[i] = arr[i-1]
            arr1[i] = arr1[i-1]
            
            i = i-1
        arr[i] = paste_element
        arr1[i] = paste_element1

def find_min_and_max(arr):
    if len(arr) == 0:
        return [0, 0]
    min_max = [arr[0], arr[0]]
    for element in arr:
        if element < min_max[0]:
            min_max[0] = element
        if element > min_max[1]:
            min_max[1] = element
    return min_max


def bucket_sort(arr, n):
    buckets = []
    buckets1 = []
    modul = []
    for i in arr:
        modul.append(abs(i))
    
    for i in range(n):
        buckets.append([])
        buckets1.append([])
    min_max = find_min_and_max(modul)
    if(min_max[0] == min_max[1]):
        return
    for i in range(len(modul)):
        buckets[math.floor((n * (modul[i] - min_max[0])) // (min_max[1]-min_max[0]+1))].append(modul[i])
        buckets1[math.floor((n * (modul[i] - min_max[0])) // (min_max[1]-min_max[0]+1))].append(arr[i])
        
    for i in range(len(buckets1)):
        if(len(buckets1[i]) <= 32):
            insertion_sort(buckets[i],buckets1[i] )            
        else:
            bucket_sort(buckets1[i], n)
    insert_index = 0
    for bucket in buckets1:
        for element in bucket:
            arr[insert_index] = element
            insert_index += 1
    insert_index = 0        
    for bucket in buckets:
        for element in bucket:
            modul[insert_index] = element
            insert_index += 1 
# Взял более менее оптимальное количество блоков = 500
# + параллельно сортирую созданный массив модулей этих чисел 

bucket_sort(complex_numbers , 500) 
print("Результат сортировки: ",complex_numbers)


# 8 selection sort, сортировка выбором

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i= j
        if min_i != i:
            temp = arr[i]
            arr[i] = arr[min_i]
            arr[min_i] = temp
    return arr
words=selection_sort(words)
print("Результат сортировки: ",words)

