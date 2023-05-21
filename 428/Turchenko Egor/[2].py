import numpy as np
import random
from pathlib import Path
import collections
import re

# Methods randomly chosen: 13, 5, 17, 16
# 13:Bucket sort 5: shellsort  17: bitonic sort 16: most significant digit
"""def randmetod():
    import random
    print(random.sample(range(1, 18), 4))
"""
x = -1;
# Simple digits
def simp():
    lower_value = 1
    upper_value = 999
    sd=[]
    sd_new=[]
    for number in range(lower_value, upper_value + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
                else:
                    sd.append(number)
    sd_new.append(sd[0])
    for i in range(1,len(sd)):
        if sd[i]!=sd[i-1]:
            sd_new.append(sd[i])

    sd=sd_new
    #Bucket sort
    N=15

    def bucketSort(arr, N):
        r = max(arr)
        l = min(arr)

        rnge = (r - l) / N
        temp = []

        for i in range(N):
            temp.append([])

        for i in range(len(arr)):
            diff = (arr[i] - l) / rnge - int((arr[i] - l) / rnge)

            # append the boundary elements to the lower array
            if (diff == 0 and arr[i] != l):
                temp[int((arr[i] - l) / rnge) - 1].append(arr[i])

            else:
                temp[int((arr[i] - l) / rnge)].append(arr[i])

        for i in range(len(temp)):
            if len(temp[i]) != 0:
                temp[i].sort()

        k = 0
        for lst in temp:
            if lst:
                for i in lst:
                    arr[k] = i
                    k = k + 1

    bucketSort(sd,N)
    print('Sorted: ', sd)

# Случ.числа
def randomer():
    n=99
    min=-1
    max=1
    rand=[]
    for i in range(n):
        rand.append(random.uniform(min,max))
    print(rand)
    #shellsort
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = rand[i]
            j = i
            while j >= interval and rand[j - interval] > temp:
                rand[j] = rand[j - interval]
                j -= interval
            rand[j] = temp
        interval //= 2
    print(rand)

def comrand():
    r=30/1
    #N=32768
    N=256
    com=[]
    for i in range(N):
        x=random.uniform(0,r)
        ymax=np.sqrt(r**2-x**2)
        y=random.uniform(-ymax,ymax)
        c=complex(x,y)
        com.append(c)
    up=1
    def compAndSwap(a, i, j, dire):
        rad_i=np.abs(a[i])
        rad_j=np.abs(a[j])
        if (dire == 1 and rad_i > rad_j) or (dire == 0 and rad_i < rad_j):
            a[i], a[j] = a[j], a[i]

    def bitonicMerge(a, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                compAndSwap(a, i, i + k, dire)
            bitonicMerge(a, low, k, dire)
            bitonicMerge(a, low + k, k, dire)

    def bitonicSort(a, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            bitonicSort(a, low, k, 1)
            bitonicSort(a, low + k, k, 0)
            bitonicMerge(a, low, cnt, dire)

    def sort(a, N, up):
        bitonicSort(a, 0, N, up)
    sort(com,N,up)
    print('Sorted: ', com)

def book():
    words = [w.lower() for w in Path('MPBook.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
    print(len(words),'words in file')
    #print(words)

    test=words[0:40]
    words=test
    for i in range(len(words)):
        words[i] = re.sub(",", "", words[i])
    print('not sorted:',words)
    #print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

    heap = [0] * 1000;
    def heapForm(k):
        global x;
        x += 1;
        heap[x] = k;
        child = x;
        index = x // 2;

        while (index >= 0):
            if (heap[index] > heap[child]):
                tmp = heap[index];
                heap[index] = heap[child];
                heap[child] = tmp;
                child = index;

                index = index // 2;

            else:
                break;
    def heapSort():
        global x;
        while (x >= 0):
            k = heap[0];

            print(k, end=" ");

            heap[0] = heap[x];

            x = x - 1;
            index = 0;
            length = x;
            left1 = 1;
            right1 = left1 + 1;

            while (left1 <= length):

                if (heap[index] <= heap[left1] and
                        heap[index] <= heap[right1]):
                    break;
                else:
                    if (heap[left1] < heap[right1]):
                        tmp = heap[index];
                        heap[index] = heap[left1];
                        heap[left1] = tmp;
                        index = left1;
                    else:
                        tmp = heap[index];
                        heap[index] = heap[right1];
                        heap[right1] = tmp;
                        index = right1;
                left1 = 2 * left1;
                right1 = left1 + 1;

    def sort(k, n):
        for i in range(n):
            heapForm(k[i]);
        heapSort();
    sort(words,len(words))
    return()
def menu():
    while(1):
        inpt=int(input('Press 1-4'))
        if inpt==1:
            simp()
        elif inpt==2:
            randomer()
        elif inpt==3:
            comrand()
        elif inpt==4:
            book()
        else:
            break
    return 1

menu()