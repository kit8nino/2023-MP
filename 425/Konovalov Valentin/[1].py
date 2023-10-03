from datetime import datetime
from multiprocessing import Queue

Name_and_born = ("Коновалов Валентин Андреевич", 14, 3, 2003)
School_marks = {
    "русский язык": 4,
    "литература": 3,
    "алгебра": 4,
    "геометрия": 5,
    "история": 4,
    "информатика": 5,
    "обж": 4,
    "физкультура": 4,
    "обществознание": 4,
    "химия": 4,
    "физика": 3,
    "география": 5,
    "английский язык": 5,
    "биология": 5}
# 1
family_names = ["Андрей", "Елена", "Полина", "Артем", "Илья", "Анастасия", "Константин", "Михаил"]
Name_of_kiwi = "Кот"
print("1) Средняя оценка в аттестате:", sum(School_marks.values()) / len(School_marks.values()))

# 2
print("2)Уникальные имена среди родственников:", list(set(family_names)))

# 3
school_subject_len = 0
for i in list(set(School_marks)):
    school_subject_len += len(i)
print("3)Общая длина всех названий предметов:", school_subject_len)

# 4
all_letters = ""
for i in list(School_marks):
    all_letters += i
print("4)уникальные буквы в названиях предметов:", set(list(all_letters)))

# 5
bin_result = ''.join(format(x, '08b') for x in bytearray(Name_of_kiwi, 'utf-8'))
print("5)имя вашей домашней пушистой кивы в бинарном виде", bin_result)

# 6
family_names.sort(reverse=True)
print("6) Отсортированный по алфавиту (в обратном порядке) список родственников:", family_names)

# 7
print("7.Количество дней от даты рождения до текущей даты: ",
      (datetime.now().date() - datetime(int(Name_and_born[3]), int(Name_and_born[2]), int(Name_and_born[1])).date()))

# 8
FIFO = Queue()
print('8)Введите элементы для FIFO очереди \nЧтобы прекратить ввод введите: stop')
while True:
    i = input()
    if i != "stop":
        FIFO.put(i)
    else:
        print("FIFO очередь сформированна:")
        while not FIFO.empty():
            print(FIFO.get(), end=' ')
        break

# 9
atstec_name = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
               'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
               'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
               'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
atstec_number = (Name_and_born[1] + (Name_and_born[2]) ** 2 + Name_and_born[3]) % 21 + 1
name_index = int(input("9)введите индекс имени родственника который хотите поменять на имя ацтекского правителя:"))
family_names[name_index] = atstec_name[atstec_number - 1]
print(family_names)

# 10
linked_list = {}
for i in range(len(family_names)):
    if i == len(family_names)-1:
        linked_list[family_names[i]] = None
    else:
        linked_list[family_names[i]] = i+1
print(linked_list)
