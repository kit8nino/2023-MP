import datetime
import queue
import numpy as np

me=('Никита', 'Сергеевич', 'Соболев', '07', '04', '2004')
attestat={
    'Русский язык':5,
    'Литература':5,
    'Алгебра':5,
    'Геометрия':5,
    'Физика':5,
    'Информатика':5,
    'Химия':4,
    'Биология':4,
    'География':5,
    'Физическая культура':5,
    'ОБЖ':5,
    'Обществознание':4,
    'Музыка':5,
    'История':5,
    'Английский язык':4
    }
relatives=['Нина 1980','Сергей 1981','Галина 1946','Владимир 1947','Олег 1970','Ирина 1972','Тимур 2002','Роман 2014']
kiva="Ламарр"

#Задание №1 - Средняя оценка в аттестате
count=0
summa=0
for i,j in attestat.items():
    count += 1
    summa += int(j)
print("Средняя оценка атестата: ",summa/count, '\n')

#Задание №2 - Уникальные имена родственников
set_name = set(relatives) 
print("Уникальные имена среди моих родственников: ")
list_name = (list(set_name)) 
for item in list_name: 
    print(item)
print(me[0], me[5], '\n')

#Задание №3 - Общая длина всех названий предметов
lenght=0
for i in list(attestat):
    lenght+=(len(i))
print("Общая длина всех названий предметов: ",lenght,'\n')  

#Задание №4 - Уникальные буквы в названиях предметов
set_letters=set()
for subject in attestat:
    for letter in subject:
        set_letters.add(letter)
print('Уникальные буквы в названиях предметов -', set_letters, '\n')

#Задание №5 - Имя вашей домашней пушистой кивы в бинарном виде
m=list(kiva)
print("Имя моей домашней пушистой кивы в бинарном виде:", end=" ")
for i in range(0,len(kiva)):
    m[i]=int(ord(m[i]))
    m[i]=bin(m[i])
    print(m[i][2:], end=" ")
print('\n')
    
#Задание №6 - Отсортированный по алфавиту (в обратном порядке) список родственников
reverseList = sorted(relatives, reverse=True)
print('Реверсивый список имен: ', reverseList, '\n')

#Задание №7 - Количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)
date_now=datetime.date.today()
date_birth=datetime.date(int(me[5]),int(me[4]),int(me[3]))
print("Дней от моего рождения до сегодняшнего дня: ", (str(date_now-date_birth)).split()[0], '\n')

#Задание №8 - Вывод FIFO очереди
print("FIFO очередь, в которую можно добавляются предметы по вводимому с клавиатуры индексу (от 1 до 15, число вне интервала - команда остановки):", end=' ')
och=queue.Queue()
i=0
p=[0]*len(attestat)
j=0
for i in attestat.keys():
    p[j]=i
    j+=1
i=1
while (i>=1) and (i<=15):
    i=int(input())
    if (i>=1) and (i<=15):
        och.put(p[i-1])
    else:
        break
while not och.empty():
    print(och.get(), end=" ")
print('\n')

#Задание №9 - Смена имени на ацтекского правителя
number = (int(me[3]) + (int(me[4]))**2 + int(me[5])) % 21 + 1
aztec=['Tenōch','Ācamāpichtli','Huītzilihhuitl','Chīmalpopōca','Xīhuitl Tēmoc','Itzcōhuātl','Motēuczōma Ilhuicamīna',
       'Atotoztli','Āxāyacatl','Tīzocic','Āhuitzotl','Motēuczōma Xōcoyōtl','Cuitlāhuac','Cuāuhtēmoc','Tlacotzin',
       'Motelchiuhtzin', 'Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']
number_m = aztec[number-1]
index = int(input("Введите индекс родственника: "))
if index < len(reverseList) and index >= 0:
    name_parts = reverseList[index].split()
    name_parts[0] = f"{number_m}"
    reverseList[index] = " ".join(name_parts)
    print("Измененный список родственников: ", reverseList, '\n')
else:
    print("Индекс вне диапазона длины списка родственников.\n")

#Задание №10 - Связный список
sorted_relatives = sorted(relatives, key=lambda x: int(x.split()[-1]))
linked_list = {}
for i in range(len(sorted_relatives)-1):
    linked_list[sorted_relatives[i].split()[0]] = sorted_relatives[i+1].split()[0]
linked_list[sorted_relatives[-1].split()[0]] = None
print("Связанный список родственников: ", linked_list, '\n')

#Задание №11 - Функция генератор
num=(len(me[0])+len(me[1])+len(me[2]))*len(p)%4
#Аликвотная последовательность
def aliquot(generator):
    a = 0
    for i in range(10):
        yield a
        a = a +generator
        if a == 0:
            break       
#Последовательность Сильвестра
def sylvester():
    a = 2
    yield a
    for i in range(9):
        a = a * a + 1
        yield a        
#Числа трибоначчи
def tribonacci():
    a, b, c = 0, 0, 1
    yield a
    yield b
    yield c
    for i in range(7):
        d = a + b + c
        yield d
        a = b
        b = c
        c = d        
#Числа Леонардо
def leonardo():
    a, b = 1, 1
    yield a
    yield b
    for i in range(8):
        a, b = b, a + b + 1
        yield b
#Выбор нужной функции
if num == 0:
    sequence = aliquot(num)
    sequence_name = "аликвотной последовательности"
elif num == 1:
    sequence = sylvester()
    sequence_name = "последовательности Сильвестра"
elif num == 2:
    sequence = tribonacci()
    sequence_name = "числа трибоначчи"
else:
    sequence = leonardo()
    sequence_name = "числа Леонардо"

print("Была выбрана функция-генератор :", sequence_name)
for i, nm in enumerate(sequence):
    print(nm, end=' ')
    if i >= 9:
        break