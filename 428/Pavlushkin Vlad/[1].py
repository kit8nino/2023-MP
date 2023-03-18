#!/usr/bin/env python
# coding: utf-8

# In[2]:


#создание кортежа
#list кортеж превращает в список
#tuple список превращает в кортеж
from datetime import datetime, date, time
tuple=("Павлушкин Владислав Александрович",4 ,6, 2003)

#словари ключ-значение
dict={"алгебра":4,"геометрия":4,"русский язык":5,"обж":5,"литература":5,"физкультура":5,"информатика":5,"пение":5,"история":5,
     "обществознание":5,"английский язык":5,"физика":5,"краеведение":5,"технология":5}
family_names=['Александр','Ирина','Олеся','Эрик','Юрий','Алина','Василий','Валентина']
s_kiv="ASYA"
average_mark=sum(dict.values())/len(dict.values())
print("средняя оценка в аттестате:",average_mark)
unique_names=[]
for name in family_names:
    if name in unique_names:
        continue
    else:
        unique_names.append(name)
uniue_char = list(set(dict)) 
langs = set()

[langs.update(set(x) if isinstance(x, (list, set)) else [x])
 for x in dict.values()]

print(langs)

print("уникальные имена среди родственников:",unique_names)
print("общая длина всех названий предметов:",len(''.join(dict)))###объединили сптсок строк в одну строку и получили её длину
print("уникальные буквы:",rr)
print("бинарный код:")
for ch in bytearray(s_kiv,'utf-8'):#### ,бинарный код
    
    print(bin(ch))
sorted_names=sorted(family_names)
family_names.sort()
print(" отсортированный по алфавиту (в обратном порядке) список родственников:",list(reversed(sorted_names)))
date1=datetime(day=4,month=6,year=2003)
date2=datetime.now()
timedelta=date2-date1
print(timedelta)


# 

# In[ ]:




