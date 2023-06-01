import datetime
import queue
my_data = ("{Хереш Никита Андреевич}", 21, 4, 2003)

subject_grade = {
    "Русский": 4, 
    "литература": 5, 
    "алгебра": 4,
    "геометрия":4,
    "физика":4,
    "английиский":5,
    "химия":5,
    "биология":5,
    "информатика":5,
    "география":5,
    "обществознание":3,
    "история России": 5,
    "Всемирная история": 5,
    "ОБЖ": 5,
    "Экономика": 5,
    "Физкультура":5
    }
family_names = ["Андрей", "Алексей", "Полина","Светлана","Надежда" ,"Илья", "Александр","Никита"]
kiwa_name = "Микки"

#1
average_grade = sum(subject_grade.values()) / len(subject_grade.values())
print('Средняя оценка по аттестату: '+ str(average_grade)+'\n')

#2
unique_names = []
for name in family_names:
    if name in unique_names:
        continue
    unique_names.append(name)
print('Уникальные имена среди своих родственников: ')
u_names=set(family_names)
for i in u_names:
    print(i)

#3
lenght=0
for i in list(subject_grade):
    lenght+=(len(i))
print('Общая длина всех названий предметов: ',lenght)


#4


letters_subject=[]
for i in list(subject_grade):
     letters_subject.extend( list(set(i)))
unique_letters=set(letters_subject)
print('Уникальные буквы в названиях предметов: ',*unique_letters)
   
#5    

print('Имя домашней пушистой кивы в бинарном виде:'+'\n')
kiwa_bin = ''.join(format(ord(char), '08b') for char in kiwa_name)
print(kiwa_bin)

#6

sorted_names=sorted(list(family_names),reverse=True)



print('Отсортированный по алфавиту (в обратном порядке) список родственников: ')
for i in sorted_names:
    print(i)
    
#7

date_now=datetime.datetime.today()
date_old=datetime.datetime(day=21,month=4,year=2003)
print('Количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной): ',date_now-date_old)

#8


q=queue.Queue()

for i in list(subject_grade):
    q.put(i)
print('Добавьте предмет ')

print('Добавляем новые элементы к очереди ')

while True:
    subject=input('Нажмите Enter,чтобы прекратить ввод с клавиатуры: ')
    if subject=='':
        break
    else:
        q.put(subject)

print('Выввод всех предметов:')
while True:
    print(q.get())
    if q.empty()==True:
        break

#9 

print('по введенному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя',end='')

Acteck_names=['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
i=int(input('Введите индекс списка имен Родственников, отсортированный по алфавиту : '))

n=(my_data[1]+(my_data[2])**2+my_data[3])%21+1


sorted_names[i]=Acteck_names[n-1]
print(sorted_names)

#10

print('Cоздать связной список, например, как словарь, где - ключ имя родственника, значение (ссылка на следующий элемент) - индекс имени по исходному списку, упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться ')

family_names_by = { "Андрей" :1, "Алексей":2, "Полина":3,"Светлана":4,"Надежда":5 ,"Илья":6, "Александр":7,"Никита":0}

print(family_names_by)
    
#11


print('Написать функцию-генератор')
number=len(my_data[0])*len(family_names)%4
print(number)

def divisors(n):
    for i in range(1,n):
        if n % i==0:
            yield i

n=int(input('Введите значение числа n ,с которого начнётся последовательность n= '))
count=0
aliquot_sequence=[]

while n!=0:
    a=0
    for i in divisors(n):
        a += i
    n=a
    aliquot_sequence.append(a)
    count+=1
    
    if count==500:
        break
print(aliquot_sequence)
