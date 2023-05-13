#!/usr/bin/env python
# coding: utf-8

# In[9]:



from datetime import datetime
from multiprocessing import Queue

Fio_date = ("Рябов Кирилл Артурович", 10, 3, 2003)
attestat = {
    'Английский язык': 3, 
    'Биология': 4,
    'География': 5,
    'Информатика': 4,
    'История': 3,
    'Литература': 4,
    'Математика': 5, 
    'Обж': 5, 
    'Обществознание': 3, 
    'Русский язык': 3, 
    'Физика': 4,
    'Физкультура': 5,
    'Химия': 4,}
fam_name = ["Миша", "Егор", "Вика", "Никита", "Света", "Маша"]
kiwi_name = "Бебрик"
print("Средняя оценка:", sum(attestat.values()) / len(attestat.values()))

print("Уникальные имена:", list(set(fam_name)))
school_mark_len = 0
for i in list(set(attestat)):
    school_mark_len += len(i)
    
print("Общая длина названий предметов:", school_mark_len)

all_school_len = ""
for i in list(attestat):
    all_school_len += i
print("Уникальные буквы названий предметов:", set(list(all_school_len)))

bin_result = ''.join(format(x, '08b') for x in bytearray(kiwi_name, 'utf-8'))
print("Имя домашней пушистой кивы в бинарном виде", bin_result)


fam_name.sort(reverse=True)
print("Отсортированный в обратном порядке алфавита список родственников:", fam_name)


print("Количество дней от даты рождения до текущей даты:",
      (datetime.now().date() - datetime(int(Fio_date[3]), int(Fio_date[2]), int(Fio_date[1])).date()))


FIFO = Queue()
print("Введите элементы для FIFO очереди. \n Чтобы прекратить введите: стоп.")
while True:
    i = input()
    if i != "стоп":
        FIFO.put(i)
    else:
        print("Очередь FIFO:")
        while not FIFO.empty():
            print(FIFO.get(), end=' ')
        break


Atstek_name = ['Tenoch',
               'Acamapochtli',
               'Huitzilihitl',
               'Chimalpopoca',
               'Xihuitl Temoc',
               'Itzcoatl',
               'Moctezuma I',
               'Atotoztli',
               'Axayacatl',
               'Tizoc', 
               'Ahuitzotl',
               'Moctezuma II',
               'Cuitlahuac',
               'Cuauhtrmoc',
               'Tlacotzin', 
               'Motelchiuhtzin',
               'Xochiquentzin',
               'Huanitzin', 
               'Tehuetzquititzin',
               'Cecetzin',
               'Cipac']
Atstek_num = (Fio_date[1] + (Fio_date[2]) ** 2 + Fio_date[3]) % 21 + 1
index_name = int(input("Введите индекс родственника которого хотите поменять на имя Ацтекского правителя:"))
fam_name[index_name] = Atstek_name[Atstek_num - 1]
print(fam_name)

my_list = {}
for i in range(len(fam_name)):
    if i == len(fam_name)-1:
        my_list[fam_name[i]] = None
    else:
        my_list[fam_name[i]] = i+1
print(my_list)

