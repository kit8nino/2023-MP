# начальные данные
fio = "Козлов Алексей Дмитриевич"
day = "11"
month = "июнь"
year = "2003"
information = (fio, day, month, year)

attestat = {"Русский язык": 4,
           "Литература": 5,
           "Алгебра": 5,
           "Геометрия": 5,
           "Физика": 5,
           "Химия": 5,
           "Биология": 5,
           "География": 5,
           "Черчение": 5,
           "Физическая культура": 5,
           "Английский язык": 5,
           "Информатика": 5,
           "Рисование": 5,
           "Музыка": 5
           }

family = ["Наталья", "Дмитрий", "Кирилл", "Павел", "Надежда", "Павел", "Ольга", "Полина", "Дарья",
          "Виктор", "Людмила", "Василий", "Роман", "Софья"]

kivi_name = "Барсик"

# 1) Средняя оценка аттестата
average = sum(attestat.values())/len(attestat)
print("Средний балл аттестата: ", average)

# 2) Уникальные имена родственников
unique_names = []
name = "Алексей"
unique_names.append(name)
for name in family:
    if name in unique_names:
        continue
    else:
        unique_names.append(name)
print("Уникальные имена в семье: ", unique_names)

# 3) общая длина всех названий предметов
total_len = sum(len(value) for value in attestat)
print("Суммарная длина всех названий предметов: ", total_len)

# 4) Уникальные буквы в названиях предметов
unique_letters = []
for keys in attestat:
    for char in keys:
        if char in unique_letters:
            continue
        else:
            unique_letters.append(char)
print("Уникальные буквы в названиях предметов: ", unique_letters)

# 5) Имя домашней Киви в бинарном виде
bin_name = ' '.join(format(ord(char), '08b') for char in kivi_name)
print("Барсик в бинарном коде: ", bin_name)

# 6) Отсортированный по алфавиту (в обратном порядке) список родственников
family.sort()
print("Отсортированный список родственников по алфавиту: ", family)
print("Отсортированный список родственников в обратном порядке: ", sorted(family, reverse=True))

# 7) количество дней от моей даты рождения до текущей даты
from datetime import date

birthday = date(2003, 6, 11)
today = date.today()
delta = today - birthday
days = delta.days

print("Число дней прошедших от моего дня рождения: ", days)

# 8) FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все
from collections import deque

keys = list(attestat.keys())

list = deque()
while True:
    i = input("Введите номер элемента в очередь от 0 до 14, для завершения введите stop  ")
    if i == "stop":
        break
    else:
        list.append(keys[int(i)])
print(list)


# 9) по введённому индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя под номером: number = (day + month**2 + year) % 21 + 1.
number = int(input("Введите номер из списка родственников "))
number_of_actek = (11 + 6**2 + 2003) % 21 + 1
print("Номер ацтекского правителя - ", number_of_actek)
name_of_actek = "Cuauhtémoc"
family[number] = name_of_actek
print(family)

# 10) Создание связанного списка родственников
list_of_relatives = {
    "Людмила": 1,
    "Виктор": 2,
    "Павел": 3,
    "Надежда": 4,
    "Василий": 5,
    "Наталья": 6,
    "Дмитрий": 7,
    "Павел ": 8,
    "Ольга": 9,
    "Роман": 10,
    "Полина": 11,
    "Дарья": 12,
    "Софья": 13,
    "Кирилл": None
}

# 11) функция генератор (последовательность Сильвестра)
var = len(fio)*len(family) % 4
print(var)


def sylvester_sequence(n):
    sylvester_numbers = [1, 2, 3]
    count = 2
    num = 1

    for count in range(n):
        for i in range(len(sylvester_numbers)):
            num += sylvester_numbers[i]
        num += 1
        sylvester_numbers.append(num)
        yield num

n = int(input("Введите количество членов последовательности Сильвестра: "))

sequence = sylvester_sequence(n)
for num in sequence:
    print(num)

