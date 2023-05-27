import math
import random

r=random.sample(range(1, 18), 4)
print(r, "- номера заданий")
# [14, 7, 3, 4] - номера заданий

numbers = list(range(0,1000000))

rand=[] 
n=100000
for i in range(n):
    rand.append(random.randint(-1,1))
    
r=5/9 
ct=[] 
while len(ct) != 42000:
    rad = random.uniform(0, r) 
    ugol = random.uniform(0, 2 * math.pi)
    ct.append([rad * math.cos(ugol),
    rad * math.sin(ugol)])

with open('text.txt', 'r', encoding='utf-8') as file:
    otrivok = file.read()
spisok = otrivok.split()

#3 - Сортировка расчёчкой
def sr(a):
	step = len(a)
	status = True
	while step > 1 or status:
		step = max(1, int(step / 1.25)) 
		status = False
		for i in range(len(a) - step):
			j = i + step
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
				status = True
	return a
print("Сортировка расчёчкой :",sr(rand))


#4 - Сортировка вставками
def sv(n):
    for i in range(1, len(n)):
        number = n[i]
        j = i - 1
        while j >= 0 and n[j] > number:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = number
    return n

print("Сортировка вставками :", sv(ct) )

# 7 - Гномья сортировка
def gs( arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr
l = len(numbers)
numbers = gs(numbers, l)
print("Гномья сортировка :", numbers)

#11 - Сортировка слиянием
def ss(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = ss(arr[:mid])
    right = ss(arr[mid:])
    return s(left, right)

def s(left, right):
    a = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a.append(left[i])
            i += 1
        else:
            a.append(right[j])
            j += 1
    a += left[i:]
    a += right[j:]
    return a
print("Cортировка слиянием:", ss(spisok))
