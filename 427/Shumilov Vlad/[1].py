import datetime as dt
import queue


data = ("Шумилов Владислав Дмитриевич", 23, 7, 2003)

certificate = {
    "Алгебра": 5,
    "Геометрия": 5,
    "Русский язык": 4,
    "Английский язык": 4,
    "Физика": 5,
    "Астрономия": 5,
    "История России": 4,
    "Всеобщая история": 4,
    "Физкультура": 5,
    "Химия": 4,
    "Социология": 4,
    "Право": 5,
    "Литература": 4,
    "Биология": 5
}

familyNames = ["Владислав", "Наталья", "Игорь", "Алла", "Дмитрий", "Алексей", "Максим", "Елена", "Анастасия", "Дмитрий", "Елена"]

kiwaName = 'Сэмюэль'

# average mark


def avg_mark(obj):
    return sum(obj.values()) / len(obj)


print(f'Средняя оценка аттестата {avg_mark(certificate)} балла \n')


# unique names


uniqueNames = set(familyNames)
print(f'Уникальные имена: {uniqueNames} \n')


# total length of all item names


def total_length(obj):
    total = 0
    for key in obj:
        total += len(key)
    return total


print(f"Общая длина названий предметов: {total_length(certificate)} символов \n")

# unique char


def unique_char(obj):
    uniqueChar = []
    for key in obj:
        for c in key:
            if not c in uniqueChar:
                uniqueChar.append(c)
    return uniqueChar


print(f'Уникальные символы: {unique_char(certificate)} \n')

# kiwa name in bin


def binary_name(str):
    binary = ' '.join(format(ord(x), 'b') for x in str)
    return binary


print(f'Имя в двоичном представлении: {binary_name(kiwaName)} \n')

# reverse sort


def reverse_list(list):
    reverseList = sorted(list, reverse=True)
    return reverseList


reverseFamily = reverse_list(familyNames)

print(f'Реверсивый список имен: {reverseFamily} \n')

# date time


def get_birth_days_out(list):
    return (dt.datetime.today() - dt.datetime(day=list[1], month=list[2], year=list[3])).days


print(f"Дней прошло: {get_birth_days_out(data)} \n")

print("Введите индекс, '-1' для выхода \n")

things = queue.Queue()
i = int(input())
while i != -1:
    things.put(i)
    i = int(input())
print("Вы ввели", end=':')
while not things.empty():
    print(things.get(), end=',')
print()

# №9

AztecNames = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']

index = (int(data[1]) + int(data[2])**2 + int(data[3])) % 21 + 1
print(f'{AztecNames[index]} - имя ацтека под индексом {index} \n')


def replace_family_name(list):
    a = int(input(f'Введите число от 0 до {len(list)} : '))
    if a < 0 or a > len(list):
        print("Нет доступного имени \n")
    else:
        list[a] = AztecNames[index]
        print(f'Обновленный список {list} \n')


replace_family_name(reverseFamily)


# №10

def get_linked_list(arr):
    lst = []
    for i in range(len(arr)):
        ls = [arr[i], i+1]
        lst.append(ls)
        ls = []
    return lst


# №11 Генератор аликвотной последовательности


def aliquot(num):
    d = []
    aliquotPos = [num]
    while num >= 1:
        for i in range(1, num):
            if num == 1:
                aliquotPos.append(0)
            elif num % i == 0:
                d.append(i)
        summ = sum(d)
        aliquotPos.append(summ)
        num = summ
        d = []
    return aliquotPos


print("Aликвотная последовательность:", aliquot(10))
