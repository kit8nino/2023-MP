"""
Сделано совместно с Кириллом Утросиным - Kirill-U-S
"""
import datetime
from datetime import date

# ФИО, число, месяц, год рождения
t = ["Фадин", "Владислав", "Васильевич", "24", "9", "2003"]
data = tuple(t)


# Предметы в школьном аттестате
atest = {"Алгебра" : 4, "Англ" : 5, "Биология" : 4, "Всеобщая история" : 5, "География" : 4, "Геометрия" : 4, "Информатика" : 5, "История России" : 4, "Литература" : 4, "ОИД" : 4, "Обществознание" : 4, "Письменная речь" : 3, "Решание задач" : 4, "Русский" : 4, "Физика" : 3, "Физра" : 5, "Химия" : 3}

# Имена родственников и их год рождения
tree = ['Светлана 1978','Василий 1978','Галина 1951',
        'Дмитрий 1945','Галина 1950','Юрий 1950',
        'Алиса 2004','Лиза 1998','Екатерина 1980',
        'Михаил 1977','Виталий 1972','Наташа 1978']

# Кива
kiwa = 'Кактус'

# Задание 1
avm = 0
count = 0
for key in atest:
     avm += atest[key]
     count += 1
print('Средняя оценка:', avm / count)


# Задание 2
name = ''
unic = ''
j = 0
tree2 = []

for i in range(len(tree)):
    name = tree[i]
    while name[j] != ' ':
        unic += name[j]
        j += 1
    tree2.append(unic)
    unic = ''
    j = 0
#print(tree2)

tree3 = []
for i in tree2:
    if i not in tree3:
        tree3.append(i)
print('\n','Уникальные имена: ','\n',tree3, 'Владислав')

#Задание 3
count = 0
for key in atest.keys():
    count += len(key)
    for i in range(len(key)):
        if key[i] == ' ':
            count = count -1 
print('\n','Общая длина всех названий предметов: ',count)

#Задание 4
ltr = ''
ltrm = []
unltrm = []
for key in atest.keys():
    for i in range(len(key)):
        if key[i] not in unltrm:
            unltrm.append(key[i])

print('\n','Уникальные буквы предметов: ')
for i in range(len(unltrm)):
    print(unltrm[i],'|', end = ' ')

#Задание 5

bin_kiwa = ''.join(format(x,'08b') for x in bytearray(kiwa, 'utf-8'))
print('\n','\n','Бинарная Кива: ', bin_kiwa)

#Задание 6
sort_tree = tree
sort_tree.sort()
sort_tree.reverse()
print('\n','Сортированные родственники: ','\n' ,sort_tree)

#Задание 7
prev_date = datetime.date(2003, 9, 24)
now_date = date.today()
print('\n','Дней с др: ', now_date - prev_date, '\n')

#Задание 8
queue = []

while True:
    index = input('Введие индекс: ')
    if index == 'stop':
        break
    elif index not in atest.keys():
        print('Такого предмета нет в словаре')
    else:
        queue.append(index)

if queue:
    print('\n',"Добавленные предметы: ")
    for item in queue:
        print(item)
else:
    print('\n',"Очередь пуста")

#Задание 9 Axayacatl
ind = (24 + 9**2 + 2003) % 21 + 1
actec = ["Tenoch","Acamapichtli","Huitzilihuitl","Chimalpopoca","Xihuitl Temoc","Itzcoatl","Moctezuma I","Atotoztli",
      "Axayacatl","Tizoc","Ahuitzotl","	Moctezuma II","Cuitláhuac","Cuauhtémoc","Tlacotzin",
      "Motelchiuhtzin","Huanitzin","Tehuetzquititzin","Cecetzin","Cipac"]
print('\n','Номер Ацтека: ', ind)
print('Введите номер родственника, что хотите сделать ацтеком: ')
act = int(input())
dt1 = ''
dt2 = ''
n = len(sort_tree[act-1])
old_actec = sort_tree[act-1]

while old_actec[n-1] != ' ':
    dt1 = dt1 + old_actec[n-1]
    n = n - 1
for i in range(len(dt1), 0, -1):
    dt2 += dt1[i-1]

    
new_actec = actec[ind-1] + ' ' + dt2
sort_tree[act - 1] = new_actec
print('\n', '+1 Ацтек: ',sort_tree)

#Задание 10 
print('\n','Связный список: ')
unlinked_tree = {"Светлана": 1978,"Василий": 1978, "Галина": 1951,
            "Дмитрий": 1945, "Галина": 1950, "Юрий": 1950,
            "Алиса": 2004, "Лиза": 1998, "Екатерина": 1980,
            "Михаил": 1977, "Виталий": 1972, "Натана": 1978}
sorted_unlinked_tree = sorted(unlinked_tree.items(), key = lambda x: x[1])

linked_tree = {}

for i, item in enumerate(sorted_unlinked_tree):
    name = item[0]
    if i < len(sorted_unlinked_tree) - 1:
        next_index = i + 1
        next_name = sorted_unlinked_tree[next_index][0]
        linked_tree[name] = next_name
    else:
        linked_tree[name] = None

for i, j in linked_tree.items():
    print(i, "→", j)


#Задание 11
family_names = ''
FIO = ''

for i in range(len(t) - 3):
    FIO += t[i]
#print(FIO)
for str in tree2:
    family_names += str
#print(family_names)
number = len(FIO) * len (family_names) % 4
print('\n','Номер варианта: ',number)

def aliquote(xp):
    sumx = 0
    for i in range(1, xp):
        if xp % i ==0:
            sumx += i
    xc = sumx
    if xc == 0:
        return 0
    print(xc)
    return aliquote(xc)

start = int(input('Введите число: '))
x = aliquote(start)
print(x)









