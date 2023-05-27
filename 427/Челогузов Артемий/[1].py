import datetime
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

# исходные данные
personal_info = ("Челогузов Артемий Андреевич", 5, "Октябрь", 2003)
attestat = {"Алгебра": 5,
            "Геометрия": 5,
            "Русский язык": 4,
            "Английский язык": 5,
            "Физика": 4,
            "Химия": 4,
            "Биология": 5,
            "ОБЖ": 5,
            "История России": 5,
            "Всеобщая история": 5,
            "Обществознание": 4,
            "Литература": 5,
            "География": 5,
            "Физическая культура": 5,
            "Технология": 5,
            "Информатика": 5,
            "МХК": 5}
relatives_names = ["Елена 1972", "Андрей 1974", "Кристина 1998", "Ольга 1950", "Римма 1946", "Дмитрий 1986",]
pet_name = "Нола"

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

# 5) Имя питомца в бинарном виде
print("5 Задание:")
pet_name_binary = ''.join(format(ord(i), '08b') for i in pet_name)
print(f"Имя питомца в бинарном виде: {pet_name_binary}\n")

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
print('Функция генератора =', number_my ,'- бесконечная последовательность натуральных чисел, первоначально начинающаяся с числа 0 один раз и дважды с числа 1. \n')

def tribonacci(n):
    h = {}  # creating the dictionary to store the results

    def tribonacci(n):
        if n in h:
            return h[n]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            res = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
            h[n] = res  # storing the results so that we can reuse it again
        return res

    return tribonacci(n)
n = int(input("Количество чисел последовательности Трибоначчи: "))
print(f"Последовательность Трибоначчи {n}:")
for i in range(n):
    print(tribonacci(i),end=' ')


