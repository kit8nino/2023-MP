from audioop import reverse
from statistics import mean
import datetime as dt
import random
import queue

##########
def QuickSort_rev(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] > q:
                i += 1
            while A[j] < q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                QuickSort_rev(A, l, j)
                QuickSort_rev(A, i, r)
###########

Me = ('Konovalov', 'Valentin', 'Andreevich', 14, 3, 2003)

certificate = {'mathematic': 4, 'russian_language': 5, 'physics': 4, 'literature': 4,
              'history': 4,'English_language': 5, 'chemistry': 5, 'biology': 4,
               'geography': 5, 'informatics': 5, 'economics': 4, 
             'obj': 5}

relatives = ['Angrey', 'Elena', 'Polina', 'Artem', 'Ilya', 'Lydmila', 'Konstantin']
relatives_1 = {'Angrey':None, 'Elena':None, 'Polina':None, 'Artem':None, 'Ilya':None, 'Lydmila':None, 'Konstantin':None}

birth_years = {"Angrey": 1970, "Elena": 1970, "Polina": 1996, "Artem": 1987, "Ilya": 2019, "Lydmila": 1948, "Konstantin": 1985}

name_kitten = 'Lisa'

################### 1

temp_1 = round(sum(dict.values(certificate)) / len(certificate), 2)
print('1)', temp_1)

################### 2

unique_names = list(set(relatives))
print('2)', unique_names)

################## 3

temp_1 = len(certificate)
temp_2 = dict.keys(certificate)
sum = 0
*x, = certificate

for i in range(0, temp_1 - 1):
    sum = sum + len(x[i])
print('3)', sum) 

################## 4

letters_subject=[]
for i in list(certificate):
     letters_subject.extend( list(set(i)))
unique_letters=set(letters_subject)
print('4)',*unique_letters)

################# 5

print('5)')
for char in bytearray(name_kitten, 'utf-8'):
    print(bin(char))

################ 6

QuickSort_rev(relatives, 0, len(relatives)-1)
*x, = reversed(relatives)
print('6)', x)

############### 7

time_now = dt.datetime.today()
time_my_bith = dt.datetime(day=Me[3], month=Me[4], year=Me[5])
print('7)' ,"days: ",(time_now-time_my_bith).days)

############### 8

print('write 0 to end')
this_1 = queue.Queue(101)
i = int(input())

while i!=0:
    this_1.put(i)
    i = int(input())

print("list: ",end=':')

while not this_1.empty():
    print(this_1.get(), end=',')
print()

############### 9

number_9 = (Me[3] + Me[4]**2 + Me[5]) % 21 + 1
print('9)', number_9)
name_ruler = "Atotoztli"

print("enter index to replace")
i = int(input())

if(i>len(relatives)):
    while(i>len(relatives)):
        i-=len(relatives)
relatives[i]=name_ruler

print(relatives)

############## 10

sorted_relatives = sorted(relatives_1.keys(), key=lambda x: birth_years[x])

for i in range(len(sorted_relatives)-1):
    relatives_1[sorted_relatives[i]] = sorted_relatives[i+1]

print('10)', relatives_1)

############## 11

number_1 = 29 * 37 % 4
print(number_1)

def sylvester_sequence():
    s = [2]
    i = 1
    while True:
        s.append(s[i-1] * s[i-1] + 1)
        yield s[i]
        i += 1

s = sylvester_sequence()

for i in range(10):
    print(next(s))