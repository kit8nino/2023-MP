import random
import numpy as np
#print(random.sample(range(1, 18), 4)) -> 11,12,4,10 

unsort_big = np.random.randint(0,1000000,1000000)                                        # случайные целые числа
unsort_sm =  [np.random.uniform(-1,1) for i in range(999999)]                            # случайные вещественные числа от -1 до 1

birth_day = int(input("Введите день рождения: "))
birth_month = int(input("Введите месяц рождения: "))                            

r = birth_day / birth_month                                                              # радиус окружности 

points = [complex(random.uniform(-r, r), random.uniform(-r, r)) for i in range(42000)]   # точки комплексной плоскости

with open("book.txt", "r", encoding="utf-8") as f:                                       # отрывок из книги 
    text = f.read()
words = text.split()      

#12 Counting sort

def count_sort(arr):
    k=len(arr)
    count_arr = [0]*(k)                

    for i in arr:             
       count_arr[i]+=1

    index=0
    for i in range(k):                 
        while count_arr[i]>0:
            arr[index] =i
            index +=1
            count_arr[i] -=1
    return(arr)

print(count_sort(unsort_big))

#11 Merge sort

def merge_sort(a):                         
    if len(a)<=1:
        return a
    middle=len(a)//2                       
    left_array=a[:middle]
    right_array=a[middle:]
    left_sorted=merge_sort(left_array)     
    right_sorted=merge_sort(right_array)
    return merge(left_sorted,right_sorted) 

def merge(left_array,right_array):
    result=[]
    i,j=0,0
    
    while i<len(left_array) and j<len(right_array):
        if left_array[i]<=right_array[j]:
            result.append(left_array[i])
            i+=1
        else:
            result.append(right_array[j])
            j+=1
    
    while i<len(left_array):
        result.append(left_array[i])
        i+=1

    while j<len(right_array):
        result.append(right_array[j])
        j+=1

    return result

sort_sm = merge_sort(unsort_sm)
print(sort_sm)

#4 insertion sort

def insert_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and abs(arr[j]) > abs(current): 
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current

    return arr

sort_points = insert_sort(points)
print(sort_points)

#10 quicksort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
                             
sorted_words = quick_sort(words)
print(sorted_words)




