'''Гномья сортировка для слов'''
import string

tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

file = open('1.txt',encoding=('UTF-8'))
text = file.read()

arr = text.translate(tab).split()

i = 0
j = 1
while True:
    if arr[i-1][0].casefold()<arr[i][0].casefold():
        i = j
        j += 1
    else:
        arr[i-1],arr[i]=arr[i],arr[i-1]
        i -= 1
        if i==0:
            i = j
            j += 1
    if i == len(arr):
        break
print(arr,len(arr))
