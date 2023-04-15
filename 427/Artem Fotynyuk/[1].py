from datetime import datetime
import queue

my_name=('Фотынюк Артём Сергеевич','23','11','2003')
my_birth=datetime(2003,11,23)
my_subjects={
    "Русский язык":5,
    "Литература":4,
    "Алгебра":5,
    "Физика":4,
    "Химия":3,  
    "Геометрия":5,
    "География":5,
    "Физическая кульута":5,
    "ОБЖ":5,
    "Обществознание":4,
    "Музыка":5,
    "Искусство":5,
    "История":5,
    "Английский язык":5
    }
my_family=['Сергей','Наталья','Дарья','Юрий','Валентина','Дарья','Сергей','Артём']
kiva_name=('Катя')

#Задание №1 - Средняя оценка в аттестате
print('\n')
average_grade=sum(my_subjects.values())/len(my_subjects.values())
print("Средняя оценка в аттестате:", average_grade)
print('\n')

#Задание №2 - Уникальные имена родственников 
unique_family=[]
unique_family =set(my_family)
print('Уникальные имена',unique_family)
print('\n')

#Задание №3 - Общая длина всех названий предметов
total_length=0

for subject in my_subjects:
    total_length+=len(subject)
print("Общая длина всех названий предметов=",total_length)
print('\n')

#Задание №4 - Уникальные буквы в названиях предметов
#Можно использовать множества (set) для хранения уникальных букв в названиях предметов
unique_letters=set()

for subject in my_subjects:
    for letter in subject:
        unique_letters.add(letter)
print('Уникальные буквы в названиях предметов -', unique_letters)
print('\n')

#Задание №5 - Имя вашей домашней пушистой кивы в бинарном виде
binary_name = ''.join(format(ord(i),'b') for i in kiva_name)
print('Катя в бинарном виде: ',binary_name,'- стало гораздо лучше')
print('\n')

#Задание №6 - Отсортированный по алфавиту (в обратном порядке) список родственников
#Чтобы отсортировать в обратном порядке пишем вот эту штуку в скобочках "reverse=True"(передаем обратный аргумент)
my_family.sort(reverse=True)
print('Отсортированный список родственников в обратном алфавитном порядке', my_family)
print('\n')

#Задание №7 - Количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)
#Тут необходим модуль datetime
#Ну поехали
today=datetime.today()

days=(today-my_birth).days
print('Количество дней с моего дня рождения до сегоднешнего дня = ', days)
print('\n')

#Задание №8 - Вывод FIFO очереди
q=queue.Queue()
for subject in my_subjects:
    q.put(subject)
print('Добавим предмет')
while True:
    new_subject=input("Для остановки введите 'стоп': ")
    if new_subject=='стоп':
        break
    else:
        q.put(new_subject)    
print('Список всех предметов')
while True:
    print(q.get())
    if q.empty()==True:
        break
print('\n')

#Задание №9 - Ацтекский правитель
Aztec=['Tenōch','Ācamāpichtli','Huītzilihhuitl','Chīmalpopōca','Xīhuitl Tēmoc','Itzcōhuātl','Motēuczōma Ilhuicamīna',
       'Atotoztli','Āxāyacatl','Tīzocic','Āhuitzotl','Motēuczōma Xōcoyōtl','Cuitlāhuac','Cuāuhtēmoc','Tlacotzin',
       'Motelchiuhtzin', 'Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']
#number = (day + month**2 + year) % 21 + 1  
birth=(2003,11,23)
number=(birth[2] + pow(birth[2],1) + birth[0]) % 21 + 1
print(my_family)
index = int(input("Введите индекс элемента для замены: "))

my_family[index-1]=Aztec[number-1]
print(my_family)
print('\n')

#Задание №10
relatives = {'Володя': 1980, 'Петя': 1990, 'Вова': 1975, 'Саня': 2000}

sorted_relatives = sorted(relatives.items(), key=lambda x: x[1]) # сортируем список родственников по возрасту

# создаем связный список
linked_list = {}
for i in range(len(sorted_relatives)-1):
    linked_list[sorted_relatives[i][0]] = sorted_relatives[i+1][0]
    
for key, value in linked_list.items():
    print(key, "->", value)
print('\n')

#Задание №11 - Функция генератор
def aliquot_sequence(n):
    while n != 1:
        yield n
        factors = [i for i in range(1, n) if n % i == 0]
        n = sum(factors)
    yield n

# вызов функции-генератора с помощью цикла
for num in aliquot_sequence(10):
    print(num)
    
number=len(my_name[0]) * len (my_family) % 4
# вызов функции-генератора с помощью функции next()
gen = aliquot_sequence(number)
print(next(gen))
print(next(gen))
print(next(gen))