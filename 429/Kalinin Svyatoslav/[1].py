import datetime as dt
import random
import queue

def QuickSort_rev(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] > q:
                i += 1
            while A[j] < q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                QuickSort_rev(A, l, j)
                QuickSort_rev(A, i, r)

def generate_sequence():
    fio_len = data[0]
    family_names_len = len(family_names)
    number = fio_len * family_names_len % 4
                

# Ввод данных
data = ("Калинин Святослав Ильич", 15 , 11, 2003) 
subjects = {"Математика": 5, "Русский язык": 4, "Физика": 4, 
            "Химия": 5, "История": 4, "География": 5, 
            "Обществознание": 3, "Биология": 5, "Английский язык": 4,
            "Немецкий язык": 4, "Французский язык": 4, "Музыка": 5, 
            "Литература": 5, "Информатика": 5}
family_names = ["Илья", "Лариса", "Арина", "Ирина", "Валера"]
kiwi_name = "Епельдефор"

# Вывод отзыва в аттестате
average = sum(subjects.values()) / len(subjects)
if average >= 4.5:
    grade = "отлично"
elif average>=3.5:
    grade = "хорошо"
else: 
    grage = "удовлетворительно"
print(f"Аттестат {data[0]} выставлен на оценку {grade}.")

# Поиск имен среди родственников
names = [name for name in family_names if name in " ".join(data[0])]
if names:
    print(f"Среди родственников есть следующие имена: {', '.join(names)}")
else:
    print("Среди родственников нет ваших имен.")

# Вычисление длины задержанных лиц
detainees = ["Илья", "Ира", "Арина"]
detainees_len = sum([len(name) for name in detainees])
print(f"Общая длина всех задержанных лиц: {detainees_len} символов.")

# Проверка наличия букв в названиях предметов
letters = set("".join(subjects.keys()))
if letters.isdisjoint(set("abcdefghijklmnopqrstuvwxyz")):
    print("Названия предметов не содержат букв латинского алфавита.")
else:
    print("Названия предметов содержат буквы латинского алфавита.")

# Перевод имени пушистой кивы в бинарный вид
kiwi_binary = " ".join(format(ord(char), "b") for char in kiwi_name)
print(f"Имя пушистой кивы в бинарном виде: {kiwi_binary}")

# Сортировка списка родственников по алфавиту в обратном порядке
sorted_relatives = sorted(family_names, reverse=True)
print("Список родственников, отсортированный по алфавиту в обратном порядке:")
print("\n".join(family_names))

# Вычисление количества дней от дня рождения до текущей даты
time_now = dt.datetime.today()
time_birth = dt.datetime(day=data[1], month=data[2], year=data[3])
print("days: ",(time_now-time_birth).days)

# Функция для замены имени в списке родственников по индексу
def change_name_by_index(index, ruler_name):
    sorted_relatives[index] = ruler_name

# Вычисление индекса для замены имени в списке родственников
QuickSort_rev(family_names, 0, len(family_names)-1)
print(family_names)

# Реализация FIFO и команды stop
print("end of input : '-1'")
things = queue.Queue(101)
i = int(input())
while i!=-1:
    things.put(i)
    i = int(input())
print("u entered",end=':')
while not things.empty():
    print(things.get(), end=',')
print()
