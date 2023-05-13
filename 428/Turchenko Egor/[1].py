# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:21:21 2023

@author: Turchenko Egor
"""
import datetime

fio = ('Turchenko Egor Ivanovich', '30', '1', '2004')
subj = {'Alg': 4, 'Rus': 4, 'Phys': 5, 'PE': 5, 'Chem': 4, 'Lit': 4, 'Eng': 5, 'Inform': 5, 'Hist': 5, 'Obsh': 5,
        'Geog': 5,
        'Bio': 5, 'Geom': 4, 'OBZ': 5}
family = ['Eudokia', 'Michail', 'Ivan', 'Alexander', 'Roman', 'Ekaterina', 'Ivan', 'Aleksey', 'Elena', 'Victor']
kit = 'Pirat'
Aztec=['Tenōch','Ācamāpichtli','Huītzilihhuitl','Chīmalpopōca','Xīhuitl Tēmoc','Itzcōhuātl','Motēuczōma Ilhuicamīna',
       'Atotoztli','Āxāyacatl','Tīzocic','Āhuitzotl','Motēuczōma Xōcoyōtl','Cuitlāhuac','Cuāuhtēmoc','Tlacotzin',
       'Motelchiuhtzin', 'Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']

def Mode1():  # Done
    avg_marks = sum(subj.values()) / len(subj.values())
    print('Avg mark: ' + str(avg_marks))
    return 1

def Mode2():  # Done
    family.append('Egor')
    unique_names = set(family)
    family.remove('Egor')
    print('Unique family names: ')
    print(unique_names)
    return 1

def Mode3():  # Done
    keys = (subj.keys())
    sumnames = ''
    for x in keys:
        sumnames += x
    print('Sum length of subj names: ' + str(len(sumnames)))
    return 1

def Mode4():  # Done
    keys = (subj.keys())
    sumnames = ''
    for x in keys:
        sumnames += x
    print("Unique letters in subj names: ")
    print(sorted(set(sumnames.lower())))
    return 1

def Mode5():  # Done
    print('Binary kit: ')
    for ch in kit:
        print(bin(ord(ch)))
    return 1

def Mode6():  # Done
    print(sorted(family, reverse=True))
    return 1

def Mode7():  # Done
    date_old = datetime.datetime(day=30, month=1, year=2004)
    date = datetime.datetime.today()
    delta = (date - date_old).days
    print('Days from my BD: ' + str(delta))
    return 1

def Mode8():        #Done
    keys = list((set(subj.keys())))
    print(keys)
    print('Create queue by typing indexes from 1 to ' + str(len(keys)))
    print('Type 0 to end the queue and list subjects')
    queue = []
    counter = -1
    while 1:
        index = int(input())
        if index == 0:
            break
        else:
            queue.append(keys[index-1])
            counter += 1
    if counter==-1:
        print('Empty queue')
        return -1
    while 1:
        print(queue[counter])
        counter -= 1
        if counter == -1:
            break
    return 1


def Mode9():    #Done
    Number = (int(fio[1]) + int(fio[2]) ** 2 + int(fio[3])) % 21 + 1
    print('Type index from 1 to ' +str(len(family))+ ' to change family member name to ' + Aztec[Number-1])
    print('Or type 0 to exit')
    familylist=sorted(family)
    print(familylist)
    index=int(input())
    if index==0:
        return -1
    familylist[index-1]=Aztec[Number-1]
    print(familylist)
    return 1

def Mode10(): #Done
    #family_sorted=['Elena', 'Victor','Eudokia','Ivan', 'Michail','Roman','Aleksey','Ekaterina', 'Alexander',  'Ivan']
    family_dict={'Elena':1,'Victor':2,'Eudokia':3,'Ivan':4, 'Michail':5,'Roman':6,'Aleksey':7,'Ekaterina':8, 'Alexander':9,  'Ivan':0}
    print(family_dict)
    return 1

def Mode11():       #Done
    number = len("Турченко Егор Иванович") * len(family) % 4
    print('var:',number)
    print('Аликвотная последовательность')
    def get_divisors(number):
        result = {1}
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                result.add(divisor)
        return sorted(result)
    test_number=678
    n=test_number
    maxiter=1000
    i=0
    while(1):
        i+=1
        n=sum(get_divisors(n))
        print(n)
        if n==1:
            break
        if i>maxiter:
            break
    return(1)


def Menu(mode):
    if mode == 1:
        Mode1()
    elif mode == 2:
        Mode2()
    elif mode == 3:
        Mode3()
    elif mode == 4:
        Mode4()
    elif mode == 5:
        Mode5()
    elif mode == 6:
        Mode6()
    elif mode == 7:
        Mode7()
    elif mode == 8:
        Mode8()
    elif mode == 9:
        Mode9()
    elif mode==10:
        Mode10()
    elif mode==11:
        Mode11()
    else:
        return -1


output = 1
while output != -1:
    print('')
    print('Select mode 1-11')
    print('Type 0 to quit')
    mode=int(input())
    output = Menu(mode)


