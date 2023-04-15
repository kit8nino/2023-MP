import datetime

info = ("Железнов Михаил Викторович", 30, 7, 2003)
attestat = {"Русский язык": 4,
            "Литература": 5,
            "Английския язык": 5,
            "Алгебра и начала математического анализа": 5,
            "Геометрия": 5,
            "Информатика и ИКТ": 5,
            "История России": 5,
            "Всеобщая история": 4,
            "Общестовазнание": 4,
            "География": 5,
            "Биология": 4,
            "Химия": 4,
            "Фмзика": 4,
            "МХК": 5,
            "Физическая культура": 5}
relatives = ["Оксана 1982", "Михаил 2003", "Алина 2002",
             "Евгений 1999", "Виктор 1953", "Зинаида 1985",
             "Таисия 1998", "Юрий 1976"]

pet = "Лёва"

# 1 вывести среднюю оценку в аттестате
print("Задание 1")
average_mark = sum(attestat.values()) / len(attestat)
print("Средняя оценка в аттестате: ", average_mark)

# 2 вывести уникальные имена среди своих родственников (включая свое)
print("\nЗадание 2")
names_unique = []
for name in relatives:
    if relatives.count(name) == 1:
        names_unique.append(name.split()[0])
print("Уникальные имена среди моих родственников:", list(set(names_unique)))

# 3 общая длина всех названий предметов
print("\nЗадание 3")
lenght = 0
for subject in sorted(attestat):
    lenght += len(subject)
print("Общая длина всех названий предметов: ", lenght)

# 4 уникальные буквы в названиях предметов
print("\nЗадание 4")
letters_unique = set()
for subject in attestat:
    for letter in subject:
        letters_unique.add(letter)
print("Уникальные буквы в названиях предметов: ", list(letters_unique))

# 5 имя вашей домашней пушистой киви в бинарном виде
print("\nЗадание 5")
bin_pet = " ".join(format(ord(letter), "08b") for letter in pet)
print("Пушистая киви в бинарном виде: ", bin_pet)

# 6 отсортированный по алфавиту (в обратном порядке) список родственников
print("\nЗадание 6")
inversion_relatives = sorted(relatives, reverse=True, key=str.lower)
print(inversion_relatives)

# 7 количество дней от вашей даты рождения до текущей даты
print("\nЗадание 7")
today = datetime.datetime.now()
birthday = datetime.datetime(info[3], info[2], info[1], 5, 50)
number_of_days = today - birthday
print("Количесвто дней от birthday до today: ", number_of_days.days)

# 8 FIFO очередь
print("\nЗадание 8")
FIFO = []
while True:
    ind = input("Введите индекс предмета для его добавления (nope-для остановки): ", )
    if ind != "nope":
        if int(ind) in range(len(attestat)):
            value = list(attestat.keys())[int(ind)]
            FIFO.append(value)
        else:
            print("В словаре нет предмета с таким индексом! Попробуйте еще раз или введите nope-для остановки:")
    else:
        print("FIFO очередь:")
        for value in FIFO:
            print(value)
        break

# 9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя
print("\nЗадание 9")
aztecs = ["Itzcoatl", "Moctezuma I", "Atotoztli",
          "Axayacatl", "Tizoc", "Ahuitzotl",
          "Moctezuma II", "Cuitláhuac", "Cuauhtémoc"]
day = info[1]
month = info[2]
year = info[3]
number = (day + month ** 2 + year) % 21 + 1
while True:
    index = int(input("Введите индекс родственника: ", ))
    if index in range(len(inversion_relatives)):
        inversion_relatives[index] = aztecs[number - 1]
        break
    else:
        print("В списке нет родственника с таким индексом! Попробуйте еще раз:")
names = []
for relative in inversion_relatives:
    name = relative.split()[0]
    names.append(name)
print("Измененный список родственников: ", names)

# 10
print("\nЗадание 10")
relatives_dict = {}
sorted_relatives = sorted(relatives, key=lambda x: int(x.split()[1]))
print("Отсортированный список родственников по годам рождения:", sorted_relatives)
for i in range(len(sorted_relatives) - 1):
    relatives_dict[sorted_relatives[i].split()[0]] = relatives.index(sorted_relatives[i+1])
relatives_dict[sorted_relatives[-1].split()[0]] = None
print("Связный список, где ключ - имя родственника, а значение индекс следующего имени по исходному списку:", relatives_dict)

# 11
print("\nЗадание 11")
number = len(info[0]) * len(relatives) % 4
print(number, "- Аликвотная последовательность")


def aliquot_sequence(N):
    yield N
    visited = {N}
    periodic_numbers = []
    while True:
        sum_divisors = 0
        for i in range(1, N):
            if N % i == 0:
                sum_divisors += i
        if sum_divisors in visited:
            if sum_divisors != N:
                periodic_numbers.append(sum_divisors)
            periodic_numbers.append(N)
            print("\nПоследовательность является периодической.")
            print("Числа в периоде:", ", ".join(str(num) for num in periodic_numbers))
            break
        visited.add(sum_divisors)
        yield sum_divisors
        N = sum_divisors
        if N == 0:
            break


N = int(input("Введите целое положительное число для аликвтоной последовательности:"))
print("Аликвотная последовательность числа ", N)
for n in aliquot_sequence(N):
    print(n, end=" ")








