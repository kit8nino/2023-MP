
from datetime import datetime
import random

#исходные данные 
name=("Леконцев Сергей Михайлович",9,7,2002)
print((name))

#домашнее животное в бинарном виде
name = "Джек"
binary_name = ''.join([format(ord(i), '08b') for i in name])
print("Кличка 'Джек' в ,бинароном виде: ", binary_name)


#средняя оценка
subjects = ['Математика', 'Физика', 'Химия', 'История', 'География', 'Литература', 'Русский язык', 'Английский язык', 'Физическая культура', 'Информатика', 'Обществознание', 'Биология', 'Технология', 'Музыка', 'Изобразительное искусство']
grades = [4, 4, 4, 3, 4, 4, 4, 4, 5, 4, 4, 4, 5, 5, 5]
average_grade = sum(grades) / len(grades)
print("Средняя оценка по всем предметам: ", average_grade)

#Родственники
people = ["Серёжа 2002", "Михаил 1975", "Артем 2006", "Савелий 2008", "Тимофей 2023", "Евгений 1995"]
unique_people = list(set(people))

print("Уникальное имя родственника: ", random.choice(unique_people))

# длинна предмета
total_length = 0
for subject in subjects:
    total_length += len(subject)

print("Общая длина всех предметов: ", total_length)

#уникальные буквы в предмете 
unique_letters = set()
for subject in subjects:
    for letter in subject:
        unique_letters.add(letter)
print("Уникальные буквы предметов: ", unique_letters)

# дата рождения
birthdate = datetime(2002, 7, 9)
today = datetime.now()
days = (today - birthdate).days
print("Количество дней с даты рождения до текущей даты:", days)



#ацтеки
number = (birthdate.day + birthdate.month ** 2 + birthdate.year) % 21 + 1
rulers = ["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Itzcoatl", "Moctezuma I", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Coanococh", "Tlacotzin", "Quaquapitzahuac", "Tecuichpoch I", "Huēnexōchitl", "Cihuacoatl", "Tlacaelel", "Tizoc", "Tlacopan"]
index = sorted(range(len(people)), key=lambda i: int(people[i].split()[-1]))[0]
people[index] = rulers[number-1] + ' ' + people[index].split()[-1]
print("Список родственников с замененным именем: ", people)


sorted_people = sorted(people, key=lambda x: int(x.split()[-1]))
linked_list = {}
for i in range(len(sorted_people)-1):
    linked_list[sorted_people[i].split()[0]] = sorted_people[i+1].split()[0]
linked_list[sorted_people[-1].split()[0]] = None
print("Связанный список родственников: ", linked_list)

#генератор 
generator = len(name[0]) * len(subjects) % 4 #выбор варианта
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

print("Была выбрана функция-генератор :", sequence_name)
for i, num in enumerate(sequence):
    print(num, end=' ')
    if i >= 9:
        break





















