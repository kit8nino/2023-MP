from datetime import date

data = ("Хохлова Алёна Олеговна", 16, 9, 2003)

marks = {
    "Русский язык": 5,
    "Литература": 5,
    "Краеведение": 5,
    "Иностранный язык": 5,
    "Алгебра": 5,
    "Геометрия": 5,
    "Информатика": 5,
    "История России": 5,
    "Всеобщая история": 5,
    "Обществознание": 5,
    "География": 5,
    "МХК": 5,
    "Химия": 5,
    "Биология": 5,
    "Физика": 5,
    "Астрономия": 5,
    "Физкультура": 5,
    "ОБЖ": 5,
    "Экономика": 5
}

relatives = ["Алёна 2003", "Евгений 1990", "Константин 1995", "Александр 1995", "Иван 2008", "Илья 2012", "Даниил 2002", "Матвей 2002"]

kiwa_name = "Натсик"

#1 вывести среднюю оценку в аттестате;
average_mark = sum(marks.values()) / len(marks)

print("Средняя оценка в аттестате:", average_mark)

#2 вывести уникальные имена среди своих родственников (включая свое);
snames = [rel.split()[0] for rel in relatives]

unames = set(snames)

print("Уникальные имена среди своих родственников", unames)

#3 общая длина всех названий предметов;
sub_len = sum(len(mark) for mark in marks.keys())

print("Общая длина всех названий предметов:", sub_len)

#4 уникальные буквы в названиях предметов;
uniqueLetters = set()

for mark in marks:
    
    uniqueLetters.update(mark)
    
print("Уникальные буквы в названиях предметов:", uniqueLetters)
 
#5 имя вашей домашней пушистой кивы в бинарном виде;
binary = ''.join(format(ord(char), '08b') for char in kiwa_name)
print("Имя домашней пушистой кивы в бинарном виде:", binary)

#6 отсортированный по алфавиту (в обратном порядке) список родственников;
RelativesReversed = sorted(relatives, reverse=True)

print("Отсортированный по алфавиту (в обратном порядке) список родственников:", RelativesReversed)

#7 количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной);
print("Количество дней от даты рождения до текущей даты: {}".format((date.today() - date(day=int(data[1]), month=int(data[2]), year=int(data[3]))).days))

#8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все;
queue = []

while True:
    
    index = input("Введите индекс для добавления в очередь или 'cancel', чтобы остановить")
    
    if index == "cancel":
        break
        
    try: index = int(index)
        
    except ValueError:
        print("Неверный индекс, попробуйте ещё раз")
        continue
        
    i = input("Введите предмет")
    queue.insert(index, i)

if queue:
    print("Предметы:")
    for i in queue:
        print(i)

#9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя (смотреть по списку всех на странице https://en.wikipedia.org/wiki/List_of_rulers_of_Tenochtitlan) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;
Aztecs = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']

number = (int(data[1]) + int(data[2])**2 + int(data[3])) % 21 + 1

index = input("Введите индекс")

try:
    index = int(index)
    
except ValueError:
    print("Неверный индекс")
    
if index >= 0 and index < len(RelativesReversed):
    RelativesReversed[index] = Aztecs[number]
    
print("Новый список:", RelativesReversed)

#10 создать связный список, например, как словарь, где ключ - имя родственника, а значение (ссылка на следующий элемент) - индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться неизменным;
llist = {}
for i in range(len(relatives)):
    if i == len(relatives) - 1:
        llist[relatives[i]] = None
    else:
        llist[relatives[i]] = relatives[i+1]

print("Связный список:")
for key, value in llist.items():
    print(f"{key} || {value}")
    
#11 написать функцию-генератор, свой вариант определяется как number = len("ФИО") * len (family_names) % 4:


def aliquot(n):
    yield n  
    if n == 1:
        return
    divisors_sum = sum([i for i in range(1, n) if n % i == 0]) 
    yield from aliquot(divisors_sum)  


starting_number = 10
sequence_length = 10

generator = aliquot(starting_number)

sequence = []
for _ in range(sequence_length):
    try:      
        number = next(generator)
        sequence.append(number)
    except StopIteration:
        break

print("Аликвотная последовательность:")
print(sequence)
