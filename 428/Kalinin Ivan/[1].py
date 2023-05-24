from datetime import datetime
import math
my_data = ("Калини Иван Иванович", 2003, 8, 8 )
marks = { "русский язык": 5,
         "математика":5, 
         "география ": 5, 
         "химия ":5,
         "геометрия": 5,
         "английский язык": 5,
         "биология": 5,
         "литература": 5,
         "физика": 5,
         "физическая культура": 5,
         "ОБЖ": 5,
         "история": 5,
         "информатика": 5,
         "экономика": 5,
         
         }
family_names = ["Иван 2003", "Иван 1983","Мария 1984","Михаил 2014","Анна 2020","Людмила 1967",
                "Антонина 1946","Александр 1961","Юрий 1980","Данил 2005","Полина 2010","Евгения 1993",
                "Дмитрий 1991","Андрей 1965","Елизавета 2021"]
family_years = {"Иван"}
kiwa_name = "Плюмбус"

# 1 -----------------Средний балл-------------------

print("1.Средний балл -->", sum(marks.values())/len(marks))

# 2 ---------------Уникальные Имена----------------------

only_family_names = []
for i in range(len(family_names)):
    index_spc = family_names[i].index(" ")
    name = family_names[i][:index_spc]
    only_family_names.append(name)
    
print("\n2.Уникальные имена -->", list(set(only_family_names)))

# 3 ------------Уникальные буквы и длинна названий предметов-------------

all_chars=[]
char=0
for key in marks:
    for j in key:
        if j ==" ":
            continue
        char+=1
        all_chars.append(j)
        
# 4 ----------Общая длинна названия предметов------------------------

print("\n3.Общая длинна названий предметов -->", char)
c=0
unicue_chars = []
for chars in all_chars:
    if all_chars.count(chars) ==1:
        unicue_chars.append(chars)
print("\n4.Уникальные буквы -->.",unicue_chars)

# 5 ----------------Имя пушистой кивы в двоичном виде--------------------

bin_kiwa = ''.join(format(x,'08b') for x in bytearray(kiwa_name,'utf-8')) 
print("\n5.Имя пушистой Кивы в двоичном коде -->",bin_kiwa)

# 6 ---------сортировать в обратном алфавитном порядке список родвстенников-----------

sorted_family_names = list(reversed(sorted(only_family_names)))
print("\n6.Отсортированные в обратном алфавитном порядке имена -->", sorted_family_names)

# 7 ---------------------Число дней от дня рождения-----------------------------

now=datetime.now()
my_birthday = datetime(my_data[1], my_data[2], my_data[3])
delta_dates = now - my_birthday
print("\n7.Число дней от моего дня рожления -->",delta_dates.days)


# 8 --------- Fifo последовательность ------------------

import queue
marks_keys_list = list(marks.keys())
q = queue.Queue()

true = True
while true:   
    i = input("Введите индекс \nЧтобы завершить, введите пробел ")
    print("\n")
    if i == " ":
        true = False
        continue
    if int(i) > len(marks):
        print("Ошибка - индекс должен быть меньше", len(marks))
        continue
    q.put(marks_keys_list[int(i)-1])
print("8. FIFO очередь из  предметов: ")
while not q.empty():
    print(q.get(), end=', ')
    
# 9 --------------- Замена имени под введенным индексом на имя Ацтекского правителя -----------------

Actek_names = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
index = int(input("9.Введите индекс"))
if index > len(sorted_family_names) or index < 0:
    print("Ошибка - индекс должен быть меньше",len(sorted_family_names) )
    index = int(input("9.Введите индекс"))
    
number = (int(my_data[2]) + int(my_data[3])**2 + int(my_data[1])) % 21 + 1
sorted_family_names[index]=Actek_names[number]
print("Индекс из моей даты рождения=", number)
print(sorted_family_names)

#10 создать связный список, например, как словарь, где ключ - имя родственника, а значение (ссылка на следующий элемент) -
# индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться неизменным

family_names_new = [['', 0] for i in range(len(family_names))]

for i in range(len(family_names)):
        split_str=str(family_names[i]).split()
        family_names_new[i][1]=int(split_str[1])
        family_names_new[i][0]=split_str[0]

family_names_new.sort(key = lambda x: x[1])

for i in range(len(family_names)):
    family_names_new[i]=str(family_names_new[i][0]) +" "+ str(family_names_new[i][1])
    
#print("Отсортированный", family_names_new)

family_dict = [{'key': 0} for k in range(len(family_names))]  # входные данные

final_family_dict = {family_names_new[x]:x+1 
                     for x in range(len(family_names)-1)}
final_family_dict.update({family_names_new[len(family_names)-1]:0})
print("\n9. Связный список отсортированных по годам рождения родственников ->", final_family_dict)

#11 --------------Функция - генератор------------

number = len(my_data)*len(family_names)%4


def get_divisors(n): #функция нахождения всех делителей
    posl=[]
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            posl.append(i)
    return posl
def alicvot(n): #Аликвотная последовательность
     posled=[n]
     element=n
     while True:
         element = sum(get_divisors(element))

         posled.append(element)
         if element==1:
             break
     return(posled)

def silvestra(x): #Последовательность Сильвестра
    element = 2
    posled=[element]
    for i in range(x):
        posled.append(math.prod(posled)+1)
        element+=1
    return posled

def tribonachi(x): #Последовательнсть Трибоначчи
    posled=[0, 1]
    for k in range(x-2):
        i=k+2
        posled.append(posled[i-1]+posled[i-2])
    return posled


print("\n11. Моя последовательность номер ", number)
if number == 0:
    print("Аликвотная последовательность->", alicvot(20))
if number == 1: 
    print("Последовательность Сильвестра->", silvestra(5))
if number == 2: 
    print("Последовательнсть Трибоначчи->", tribonachi(10))