import random
import re
import math

# Gnome Sort
numbers = list(range(1000000))
random.shuffle(numbers)

def gnome_sort(arr):
    i = 0
    n = len(arr)
    
    while i < n:
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            
    return arr

sorted_numbers = gnome_sort(numbers)
print(sorted_numbers)

# Bucket Sort
real_numbers = [random.uniform(-1, 1) for _ in range(99999)]

def bucket_sort(numbers):
    buckets_num = 10
    buckets = [[] for _ in range(buckets_num)]
    
    for number in numbers:
        ind = int((number + 1) * buckets_num / 2)
        buckets[ind].append(number)
        
    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers.extend(sorted(bucket))
        
    return sorted_numbers

sorted_real_numbers = bucket_sort(real_numbers)
print(sorted_real_numbers)

# Heapsort
bday = 1
bmonth = 8
r = bday / bmonth

points = []
for _ in range(56000):
    angle = random.uniform(0, 2 * math.pi)
    
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    
    point = complex(x, y)
    points.append(point)

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and abs(arr[i]) < abs(arr[l]):
        largest = l
    
    if r < n and abs(arr[largest]) < abs(arr[r]):
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapsort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

sorted_points = heapsort(points)
print(sorted_points)

# Least Significant Digit (LSD) Sort
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[A-Za-z]+\b', text)
        return words

filename = 'text.txt'
words = read(filename)

def lsd_sort(words):
    max_len = max(len(word) for word in words)
    min_len = min(len(word) for word in words)
    
    if max_len == min_len:
        return sorted(words)
    
    for i in range(max_len - 1, -1, -1):
        blocks = [[] for _ in range(256)]
        
        for word in words:
            if i < len(word):
                letter = ord(word[i])
                blocks[letter].append(word)
            else:
                blocks[0].append(word)
                
        words = []
        for block in blocks:
            words.extend(block)
            
    return words

sorted_words = lsd_sort(words)
print(sorted_words)
