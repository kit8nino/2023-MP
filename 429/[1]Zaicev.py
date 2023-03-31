# Исходные данные

Date = ("Зайцев", "Владислав", "Владимирович",9,4,2003)
attestate = {"Алгебра": 5,
             "Геометрия": 5,
             "География": 5,
             "Физкультура": 5,
             "Биология": 5,
             "Информатика": 5,
             "Литература": 5,
             "Основы Безпасности Жизни": 5,
             "Химия": 5,
             "Русский": 4,
             "Физика": 4,
             "Астрономия": 5,
             "Графика": 5,
             "Мировая художественная культура": 5           
             }
Names = ["Татьяна", "Владимир", "Владислав", "Дарья"]
NameOfKiva = "Йетя"

# Действия с данными

import datetime

###
count = 0
for key in attestate.values():
    count += key
print("Средняя оценка: ", count/(len(attestate)))
###

print("\n")

###
UnikNames = set(Names)
print("Уникальные имена: ",UnikNames)
###

print("\n")

###
count = 0
for key in attestate.keys():
    count += len(key)
print("Общая длина предметов: ", count)
###

print("\n")

###
UnikWords = set()
for key in attestate.keys():
    L = len(key)
    for i in range(L):
        UnikWords.add(key[i])
print("Уникальные буквы: ",UnikWords)
###

print("\n")


###
bin_result = ''.join(format(ord(x), '08b') for x in NameOfKiva)
print("Имя Кивы в двоичном виде:", bin_result)
###

print("\n")

###
Names.sort()
print("Отсвортированные имена: ", Names)
###

print("\n")

###
date1 = datetime.datetime(day = Date[3],month = Date[4],year = Date[5])
date_now = datetime.datetime.now()
print("Количество дней от вашей даты рождения до текущей даты: ", (date_now - date1).days)
###

print("\n")

###
arr = []
a = (input("Введите число (для выхода введите 00): "))
while a != '00' :
    arr.append(a)
    a = (input("Введите число (для выхода введите 00): "))
for i in arr:
    print(i)
###

print("\n")

###

ind = int(input("Введите индекс (от 1 до 4): "))
Names[ind-1] = "Cuitláhuac"
#number = (date1.day + date1.month**2 + date1.year) % 21 + 1
#print(number) # 13
print(Names)

###


l = {"Татьяна" : 1980 , "Владимир" :  1972, "Дарья" : 2011}

l_sorted = sorted(l.items(), key = lambda x: x[1])

linked_list = {}
for i in range(len(l_sorted)):
    if i == len(l_sorted) - 1:
        linked_list[l_sorted[i][0]] = None
    else:
        linked_list[l_sorted[i][0]] = l_sorted[i+1][0]

print("\nСвязный список: ", linked_list)

###


Names = ["Татьяна", "Владимир", "Владислав", "Дарья"]

#number = len("Зайцев Владислав Владимирович") * len (Names) % 4    ## 0

n = int(input("\nВведите число для построения аликвотной последовательности: "))

posled = []

for i in range(1,n):
    if n % i == 0:
        posled.append(i)
        
print(posled)
               


