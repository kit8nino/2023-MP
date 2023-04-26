#!/usr/bin/env python
# coding: utf-8

# In[58]:


import queue
from datetime import date


#ФИО, дата рождения
I = ("Барсуков Иван Владимирович", 22, 5, 2003) 

#предметы в аттестате
marks = {"русский язык": 4,"литература": 5,"алгебра": 4,"геометрия": 4,"физика": 5,"экспериментальная физика": 5,"Астрономия": 5,
          "история": 5,"химия": 5,"биология": 5,"информаика": 4,"обж": 5,"физкультура": 5,"обществознание": 5,"черчение": 5,
          "география": 5,"иностранный язык": 5} 

#имена родственников
My_family = ["Елена 1972", "Олег 1971", "Нина 1934", "Игорь 1969",
                "Денис 1995", "Андрей 2000"] 
 
#имя блохастика
Pitomec = "БелОк" 



#1.
total_grade = sum(marks.values()) #Сумма оценок
num_subjects = len(marks) #Количесво предметов(оценок)
average_grade = total_grade / num_subjects #Находим среднее аттестата
print("Средняя оценка:", average_grade)
print("")



#2.
names = []  # Создаем список имен из списка My_family, взяв только первое слово в каждой строке, и добавляем имя из кортежа I
for i in My_family:
    name = i.split()[0]
    names.append(name)
last_name = I[0].split()[1]
names.append(last_name)
unique_names = set(names) # находим имена
print("Уникальные имена среди родственников:", unique_names)
print("")


#3.
total_len = 0
for i in marks:  #Проходим по всем предметам
    total_len += len(i)  #Добовляю длину каждого названия
print("Общая длина всех названий предметов:", total_len)
print("")



#4 
unique_bukva = set() 
for i in marks: #Проходим по каждому предмету
    for j in i.lower():
        if j.isalpha(): #Добавляем букву если она есть в алфавите
            unique_bukva.add(j)
print("Уникальные буквы:", unique_bukva)
print("")



#5.
bini = ""
for i in range(len(Pitomec)):   # проходимся по каждому символу в строке
    byte = Pitomec[i].encode('utf-8')  # получаем байтовое представление символа
    for j in range(len(byte)):    # проходимся по каждому байту
        bini += format(byte[j], '08b')  # преобразуем каждый байт в его двоичное представление и добавляем его к строке binary
print("Имя в бинарном виде:", bini)
print("")



#6.
My_family.sort(reverse=True) #Сортирую список в обратном порядке
print("Cписок родственников в обратном порядке:", My_family)
print("")



#7.
today = date.today() #Объект для текущей даты
dr= date(I[3], I[2], I[1]) #Записываю сою дату рождения
d = today - dr #Вычислеение дней
print("Количество дней от даты рождения до текущей даты:", d.days)
print("")



#8. 
queue = []  # Создание пустой очереди
while True: # Пока  вводим индексы, добавляем их в очередь
    index = input("Введите индекс предмета (для остановки введите 'z'): ")
    if index == "z":
        break
    else:
        s = list(marks.keys())[int(index)]  # Находим предмет по введенному индексу и добавляем его в очередь
        queue.append(s)
print("Предметы:")
for i in queue:
    print(i)
print("")



#9 
aztec_rulers = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
                'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
                'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
                'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
index = int(input("Введите индекс от 0 до " + str(len(My_family) - 1) + ": ")) #Вычисляю индекс правителя
day, month, year = 22, 5, 2003 
n = (day + month ** 2 + year) % 21 + 1
if index in range(len(My_family)): #Проверяем корректность индекса
    My_family[index] = aztec_rulers[n]  #Меняем имя
    print("Обновленный список имен:", My_family) 
else: 
    print("Ошибка: индекс должен быть от 0 до", len(My_family) - 1)
print("")




#10

My_family = ["Елена 1972", "Олег 1971", "Нина 1934", "Игорь 1969",
                "Денис 1995", "Андрей 2000"] 
# создаем словарь
rel_d = {}
rel_list = sorted(My_family, key=lambda x: int(x.split()[1]))  # сортируем список по годам рождения

for i in range(len(rel_list)-1):
    rel_d[rel_list[i].split()[0]] = rel_list[i+1]  # присваиваем следующее имя в списке

# последний элемент связанного списка ссылается на первый элемент для образования замкнутого цикла
rel_d[rel_list[-1].split()[0]] = rel_list[0]
print("Cловарь, где каждому имени родственника соответствует ссылка на следующее имя в упорядоченном по годам рождения списке:")
# проверяем результат
for name, next_name in rel_d.items():
    print(name, next_name)
print("")




#11 
My_family1 = ["Елена ", "Олег ", "Нина ", "Игорь ", "Денис"]

def tribonacci():
    fio = "Барсуков Иван Владимирович"
    n = len(fio) * len(My_family1) % 4
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a + b + c  
for n in tribonacci():
    print("tribonacci",n)
print("")

def leonardo():
    fio = "Барсуков Иван Владимирович"
    n = len(fio) * len(My_family1) % 4   
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b + 1
for n in leonardo():
    print("leonardo",n)
print("")

def sylvester(n):
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = sum(2**i * a for i, a in enumerate(sylvester()))
        yield c + 1
n = len("Барсуков Иван Владимирович") * len(My_family1) % 4
sylvester_gen = (next(sylvester()) for i in range(n))  
for n in sylvester(n):
    print("sylvester",n)
print("")            
    
def aliquot(fio, My_family1):
    fio = "Барсуков Иван Владимирович"
    My_family1 = ["Елена ", "Олег ", "Нина ", "Игорь ", "Денис "]
    n = len(fio) * len(My_family1) % 4
    c = 0
    while True:
        if c % 2 == 0:
            yield fio[c // 2]
        else:
            yield My_family1[(c // 2) % len(My_family1)]
        c += 1
        if c % n == 0:
            c = 0    
            
            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 


# 

# In[ ]:




