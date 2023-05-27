'''Сортировка слиянием для вещественных чисел'''
import numpy as np
'''Сначала печатает массив вещественных чисел, потом отсортированный'''
arrSize = 99999
arr = []
arr = np.random.uniform(-1,1,size=arrSize)
print(arr,len(arr))

def Merge(arr):
    if len(arr) <= 1:
        return arr
    
    arr1 = arr[0:len(arr)//2]
    arr2 = arr[len(arr)//2 : ]
    
    arr1 = Merge(arr1)
    arr2 = Merge(arr2)
    rarr1 = len(arr1); rarr2 = len(arr2)
    larr1 = 0 ; larr2 = 0 ; k = 0
    Dublicat = [0] * (len(arr1) + len(arr2))
    
    if len(arr1) == 1 and len(arr2) == 1: 
        if arr1[0] < arr2[0]:
            Dublicat[0] = arr1[0]
            Dublicat[1] = arr2[0]
            return Dublicat
        else:
            Dublicat[0] = arr2[0]
            Dublicat[1] = arr1[0]
            return Dublicat
    
    while larr1 < rarr1 and larr2 < rarr2:
        if arr1[larr1] < arr2[larr2]:
            Dublicat[k] = arr1[larr1]
            larr1 += + 1 
            k = k + 1
        else:
            Dublicat[k] = arr2[larr2]
            larr2 += 1
            k += 1
            
    if larr1 == rarr1:
        for i in range(larr2,rarr2):
            Dublicat[k] = arr2[i] 
            k += 1
    else:
        for i in range(larr1,rarr1):
            Dublicat[k] = arr1[i]
            k += 1
    return Dublicat
print(Merge(arr))