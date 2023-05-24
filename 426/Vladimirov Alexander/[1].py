from datetime import date

data = ("Владимиров Александр Сергеевич", 1, 8, 2003)

subjects = {
    "Русский язык": 4,
    "Литература": 4,
    "Иностранный язык": 5,
    "Алгебра и начала анализа": 4,
    "Геометрия": 4,
    "Информатика и ИКТ": 4,
    "История России": 4,
    "Всеобщая история": 4,
    "Обществознание": 4,
    "География": 5,
    "Химия": 4,
    "Биология": 4,
    "Физика": 4,
    "Астрономия": 4,
    "Физкультура": 5,
    "ОБЖ": 5,
    "Избранные разделы математики для старшей школы": 4,
    "Компьютерная инженерная графика": 5    
}

names = ["Александр 2003", "Никита 2015", "Елена 1979", "Сергей 1974", "Валентина 1955", "Александр 1958"]

kiwa = "Рудольф"

#1
avg = sum(subjects.values()) / len(subjects)
print("Средняя оценка в аттестате:", avg)

#2
split_names = [nam.split()[0] for nam in names]
unique_names = set(split_names)
print("Уникальные имена родственников:", unique_names)

#3
lenght = sum(len(subject) for subject in subjects.keys())
print("Общая длина всех названий предметов:", lenght)

#4
unique_letters = set()
for subject in subjects:
    unique_letters.update(subject)
print("Уникальные буквы в названиях предметов:", unique_letters)

#5
bi_name = ''.join(format(ord(char), '08b') for char in kiwa)
print("Имя домашней пушистой кивы в бинарном виде:", bi_name)

#6
sorted_names = sorted(names, reverse=True)
print("Отсортированный по алфавиту в обратном порядке список родственников:", sorted_names)

#7
print("Количество дней от даты рождения до текущей даты: {}".format((date.today() - date(day=int(data[1]), month=int(data[2]), year=int(data[3]))).days))

#8 
queue = []
while True:
    index = input("Введите индекс для добавления в очередь или 'stop' для завершения: ")
    if index == "stop":
        break
        
    try: index = int(index)
        
    except ValueError:
        print("Некорректный индекс")
        continue
    item = input("Введите предмет для добавления в очередь: ")
    queue.insert(index, item)

if queue:
    print("Предметы в очереди:")
    for item in queue:
        print(item)

#9
AztecNames = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
number = (int(data[1]) + int(data[2])**2 + int(data[3])) % 21 + 1
index = input("Введите индекс для замены имени: ")
try:
    index = int(index)
except ValueError:
    print("Некорректный индекс")
if index >= 0 and index < len(sorted_names):
    sorted_names[index] = AztecNames[number]
    
print("Обновлённый список родственников:", sorted_names)

#10
linked_list = {}
for i in range(len(names)):
    if i == len(names) - 1:
        linked_list[names[i]] = None
    else:
        linked_list[names[i]] = names[i+1]

print("Связный список:")
for key, value in linked_list.items():
    print(f"{key} -> {value}")
    
#11
number = (len(data[0]) * len(names)) % 4
print(number)
print(len(names))
print(len(data[0]))
def aliquot_sequence_generator(n):
    yield n  
    while True:
        divisors_sum = sum([i for i in range(1, n) if n % i == 0])  
        yield divisors_sum  
        n = divisors_sum 


starting_number = 20
sequence_length = 10

generator = aliquot_sequence_generator(starting_number)

sequence = []
for i in range(sequence_length):
    number = next(generator)
    sequence.append(number)

print("Аликвотная последовательность:")
print(sequence)

