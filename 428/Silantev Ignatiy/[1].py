#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
from collections import deque
import random

f_name = ("Силантьев Игнатий Андреевич", 9, 6, 2003)

subs = ['Математика', 'Физика', 'Химия', 'История России', 'География', 
            'Литература', 'Русский язык', 'Английский язык', 'Физическая культура', 
            'Информатика', 'Обществознание', 'Биология', 'Технология', 'Музыка']
grad = [5, 4, 4, 4, 5, 4, 5, 5, 5, 4, 4, 4, 5, 5]

full_house = ["Сергей 1988", "Виктор 1950", "Олег 2000", 
              "Максим 2002", "Анастасия 1996", "Виктория 1999", 
              "Святослав 2009", "Даниил 2011", "Дмитрий 1977"]

nameKiwi = "Киви"

#       1 вывести среднюю оценку в аттестате

average_gr = sum(grad) / len(grad)
print("1) Средняя оценка по всем предметам: ", average_gr)
print(" ")

#       2 вывести уникальные имена среди своих родственников

unique_people = list(set(full_house))
print("2) Уникальное имя родственника: ", random.choice(unique_people))
print(" ")

#       3 общая длина всех названий предметов

summ = 0
for sub in subs:
    summ += len(sub)
print("3) Общая длина всех предметов: ", summ)
print(" ")

#       4 уникальные буквы в названиях предметов 

unique_let = set()
for sub in subs:
    for letter in sub:
        unique_let.add(letter)
print("4) Уникальные буквы предметов: ", unique_let)
print(" ")

#       5 имя вашей домашней пушистой кивы в бинарном виде

binary = ''.join([format(ord(i), '08b') for i in nameKiwi])
print("5) Имя 'Папич' в бинароном виде: ", binary)
print(" ")

#       6 отсортированный по алфавиту (в обратном порядке) список родственников;

full_house.sort(reverse=True)
print("6) Отсортированный список родственников:", full_house)
print(" ")

#       7 количество дней от вашей даты рождения до текущей даты 
#   (должна быть всегда актуальной);

birthdate = datetime(2002, 11, 13)
today = datetime.now()
days = (today - birthdate).days
print("7) Количество дней с даты рождения до текущей даты:", days)
print(" ")

#       8 FIFO очередь, в которую можно добавлять предметы по вводимому 
#   с клавиатуры индексу (до команды остановки), после введения - вывести все;

print("8)")
queue = deque()
while True:
    index = input("Введите индекс для добавления элемента или 'стоп' для остановки: ")
    if index == "стоп":
        break
    else:
        try:
            index = int(index)
            item = input("Введите элемент для добавления: ")
            queue.insert(index, item)
        except ValueError:
            print("Неверный индекс. Пожалуйста, введите число.")

print("Содержимое очереди:")
for item in queue:
    print(item)
print(" ")

#       9 по введеному индексу, поменять имя в отсортированном списке 
#   родственников на имя ацтекского правителя под номером, получаемым из 
#   вашей даты рождения: number = (day + month**2 + year) % 21 + 1;

at = ["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Itzcoatl", "Moctezuma I", 
          "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac",
          "Cuauhtémoc", "Coanococh", "Tlacotzin", "Quaquapitzahuac", 
          "Tecuichpoch I", "Huēnexōchitl", "Cihuacoatl", "Tlacaelel",
          "Tizoc", "Tlacopan"]

day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

number = (day + month ** 2 + year) % 21 + 1

index = int(input("Введите индекс для замены имени: "))
if 0 <= index < len(full_house):
    full_house[index-1] = at[number - 1]
    print("Обновленный список родственников:", full_house)
else:
    print("Неверный индекс.")
print(" ")

#       10 создать связный список, например, как словарь, 
#   где ключ - имя родственника, а значение (ссылка на следующий элемент) - 
#   индекс следующего имени по исходному списку, упорядоченному по их 
#   (родственников) годам рождения), исходный список при этом должен остаться 
#   неизменным;

full_house1= ["Сергей 1988", "Виктор 1950", "Олег 2000", 
              "Максим 2002", "Анастасия 1996", "Виктория 1999", 
              "Святослав 2009", "Даниил 2011", "Дмитрий 1977"]

relatives = []
birth_years = []
for item in full_house1:
    name, year = item.split()
    relatives.append(name)
    birth_years.append(int(year))

sorted_indices = sorted(range(len(relatives)), key=lambda i: birth_years[i])
linked_list = {}
for i in range(len(sorted_indices) - 1):
    name = relatives[sorted_indices[i]]
    next_index = sorted_indices[i + 1]
    linked_list[name] = next_index

print("Связный список:", linked_list)
print(" ")


#       11 написать функцию-генератор, свой вариант определяется 
#   как number = len("ФИО") * len (family_names) % 4:
#   аликвотной последовательности;
#   последовательности Сильвестра;
#   числа трибоначчи;
#   числа Леонардо.

generator = len(f_name[0]) * len(subs) % 4 

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

if generator == 0:
    sequence = aliquot(generator)
    sequence_name = "аликвотной последовательности"
elif generator == 1:
    sequence = sylvester()
    sequence_name = "последовательности Сильвестра"
elif generator == 2:
    sequence = tribonacci()
    sequence_name = "числа трибоначчи"
else:
    sequence = leonardo()
    sequence_name = "числа Леонардо"

print("11) Была выбрана функция-генератор: ", sequence_name)
for i, num in enumerate(sequence):
    print(num, end=' ')
    if i >= 9:
        break
print(" ")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




