import datetime as dt
import queue as qu

NSN_tuple = ('Руменяцев Александр Михайлович',15,6,2002)
SM = {
    'Алгебра':5,
    'Геометрия':4,
    'Физика':4,
    'География':4,
    'Биология':5,
    'Химия':3,
    'Физ-ра':5,
    'Информатика':1,
    'История России':3,
    'Всеобщая История':4,
    'Обществознание':3,
    'Русский':3,
    'Литература':4,
    'Астрономия':5,
    'Технология':4,
}
family_names = {'Никита 2001','Илья 1998','Александр 1998','Андрей 1977','Лена 1966','Дмитрий 1987','Андрей 1956', 'Татьяна 1973'}

Kiwa = "Bobs"

SM_Summ_Marks = 0

# 1 вывести среднюю оценку в аттестате

for value in SM.values():
    SM_Summ_Marks += int(value)
    
print("1)Средняя оценка = ", SM_Summ_Marks/len(SM),"\n")

# 2 вывести уникальные имена среди своих родственников (включая свое)
unique_names = []
names = []
for name in family_names:
    if name not in names:
        names.append(name.split(' ')[0])
unique_names = set(names)        
print("2)Уникальные имена родственников: ", unique_names,"\n")
    
# 3 общая длина всех названий предметов

SM_Summ_NLength = 0

for key in SM.keys():
    SM_Summ_NLength +=int(len(key))
    
print("3)Общая длинна названий всех предметов = ", SM_Summ_NLength,'\n')

# 4 уникальные буквы в названиях предметов

unique_letters = []
for key in SM:
    for let in key:
        if let not in unique_letters:
            unique_letters.append(let)
print("4)Уникальные буквы в названиях предметов", unique_letters, "\n")            

# 5 имя вашей домашней пушистой кивы в бинарном виде

print("5)Имя кивы в бинарном виде ", ''.join(format(ord(x), 'b') for x in Kiwa),'\n')

# 6 отсортированный по алфавиту (в обратном порядке) список родственников

sorted_names = sorted(unique_names ,reverse = True)
print("6)Список родственников в обратном алфавитном порядке:",sorted_names, "\n")

# 7 количество дней от вашей даты рождения до текущей даты

born = dt.date(int(NSN_tuple[3]),int(NSN_tuple[2]),int(NSN_tuple[1]))
today_date = dt.date.today()
amount_days = today_date - born
print("7)Дней от даты рождения", str(amount_days).split(' ')[0], "\n")

# 8 FIFO

items = qu.Queue()
item = input("8) FIFO| Для завершения введите Пробел\n")
while item != " ":
    items.put(item)
    item = input()
while not items.empty():
    print (items.get(), end = " ")

# 9 поменять имя в списке родственников на имя ацтекского правителя

number = (NSN_tuple[1] + NSN_tuple[2] ** 2 + NSN_tuple[3]) % 21 + 1
rulers = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]
print ("\n9) Чтобы поменять имя введите число")
index = int(input())
index = index % len(sorted_names)
sorted_names[index] = rulers[number - 1]
print (sorted_names, "\n")

# 10

relatives_dict = {}
sorted_relatives = sorted(family_names, key=lambda x: int(x.split()[1]))
print('10) Упорядоченный список родственников по годам рождения:', sorted_relatives)
for i in range(len(sorted_relatives) - 1):
    relatives_dict[sorted_relatives[i]] = sorted_relatives.index(sorted_relatives[i+1])
relatives_dict[sorted_relatives[-1]] = 0
print(' Связный список, где ключ - имя родственника, а значение индекс следующего имени по исходному списку:', relatives_dict, "\n")

# 11 написать функцию-генератор
generator_variant = len(NSN_tuple) * len (family_names) % 4
print ("11)","номер варианта: ", generator_variant)
print("Введите первое число последовательности")
start = int(input())
while start != 1:
    summ = 0
    for i in range(1,start//2+1):
        if start % i == 0:
            summ += i
    print(summ)
    start = summ
