import numpy as np
import datetime
name=("Рокин Данила Александрович", 9 , 7 , 2033)
marks={
       "Алгебра":3,
       "Геометрия":4,
       "География":5,
       "Физкультура":3,
       "Биология":4,
       "Информатика":5,
       "Литература":3,
       "ОБЖ":4,
       "Химия":5,
       "Русский язык":3,
       "Физика":4,
       "Астрономия":5,
       "Черчение":3,
       "МХК":4,
       }
rel_names=["Александр" , "Галина" , "Иван" , "Алексей" , "Алексей", "Данила" ]
Kiwa= "Ершик"

#srednee
sr = float(sum(marks.values())/len(marks.values()))
print(sr)

#un_names
un = set(rel_names)
print(un)

#len_sub
leng=0
for key in marks.keys():
    leng += len(key)
print(leng)

#un_letters
un_let = set()
for key in marks.keys():
    l = len(key)
    for i in range(l):
        un_let.add(key[i])        
print(un_let)

#bin_kiwa
bin1 = ' '.join(format(ord(x), '08b') for x in Kiwa)
print(bin1)

#sort
from operator import itemgetter
print(sorted(rel_names,key=itemgetter(0),reverse=True))

#date
birt = datetime.datetime(2003,7,9)
today = datetime.datetime.now()
print(today-birt)

#index
arr=[]
while True:
    word=input("Введите число(Для выхода q):")
    if word=="q":
        break
    arr.append(word)
print(arr)

#ruler
index=int(input("Введите индекс:"))
rel_names[index-1]="Ahuitzotl"
print (rel_names)


#sv_spisok

spisok = {"Галина" : 1970 , "Александр" :  1962, "Иван" : 1995}

spisok_sorted = sorted(spisok.items(), key = lambda x: x[1])

sv_spisok = {}
for i in range(len(spisok_sorted)):
    if i==len(spisok_sorted)-1:
        sv_spisok[spisok_sorted[i][0]]=None
    else:
        sv_spisok[spisok_sorted[i][0]]=spisok_sorted[i+1][0]
print("Связный список: ", sv_spisok )


#generator
#print(len(name[0]))
#print(len (rel_names))
#number = len(name[0]) * len (rel_names) % 4
#print(number)
#0-Алликвотная последовательность

def sum_d(x):
    s_d=0
    for i in range(1,int((x/2)+1)):
        if x % i == 0 :
            s_d += i
    return s_d


def al_posl(x):
    a =[]
    a=np.append(a,x)
    while x > 0:
        x = sum_d(x)
        if x in a:
            break
        a=np.append(a,x)
    return a

def generator(x): #Функция-генератор алликвотной последовательности
    for i in range(len(al_posl(x))):
        yield al_posl(x)[i]

for i in generator(10): #Пример работы функции
    print(i)
        


    
    

