from datetime import date

#Исходные данные
my_data = ("Белянин Денис Алексеевич", 7, 6, 2003)

attestat = {'математика': 5, 'русский язык': 5, 'английский язык': 5, 'история': 4,
            'обществознание': 4, 'физика': 5, 'химия': 5, 'биология': 5, 'география': 5,
            'информатика': 5, 'технология': 5, 'физическая культура': 5, 'музыка': 5,
            'изобразительное искусство': 5}

relatives = ['Денис 2003', 'Мария 1978', 'Иван 1955', 'Алексей 1975']

animal_name = 'Миса'

#ЗАДАНИЕ1
print("1 ЗАДАНИЕ:")
average_rating = sum(attestat.values()) / len(attestat)
print(f"Средняя оценка в аттестате: {average_rating:.2f}")

#ЗАДАНИЕ2
print("2 ЗАДАНИЕ:")
unique_names = set([name.split()[0] for name in relatives])
print("Уникальные имена среди родственников:", unique_names)

#ЗАДАНИЕ3
print("3 ЗАДАНИЕ:")
subjects = list(attestat.keys())
length = sum([len(sub_len) for sub_len in subjects])
print("Общая длина всех названий предметов:", length)

#ЗАДАНИЕ4
print("4 ЗАДАНИЕ:")
unique_letters = set(''.join(subjects))
print("Уникальные буквы в названиях предметов:", unique_letters)

#ЗАДАНИЕ5
print("5 ЗАДАНИЕ:")
binary_name = ''.join(format(ord(char), 'b') for char in animal_name)
print(binary_name)

# #ЗАДАНИЕ6
print("6 ЗАДАНИЕ:")
sorted_relatives = sorted(relatives, reverse=True)
print(sorted_relatives)

#ЗАДАНИЕ7
print("7 ЗАДАНИЕ:")
my_date = date(my_data[3], my_data[2], my_data[1])
days_diff = (date.today() - my_date).days
print("Количество дней от даты рождения до текущей даты:", days_diff)

#ЗАДАНИЕ8
print("8 ЗАДАНИЕ:")
FIFO_queue = []

while True:
        index = int(input("Введите индекс предмета для добавления в очередь(0-13): "))
        if index < 0 or index > 13:
            print("Индекс должен быть от 0-13")
            continue
        else:
            item = list(attestat.items())[index]
            FIFO_queue.append(item)
            print(f"Предмет {item[0]} добавлен")

        stop = input("'stop' - остановить ввод. Любая другая клавиша - продолжить: ")
        if stop == "stop":
            break

print("В очереди находятся следующие предметы:")
for item in FIFO_queue:
    print(item[0], "- оценка", item[1])

#ЗАДАНИЕ9
print("9 ЗАДАНИЕ:")
aztec_rulers = ['Acamapichtli', 'Huitzilihuitl', 'Chimalpopoca', 'Itzcoatl', 'Moctezuma I',
                'Axayacatl', 'Tizoc', 'Ahuitzotl', 'Moctezuma II', 'Cuitláhuac', 'Cuauhtémoc',
                'Coanacoch', 'Totoquihuatzin', 'Ixtlilxochitl I', 'Nezahualcoyotl', 'Maxtla',
                'Tlacaelel', 'Chimalpilli I', 'Nezahualpilli', 'Chimalpopoca II', 'Moquihuixtli']

number = (my_data[1] + my_data[2]**2 + my_data[3]) % 21 + 1
print("Номер ацетковского правителя:", number)

relative_index = int(input("Введите индекс родственника(0-3): "))
if 0 <= relative_index < len(sorted_relatives):
    relative_name = sorted_relatives[relative_index].split()[0]
    print("Родственник", relative_name, "заменен на", aztec_rulers[number-1])
else:
    print("Неверный индекс родственника.")

#ЗАДАНИЕ10
print("10 ЗАДАНИЕ:")
relatives_dict = {}

sorted_indexes = sorted(range(len(relatives)), key=lambda i: int(relatives[i].split()[1]))
print("Отсортированный в порядке возрастания по индексам из начального списка relatives: ",sorted_indexes)

sorted_relatives = sorted(relatives, key=lambda x: int(x.split()[1]))

for i in range(len(sorted_relatives)):
    if i == len(sorted_relatives)-1:
        relatives_dict[sorted_relatives[i]] = None
    else:
        relatives_dict[sorted_relatives[i]] = sorted_relatives[i+1]

for name, val in relatives_dict.items():
    print(name, ':' ,val)

#11ЗАДАНИЕ
print("11 ЗАДАНИЕ:")
full_name = my_data[0].split()
family_names = [relative.split()[0] for relative in relatives]

number = len(''.join(full_name)) * len(family_names) % 4
print("Полученный способ: ", number)

def aliquot_sequence(n):
    yield n
    while n != 1:
        n = sum([i for i in range(1, n) if n % i == 0])
        yield n

start_value = int(input("Введите начальное значение: "))
sequence = aliquot_sequence(start_value)

for i in range(100):
    try:
        print(next(sequence))
    except StopIteration:
        print("Закончились значения для генерации")
        break















