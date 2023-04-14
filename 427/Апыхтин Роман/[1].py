import datetime
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

# исходные данные
personal_info = ("Апыхтин Роман Русланович", 28, "Июнь", 2001)
attestat = {"Алгебра": 4,
            "Геометрия": 4,
            "Русский язык": 4,
            "Английский язык": 5,
            "Немецкий язык": 5,
            "Физика": 4,
            "Химия": 5,
            "Биология": 5,
            "История России": 4,
            "Всеобщая история": 5,
            "Обществознание": 5,
            "Литература": 4,
            "География": 4,
            "Физическая культура": 5,
            "Технология": 5,
            "Информатика": 5,
            "МХК": 5}
relatives_names = ["Дмитрий 1985", "Светлана 1970", "Алексей 1995", "Алена 1997", "Александр 2005", "Анастасия 2006"]
pet_name = "Тихон"

# 1) Средняя оценка в аттестате
print("1 Задание:")
avg_mark = sum(attestat.values()) / len(attestat)
print(f"Средняя оценка в аттестате: {avg_mark}\n")

# 2) Уникальные имена среди своих родственников
print("2 Задание:")
unique_names = set()#используется для хранения уникальных значений
unique_names.add(personal_info[0].split()[1])
for name in relatives_names:
    unique_names.add(name.split()[0])
print(f"Уникальные имена среди своих родственников: {', '.join(unique_names)}\n")

# 3) Общая длина всех названий предметов
print("3 Задание:")
total_sub_len = 0
for subject in attestat.keys():
    total_sub_len += len(subject)
print(f"Общая длина всех названий предметов: {total_sub_len}\n")

# 4) Уникальные буквы в названиях предметов
print("4 Задание:")
all_letters = []
for word in attestat.keys():
    for letter in word:
        if letter.isalpha():
            all_letters.append(letter)
unique_letters = set(all_letters)
print(f"Уникальные буквы в названиях предметов: {', '.join(unique_letters)}\n")

# 5) Имя вашей домашней пушистой кивы в бинарном виде
print("5 Задание:")
pet_name_binary = ''.join(format(ord(i), '08b') for i in pet_name)
print(f"Имя вашей домашней пушистой кивы в бинарном виде: {pet_name_binary}\n")

# 6) Отсортированный по алфавиту (в обратном порядке) список родственников
print("6 Задание:")
sorted_inv = sorted(relatives_names, reverse=True)
print(f"Отсортированный по алфавиту (в обратном порядке) список родственников: {', '.join(sorted_inv)}\n")

# 7. количество дней от даты рождения до текущей даты
print("7 Задание:")
# дата рождения в формате datetime.date
birthdate = datetime.date(personal_info[3], list(calendar.month_name).index(personal_info[2]), personal_info[1])
# количество дней от даты рождения до текущей даты
days_since_birth = (datetime.date.today() - birthdate).days
print(f"Количество дней от даты рождения до текущей даты: {days_since_birth}\n")

#8) FIFO очередь
print("8 Задание:")
queue = []
while True:
    index = input("Введите индекс(0-13) для добавления предмета в очередь или 'стоп' для остановки: ")
    print()
    if index == "стоп":
        break
    else:
        try:
            index = int(index)
            subject = list(attestat.keys())[index]
            queue.append(subject)
        except (ValueError, IndexError):
            print("Некорректный индекс, повторите ввод")
    print("Предметы в очереди:")
    for item in queue:
        print(item)

#9) По введенному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя под номером, получаемым из вашей даты рождения
print("9 Задание:")
# массив ацтекских правителей
aztec = [
    "Itzcoatl",
    "Moctezuma I",
    "Atotoztli",
    "Axayacatl",
    "Tizoc",
    "Ahuitzotl",
    "Moctezuma II",
    "Cuitláhuac",
    "Cuauhtémoc",
]
day = personal_info[1]
month = list(calendar.month_name).index(personal_info[2])
year = personal_info[3]
number = (day + month**2 + year) % 21 + 1
number_m = f"{aztec[number-1]}"
print(f"Имя ацтекского правителя по моей дате рождения: {number_m}")

index = int(input("Введите индекс родственника: "))
if index < len(sorted_inv) and index >= 0:
    name_parts = sorted_inv[index].split()
    name_parts[0] = f"{number_m}"
    sorted_inv[index] = " ".join(name_parts)
    print(f"Измененный список родственников: {', '.join(sorted_inv)}\n")
else:
    print("Индекс вне диапазона длины списка родственников.\n")

#10)Cоздать связный список, например, как словарь, где ключ - имя родственника, а значение (ссылка на следующий элемент) - индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться неизменным;
print("10 Задание:")
sorted_relatives = sorted(relatives_names, key=lambda x: int(x.split()[1]))
relatives_dict = {}
for i in range(len(sorted_relatives)):
    if i == len(sorted_relatives)-1:
        relatives_dict[sorted_relatives[i]] = None
    else:
        relatives_dict[sorted_relatives[i]] = sorted_relatives[i+1]
print(relatives_dict)
print("Связный список родственников:")
for key, value in relatives_dict.items():
    print(f"{key} => {value}")

#11)функция-генератор:
print("11 Задание:")
gen = [
    "Аликвотная последовательность",
    "Последовательность Сильвестра;",
    "Числа трибоначчи",
    "числа Леонардо",
]
number = len(personal_info[0])*len(relatives_names)%4
number_my = f"{gen[number]}"
print('Функция генератора =', number_my ,'- это рекурсивная последовательность, в которой каждый член является суммой собственных делителей предыдущего члена. \n')

def aliquot(n):
    numb = set()
    while True:
        yield n
        numb.add(n)
        s = 0 #В эту переменную будут записываться суммы делителей числа n
        for i in range(1, n):
            if n % i == 0:
                s += i
        if s in numb:
            print(f"\n{s} в периоде")
            break
        if s == n:
            break
        n = s #в n записывается сумма делителей числа n
n = int(input("Введите число для начала аликвотной последовательности: "))
print(f"Аликвотная последовательность числа {n}:")
for x in aliquot(n):
    print(x, end=' ')



