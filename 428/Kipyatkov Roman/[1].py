# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:42:11 2023

@author: Роман
"""
import re
import datetime
import numpy as np
import queue
#ВХОДНЫЕ ДАННЫЕ:
my_data=("Роман",26,7,2003)
disc_marks= {
    "русский":5,
    "литература":3,
    "информатика":4,
    "алгебра":4,
    "технология":5,
    "физра":5,
    "ИЗО":5,
    "геомтерия":5,
    "история России":4,
    "всеобщая история":5,
    "краеведение":4,
    "география":5,
    "физика":4,
    "экономика":5,
    "лицееведение":4,
    "ничегонеделание":5,
    }
Aztec_Empire=["Tenoch","Acamapichtli","Huitzilihuitl","Chimalpopoca","Xihuitl Temoc","Itzcoatl","Moctezuma I","Atotoztli","Axayacatl","Tizoc","Ahuitzotl","Moctezuma II","Cuitláhuac","Cuauhtémoc","Tlacotzin","Motelchiuhtzin","Xochiquentzin","Huanitzin","Tehuetzquititzin"
              ,"Cecetzin","Cipac"]
print(len(Aztec_Empire))
family_names=["Айза","Мухаммад","Айзек","Айза","Сергей","Иван","Владислав","Сергей","Юнона"]
dict_family_names={"Айза":2001,"Мухаммад":1999,"Айзек":1995,"Айза":1994,"Сергей":1967,"Иван":1955,"Владислав":1954,"Сергей":1990,"Юнона":1919}
kivi_name="Терешкова"
#ЗАДАНИЯ:
marks=sum(disc_marks.values())/len(disc_marks.values())
unique_name=[]
for name in family_names:
    if name in unique_name:
        continue
    else:
        unique_name.append(name)
uniq_a=[]
n=0
for sub in disc_marks:
    for i in sub:
        if i in uniq_a or i.swapcase() in sub:
            continue
        else:
            uniq_a.append(i)
    n+=(len(sub))
print("/n" * 100)
print("1)Средняя оценка в аттестате-",marks)
print('--------------------------------')
print("2)Уникальные имена:",*unique_name)
print('--------------------------------')
print("3)Общая длина всех названий предметов:",n)
print('--------------------------------')
print("4)Уникальные буквы в названии предметов:",uniq_a)
print('--------------------------------')
print("5)Имя пушистой кивы -",kivi_name,". В двоичной системе:")
print(bin(12))
for ch in kivi_name:
    print(bin(ord(ch)))
print('--------------------------------')
family_names.sort(reverse=True)
print("6) Отсортированный список родственников по именам:",family_names)
print('--------------------------------')
print(datetime.datetime.today())
date_old=datetime.datetime(day=my_data[1],month=my_data[2],year=my_data[3])
date=date_old
print(date)
print("7) количество дней от моей даты рождения до текущей даты",(datetime.datetime.today()-date).days)
tonex=str(input("Для продолжения введите любой символ:"))
print('--------------------------------')
print("8)FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - выводятся все;")
objects=0
q = queue.Queue()
objects=int((input("К заданию 8: Введите индекс который хотите добавить в очередь(110 - прекратить алгоритм): ")))
while objects!=110:
    q.put(family_names[objects])
    objects=int((input("К заданию 8: Введите индекс который хотите добавить в очередь(110 - прекратить алгоритм): ")))
while not q.empty():
    print(q.get(), end=' ')
print('--------------------------------')
number = (my_data[1] + my_data[2]**2 + my_data[3]) % 21 + 1
numb=int(input("к зад 9: Введите индекс(1-9):"))
family_names[numb-1]=Aztec_Empire[number-1]
print("9-по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1:",family_names)
print('--------------------------------')
print("10-создать связный список:")
#зад 10
class Node:
    def __init__(self,key, data):
        self.data = data
        self.key=key
        self.next = None
    def append(self, key,data):
        end = Node(key,data)
        n = self
        while (n.next):
            n = n.next
        n.next = end
linlist=Node(1,0+1)
i=0
n=dict_family_names.values()
dict_family_names=["Айза 2001","Мухаммад 1999","Айзек 1995","Айза 1994","Сергей 1967","Иван 1955","Владислав 1954","Сергей 1990","Юнона 1919"]
l=sorted(dict_family_names, key=lambda x: x[-4]+x[-3]+x[-2]+x[-1])
lnew=[]
for i in range(len(l)):
    lnew.append(re.sub(r'[^\w\s]+|[\d]+', r'',l[i]).strip())
print(lnew)
i=0
while i!=len(lnew):
    linlist.append(lnew[i],i+1)
    i+=1
node=linlist
while node.next:
    node = node.next
    print(node.key,node.data)
print('--------------------------------')
#зад 11:
print("11)функцию-генератор, вариант определяется как number = len(ФИО) * len (family_names) % 4:)")
numberr=len(my_data[0]) * len (family_names) % 4
print(numberr,'-Номер, получившийся по формуле - Последовательность Сильвестра:')
def gen(N):
    c=1
    a=1
    while c!=10:
        c+=1
        yield a+1
        a+=1
        a=a*(a-1)
N=10
for b in gen(N):
    print(b)
print(numberr)
