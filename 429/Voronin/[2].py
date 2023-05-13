import random
import math
#[2]

#choose
n = random.sample(range(1, 18), 4)
print(n)
#3 2 7 10

#comp sort for int[0-999999]
print("______________________________________________________________________")
print("comp sort->")
size_arr = 100

arr = [random.randint(0, 999999) for i in range(size_arr)]

print("unsorted = > ",arr)

def comp_sort(arr):
    flag = False
    h=len(arr)
    k=0
    while(flag == False):
        h =  int(h/1.247)  
        if(h<=1):
            h=1
            flag=True
        i=0
        k+=1
        while(i+h<len(arr)):
            if (arr[i]>arr[i+h]):
                arr[i], arr[i+h] = arr[i+h], arr[i]
                flag = False
            i += 1
    print("iter - ",k)
    return arr

print("sorted = > ",comp_sort(arr))

#bubble sort for 
print("______________________________________________________________________")
print("bubble sort->")


n = 99999 #count of numbers
numbers = [random.uniform(-1, 1) for _ in range(n)]
print("unsorted = > ",numbers)
print('proceeding')

def bubble_sort(nums):
    swapped = True
    while (swapped==True):
        swapped=False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums

bubble_sort(numbers)
print("sorted = > ",bubble_sort(numbers))

#bgnome sort for zs
print("______________________________________________________________________")
print("gnome sort->")
r = 29/12  #z radius

def generate_complex_number():
    while True:
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if math.sqrt(x**2 + y**2) <= r:
            return complex(x, y)

def compare(a, b):
    return abs(a) <= abs(b)

def gnome_sort(lst, cmp):
    i, j, size = 1, 2, len(lst)
    while i < size:
        if cmp(lst[i - 1], lst[i]):
            i=j
            j+=1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1] # оказывается так можно...
            i -= 1
            if i == 0:
                i, j = j, j + 1

print("proceeding")
n = 42000 #count of z numbers
zs = [generate_complex_number() for _ in range(n)]

gnome_sort(zs, compare)
print(zs)

moduls = []

for el in zs:
    moduls.append(abs(el))
    
print("moduls -> ")
print(moduls)

#quick sort for words
print("______________________________________________________________________")
print("quick sort->")

def quicksort(lst):
   if len(lst) <= 1:
       return lst
   else:
       q = random.choice(lst)
       right = []
       left = []
       middle = []
       for w in lst:
           if w < q:
               left.append(w)
           elif w > q:
               right.append(w)
           else:
               middle.append(w)
       return quicksort(left) + middle + quicksort(right)

with open('Giver.txt', 'r') as file:
    text = file.read()


punctuation = "\'"+"\”"+'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct_text = ""
for char in text:
    if char not in punctuation:
        no_punct_text += char

words = no_punct_text.split()

print("Исходный список слов:", words)
print("Отсортированный список слов:",quicksort(words))

