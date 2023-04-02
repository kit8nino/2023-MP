import datetime
import queue

# Входные данные
my_data = ("Любимов Григорий Ильич", 4, 1, 2003)
disc_marks = {
    "русский": 5,
    "литература": 5,
    "алгебра": 5,
    "история": 5,
    "обж": 5,
    "геометрия": 5,
    "английский": 5,
    "физика": 5,
    "химия": 5,
    "физра": 5,
    "музыка": 5,
    "труд": 5,
    "обществознание": 5,
    "география": 5,
}
family_names = ["Дима", "Илья", "Елена", "Анна", "Алексей", "Сергей", "Татьяна", "Татьяна", "Полина", "Алина", "Андрей"]
kiwa_name = "Афина"


# 1. средняя оценка
average_mark = sum(disc_marks.values()) / len(disc_marks.values())
print("средняя оценка: ", average_mark)


# 2. уникальные имена среди своих родственников (включая свое)
modified_family_names = ["Григорий"]
unique_names = []
for name in family_names:
    if name not in unique_names:
        unique_names.append(name)
        modified_family_names.append(name)
print("уникальные имена среди родственников: ", *modified_family_names)


# 3-4.общая длина всех названий предметов и общая длина всех названий предметов
len_of_subjects = 0
unique_letters = []
for subject in disc_marks:
    len_of_subjects += len(subject)
    for letter in subject:
        if letter in unique_letters:
            continue
        unique_letters.append(letter)
print("общая длина всех названий предметов: ", len_of_subjects)
print("общая длина всех названий предметов: ", *unique_letters)


# 5. имя в бинарном виде
print("имя в бинарном виде: ")
for ch in bytearray(kiwa_name, 'utf-8'):
    print(bin(ch))


# 6. отсортированный по алфавиту (в обратном порядке) список родственников
unique_names.sort()
unique_names.reverse()
print(*unique_names)


# 7. количество дней от даты моего рождения до текущей даты
my_birthday_date = datetime.date(2003, 1, 4)
current_date = datetime.date.today()
number_of_days = current_date-my_birthday_date
print("количество дней от даты моего рождения:  ", number_of_days.days)


# 8. FIFO очередь
queue = queue.Queue()
while True:
    element = input("Введите элемент очереди(out для вывода) ")
    if element == "out":
        print("Элементы очереди: ")
        while not queue.empty():
            print(queue.get())
        break
    else:
        queue.put(element)


# 9. замена имени в отсортированном списке родственников на имя ацтекского правителя
day = my_data[1]
month = my_data[2]
year = my_data[3]
number_of_aztec = (day + month**2 + year) % 21 + 1
number = int(input("Введите номер для замены имени родственника на имя ацтека: "))
aztec_rulers = ["Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Acamapichtli", "Tenoch", "Itzcoatl", "Moctezuma I",
                "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc",
                "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]
unique_names[number] = aztec_rulers[number_of_aztec]
print(*unique_names)


# 10. связный список
linked_family_list = {"Алексей": 1, "Сергей": 2, "Татьяна": 3, "Елена": 4, "Илья": 5, "Анна": 6, "Григорий": 7,
                      "Дима": 8, "Алина": 9, "Полина": None}

print(linked_family_list)


# 11. Генератор
number_of_generator = (len(my_data[0]) * len(family_names)) % 4
print("Номер генератора: ", number_of_generator)
N = int(input("Введите кол-во чисел трибоначчи(начиная с 3-его): "))


def tribonacci(n):
    t1 = 0
    t2 = 0
    t3 = 1
    for a in range(n):
        c = t1+t2+t3
        t1 = t2
        t2 = t3
        t3 = c
        yield c


tri = tribonacci(N)
tribo = [0, 0, 1]
for i in tri:
    tribo.append(i)
print(tribo)
