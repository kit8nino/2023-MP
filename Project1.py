# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:21:21 2023

@author: 1
"""
import datetime

fio=('Turchenko Egor Ivanovich', '30','1','2004')
subj={'Alg':4,'Rus':4,'Phys':5,'PE':5,'Chem':4,'Lit':4,'Eng':5,'Inform':5,'Hist':5,'Obsh':5,'Geog':5,
      'Bio':5,'Geom':4,'OBZ':5}
family=['Eudokia','Michail','Ivan','Alexander','Roman','Ekaterina','Ivan','Aleksey','Elena','Victor']
kit='Pirat'
print('Select mode 1-9')
#mode=int(input())
mode=6
def Mode1():       #Done
    avg_marks=sum(subj.values())/len(subj.values())
    print('Avg mark: ' + str(avg_marks))
    return 1
def Mode2():       #Done
    family.append('Egor')
    unique_names=set(family)
    family.remove('Egor')
    print(unique_names)
    return 1
def Mode3():
    sumnames=sum(subj.keys())
    print(len(sumnames))
    return 1
def Mode4():
    
    return 1
def Mode5():       #Done
    for ch in kit:
        print(bin(ord(ch)))
    return 1
def Mode6():        #Done
    print(sorted(family,reverse=True))
    return 1
def Mode7():       #Done
    date_old=datetime.datetime(day=30,month=1,year=2004)
    date=datetime.datetime.today()
    delta=(date-date_old).days
    print('Days from my BD: ' + str(delta))
    return 1
if mode==1:
    Mode1()
elif mode==2:
    Mode2()
elif mode==3:
    Mode3()
elif mode==4:
    Mode4()
elif mode==5:
    Mode5()
elif mode==6:
    Mode6()
elif mode==7:
    Mode7()