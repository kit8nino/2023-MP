import queue
from datetime import datetime, date, time
###свои ФИО, число, месяц, год рождения в виде кортежа;
date_of_burn=("Павлушкин Владислав Александрович",4 ,6, 2003)

#словари ключ-значение
###предметы в школьном аттестате (не меньше 14), как словарь из названия и оценки
dict={"алгебра":4,"геометрия":4,"русский язык":5,"обж":5,"литература":5,"физкультура":5,"информатика":5,"пение":5,"история":5,
     "обществознание":5,"английский язык":5,"физика":5,"краеведение":5,"технология":5}
###имена (только) ближайших (до двоюродных включительно) родственников в списке;
family_names=['Александр 1968','Ирина1968','Олеся 1992','Эрик 1958','Юрий 1978','Алина 2004','Василий 1943','Валентина 1947']
###имя, которое вы бы дали своей домашней пушистой киве (строка).
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
print("уникальные буквы:",)
print("бинарный код:")
for ch in bytearray(s_kiv,'utf-8'):#### ,бинарный код
    
    print(bin(ch))
sorted_names=sorted(family_names)###отсортированный по алфавиту (в обратном порядке) список родственников;
family_names.sort()
print(" отсортированный по алфавиту (в обратном порядке) список родственников:",list(reversed(sorted_names)))
today = date.today()
  
# Storing the specific date
graduation_day = date(2003, 6, 4)
days_left = abs(graduation_day - today)

print("7)" ,days_left)
###8
q = queue.Queue()
print('   Чтобы прекратить на любую клавишу: ')
for i in list(dict):
    q.put(i)
while True:
    sub = input('   ')
    if sub == '':
        break
    else:
        q.put(sub)
print("8) FIFO очередь из всех предметов: ")
while True:
    print(q.get(), end=', ')
    if q.empty()==True:
        break
print('\n')
###9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя (смотреть по списку всех на странице https://en.wikipedia.org/wiki/List_of_rulers_of_Tenochtitlan) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;
ac_pravit=['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
num=(int(date_of_burn[1]) + int(date_of_burn[2])**2 + int(date_of_burn[3])) % 21 + 1
ind=int(input('Введите индекс от 0 до 7:'))
if ind<0 or ind>7:
    print("такого индекса нет")
else:
    family_names[ind] = ac_pravit[num]
    print("9) новый список имён:",  family_names)
###10
relatives={'Василий 1943':1,'Валентина 1947':2,'Эрик 1957':3,'Александр 1968':4,'Ирина 1968':5,'Юрий 1978':6,'Олеся 1992':7,'Алина 2004':0}
print("10)Новый список имён",relatives)

print("11)функцию-генератор, вариант определяется как number = len(ФИО) * len (family_names) % 4:)")
val=len(date_of_burn[0]) * len (family_names) % 4
print(numberr,"Число в формуле генератора-Аликводная последовательность")
if val==0:
    def generator(val):
        b = 0
        T=10
        for i in range(T):
            yield b
            b = b + val
            if b == 0:
                break



