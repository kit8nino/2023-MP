from datetime import date
import queue

data = ("Круглов Никита Викторович", 30, 8, 2003)

certificate = {
    "Русский язык": 4,
    "Литература": 4,
    "Иностранный язык": 5,
    "Алгебра и начала анализа": 4,
    "Геометрия": 4,
    "Информатика и ИКТ": 4,
    "История России": 4,
    "Всеобщая история": 5,
    "Обществознание": 4,
    "География": 5,
    "Химия": 4,
    "Биология": 4,
    "Физика": 5,
    "Астрономия": 4,
    "Физкультура": 5,
    "ОБЖ": 5,
    "Избранные разделы математики для старшей школы": 4,
    "Компьютерная инженерная графика": 5    
}

family_names = ["Никита 2003", "Виктория 2010", "Виктор 1970", "Людмила 1975", "Ксения 2018", "Дмитрий 1993"]

namekiwa = "Арагог"


average_mark = sum(certificate.values())/len(certificate.values())
print("1.Средняя оценка в аттестате:", average_mark)

unique_names = list(set(family_names))
print("2.Уникальные имена среди родственников:\n", unique_names)

cer_len = [0]*len(certificate.values())
count = 0
disk_marks_string = ""
for i in certificate.keys():
    cer_len[count] = i
    disk_marks_string += cer_len[count]
    count += 1
print("3.Общая длина всех названий предметов:", len(disk_marks_string))

unique_letters = set()
for cer in certificate:
    unique_letters.update(certificate)
print("4.Уникальные буквы в названиях предметов:", unique_letters)

bin_kiwa_name = list(format(c, 'b') for c in bytearray(namekiwa, "utf-8"))
print("5.Имя пушистой кивы в бинарном виде:", namekiwa)

sorted_names = sorted(family_names, reverse=True)
print("6.Отсортированный по алфавиту в обратном порядке список родственников:", sorted_names)

print("7.Количество дней от даты рождения до текущей даты: {}".format((date.today() - date(day=int(data[1]), month=int(data[2]), year=int(data[3]))).days))

q = queue.Queue()
print('Чтобы прекратить ввод введите end: ')
while True:
    subject = input('   ')
    if subject == 'end':
        break
    else:
        q.put(subject)
print("8.FIFO очередь: ")
while True:
    print(q.get(), end=', ')
    if q.empty()==True:
        break

Aztec= ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
number = (int(data[1]) + int(data[2])**2 + int(data[3])) % 21 + 1
index = input("Введите индекс")
index = int(index)
if index >= 0 and index < len(sorted_names):
    sorted_names[index] = Aztec[number]

print("9.Cписок родственников:", sorted_names)

familynameslinked = {"Никита 2003":1, "Виктория 2010":2, "Виктор 1970":3, "Людмила 1975":4, "Ксения 2018":5, "Дмитрий 1993":6}
print("10.Список", familynameslinked)

number = (len(data[0]) * len(family_names)) % 4


def tribonacci_generator():
    a, b, c = 0, 0, 1
    yield a
    yield b
    yield c

    while True:
        next_num = a + b + c
        yield next_num
        a, b, c = b, c, next_num


n = 10

tribonacci = tribonacci_generator()
tribonacci_sequence = [next(tribonacci) for _ in range(n)]

print("11.Последовательность чисел Трибоначчи:")
print(tribonacci_sequence)
