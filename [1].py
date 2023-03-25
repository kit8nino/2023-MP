#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import datetime
from collections import deque
import queue
q=queue.Queue()
queue = deque()


# исходные данные
FIO = ("Панова Кристина Андреевна", 1,11,2002)
marks = {"физра": 4,
         "география": 4,
         "геометрия": 4,
         "информатика": 4,
         "аглебра": 5,
         "физика" : 4,
         "английский язык" : 5,
         "биология" : 5,
         "история России" : 5,
         "всеобщая история" : 5,
         "русский язык" : 4,
         "химия" : 4,
         "обществознание" : 4,
         "литература" : 4}
family_list = ["Ирина 1977", "Андрей 1976", "Надежда 1957", "Алексей 1955", "Наталья 1984", "Павел 1986"]
kiwa_name = "даздраперма"
aztec_names = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
# действия
print("=====1=====")
average_rating = sum(marks.values())/len(marks.values())
print("Средняя оценка:", average_rating, "\n")

print("=====2=====")
unique_names = list(set(family_list))
print("Уникальные имена родственников:", unique_names, "\n")

print("=====3=====")
length = sum([len(marks) for marks in marks.keys()])
print(f"Общая длина всех названий предметов: {length} \n")

print("=====4=====")
n = 0
lenght_name_marks = [0]*len(marks.values())
name_marks_string = ""
for i in marks.keys():
    for n in range(14):
        lenght_name_marks[n] = i
        name_marks_string += lenght_name_marks[n]

unique_letter = {}
for letter in name_marks_string:
    if letter in unique_letter:
        unique_letter[letter]+=1
    else:
        unique_letter[letter]=1
print(f"Уникальные буквы в названиях предметов: {', '.join(unique_letter)} \n")

print("=====5=====")
binary_kiwa_name = ''.join(format(ord(letter), '08b') for letter in kiwa_name)
print(f"Имя пушистой кивы в бинарном виде: {binary_kiwa_name} \n")

print("=====6=====")
family.sort(reverse=True)
print("Отсортированный по алфавиту в обратном порядке список родственников:\n", family, "\n")

print("=====7=====")
print("Количество дней от даты рождения до текущей даты: {}".format((datetime.now() - datetime(day=int(FIO[1]), month=int(FIO[2]), year=int(FIO[3]))).days), "\n")

print("=====8=====")
while True:
    item = input("Введите предмет (или 'stop' для завершения): ")
    if item == "stop":
        break
    try:
        n=1
        queue.insert(n,item)
    except ValueError:
        queue.append(item)

print("FIFO Очередь:")
for item in queue:
    print(item)

print("=====9=====")
number = (int(FIO[1]) + int(FIO[2])**2 + int(FIO[3])) % 21 + 1
print("Индекс имени ацтека:", number, "\nВыбранное имя ацтека =>", aztec_names[number])
index = int(input("Введите число от 0 до 11:"))
family[index] = aztec_names[number]
print("Обновленный список имён:", family, "\n")

print("=====10=====")
family_new = {"Наталья 1984": 1, "Павел 1986": 2, "Алексей 1955": 3, "Надежда 1957": 4,"Ирина 1977": 6, "Андрей 1976": 5, "Кристина 2002": 0}
print("Список, упорядоченный по годам рождения:", family_new, "\n")

print("=====11=====")
number = len(FIO[0])*len(family)%4
print(number,"=> Выбранная функция-генератор - последовательность Сильвестра")
def sylvester():
    x = 2
    yield x
    for i in range(9):
        x = x * x + 1
        yield x

for i, num in enumerate(sylvester()):
    print(num, end=' ')
    if i >= 5:
        break


# In[ ]:




