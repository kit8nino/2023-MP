from datetime import datetime
import itertools

attestat = {'Русский язык': 4,
            'Алгебра': 4,
            'Геометрия': 4,
            'Английский язык': 4,
            'Информатика': 5,
            'Физика': 4,
            'Химия': 4,
            'История России': 4,
            'Всеобщая история': 4,
            'География': 4,
            'Биология': 4,
            'Литература': 4,
            'Физкультура': 5,
            'Музыка': 5,
            'Экономика': 5}

avg_rating = sum(attestat.values()) / len(attestat)
print("Задание 1")
print(f"Средняя оценка в аттестате: {avg_rating}")

relatives = [
             "Екатерина 1980",
             "Александр1977",
             "Вера 1959",
             "Денис 2014",
             "Егор 2007",
             "Пётр 1959",
             "Надежда 1956",
             "Татьяна 1970",
             "Татьяна 1984",
             "Ярослав 2010",
             "Наталья 1982"]
unique_names = set(relatives)
print("Задание 2")
print(f"Уникальные имена родственников: {unique_names}")

subject_lengths = [len(subject) for subject in attestat]
total_subject_length = sum(subject_lengths)
print("Задание 3")
print(f"Общая длина названий предметов: {total_subject_length}")

letters = []
for subject in attestat:
    for letter in subject:
        if letter not in letters:
            letters.append(letter)
print("Задание 4")            
print(f"Уникальные буквы в названиях предметов: {sorted(letters)}")

name = "Кокос"
binary_name = ''.join(format(ord(letter), 'b') for letter in name)
print("Задание 5")
print("Кокос")
print(f"Имя домашней пушистой кивы в бинарном виде: {binary_name}")

sorted_relatives = sorted(relatives, reverse=True)
print("Задание 6")
print(f"Отсортированный список родственников: {sorted_relatives}")

today = datetime.now()
birthday = datetime.strptime("25.04.2003", "%d.%m.%Y")
days_since_birthday = (today - birthday).days
print("Задание 7")
print(f"Количество дней от дня рождения до сегодняшнего дня: {days_since_birthday}")

queue = []
print("Задание 8")
while True:
    try:
        index = int(input("Введите индекс предмета, который вы хотите добавить в очередь (или  -1 для остановки): "))
        if index == -1:
            break
        subject = list(attestat.keys())[index]
        queue.append(subject)
    except:
        print("Неверный индекс, попробуйте еще раз")

print("Очередь предметов:")
for subject in queue:
    print(subject)

aztec_rulers = ["Acamapichtli",
                "Huitzilihuitl",
                "Chimalpopoca",
                "Itzcoatl",
                "Moctezuma I",
                "Axayacatl",
                "Tizoc",
                "Ahuitzotl",
                "Moctezuma II",
                "Cuitlahuac",
                "Cuauhtemoc",
                "Coanacoatl",
                "Quauhtlatoa",
                "Tlacotzin",
                "Ixtlilxochitl",
                "Nezahualcoyotl",
                "Totoquihuatzin",
                "Tezozomoc",
                "Maxtla",
                "Tezcatlipoca",
                "Itzcoatl"]
number = (birthday.day + birthday.month**2 + birthday.year) % 21 + 1
new_name = aztec_rulers[number - 1]
index = 0  #вводим нужный индекс для замены на имя ацтекского правителя
sorted_relatives[index] = new_name

print("Задание 9")
print(f"Список родственников после замены имени: {sorted_relatives}")

ordered_indexes = sorted(range(len(relatives)), key=lambda k: int(relatives[k][-4:]) if relatives[k][-4:].isdigit() else 0)



linked_list = {}
for i, index in enumerate(ordered_indexes):
    linked_list[relatives[index]] = ordered_indexes[i+1] if i < len(relatives)-1 else None
print("Задание 10")
print(f"Связный список родственников: {linked_list}")

def aliquot_sequence(start):
    num = start
    while True:
        yield num
        divisor_sum = sum([i for i in range(1, num) if num % i == 0])
        num = divisor_sum
    
def sylvester_sequence(start):
    num = start
    while True:
        yield num
        num *= 2
        num += 1
        
def tribonacci_sequence():
    seq = [0, 0, 1]
    while True:
        yield seq[-1]
        seq = [seq[-2], seq[-1], sum(seq)]
        
def leonardo_sequence():
    seq = [1, 1]
    while True:
        yield seq[-1]
        seq.append(seq[-1] + seq[-2] + 1)
        
fio_len = len("Попкова Дарья Александровна")
family_names = ["Екатерина",
                "Александр",
                "Вера",
                "Денис",
                "Егор",
                "Пётр",
                "Надежда",
                "Татьяна",
                "Татьяна",
                "Ярослав",
                "Наталья"]

number = fio_len * len(family_names) % 4

if number == 0:
    sequence = aliquot_sequence(10)
elif number == 1:
    sequence = sylvester_sequence(2)
elif number == 2:
    sequence = tribonacci_sequence()
else:
    sequence = leonardo_sequence()

result = list(itertools.islice(sequence, 10))
print("Задание 11")
print(f"Результат генератора для number={number}: {result}")