from datetime import datetime
from collections import deque
import queue

q = queue.Queue()
queue_ = deque()

full_name = ("Куприянов Данила Максимович", 29, 8, 2003)

marks = {
    "русскийязык": 3,
    "литература": 4,
    "геометрия": 3,
    "алгебра": 3,
    "биология": 5,
    "информатика": 5,
    "английский язык": 5,
    "обществознание": 5,
    "география": 5,
    "историяроссии": 4,
    "всоебщаяистория": 4,
    "химия": 4,
    "физкультура": 5,
    "обж": 4
}

family = ["Татьяна 1983", "Максим 1979", "Ирина 1959", "Валерий 1957", "Анна 1961", "Владимр 1959"]

kiwa_name = "Милеле"
aztec_names = [
    'Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
    'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
    'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
    'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac'
]

average_rating = sum(marks.values()) / len(marks.values())
print("Средняя оценка в школе:", average_rating, "\n")

unique_names = list(set(family))
print("Уникальные имена родственников:", unique_names, "\n")

length = sum(len(m) for m in marks.keys())
print(f"Общая длина всех названий предметов: {length} \n")

lenght_name_marks = [0] * len(marks.values())
name_marks_string = ""
for i in marks.keys():
    for n in range(14):
        lenght_name_marks[n] = i
        name_marks_string += lenght_name_marks[n]

unique_letter = {}
for letter in name_marks_string:
    if letter in unique_letter:
        unique_letter[letter] += 1
    else:
        unique_letter[letter] = 1
print(f"Уникальные буквы в названиях предметов: {', '.join(unique_letter)} \n")

binary_kiwa_name = ''.join(format(ord(letter), '08b') for letter in kiwa_name)
print(f"Имя пушистой кивы в бинарном виде: {binary_kiwa_name} \n")

family.sort(reverse=True)
print("Отсортированный по алфавиту в обратном порядке список родственников:\n", family, "\n")

birth_date = datetime(day=int(full_name[1]), month=int(full_name[2]), year=int(full_name[3]))
days_since_birth = (datetime.now() - birth_date).days
print("Количество дней от даты рождения до текущей даты: {}".format(days_since_birth), "\n")

while True:
    item = input("Введите предмет (или 'quit' для завершения): ")
    if item == "quit":
        break
    try:
        n = 1
        queue_.insert(n, item)
    except ValueError:
        queue_.append(item)

print("FIFO Очередь:")
for item in queue_:
    print(item)

number = (int(full_name[1]) + int(full_name[2]) ** 2 + int(full_name[3])) % 21 + 1
print("Индекс имени ацтека:", number, "\nВыбранное имя ацтека =>", aztec_names[number])

index = int(input("Введите число от 0 до 11:"))
family[index] = aztec_names[number]
print("Обновленный список имён:", family, "\n")

family_new = {
    "Анна 1961": 1,
    "Владимр 1959": 2,
    "Валерий 1957": 3,
    "Ирина 1959": 4,
    "Татьяна 1983": 6,
    "Максим 1979": 5,
    "Данила 2003": 0
}
print("Список, упорядоченный по годам рождения:", family_new, "\n")

number = len(full_name[0]) * len(family) % 4
print(number, "Последовательность Сильвестра")


def sylvester():
    x = 2
    yield x
    for i in range(9):
        x = x * x + 1
        yield x


for i, num in enumerate(sylvester()):
    print(num, end=' ')
    if i >= 5:
        break
