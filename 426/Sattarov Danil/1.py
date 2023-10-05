from datetime import date

# Исходные данные
IAM = ( 'Саттаров Данил Валерьевчи', '04', '04', '2002')
marks = {
    "Русский язык": 3,
    "Родной язык": 4,
    "Литература": 4,
    "Алгебра": 5,
    "Геометрия": 5,
    "Физика": 5,
    "География": 5,
    "Биология": 4,
    "Физкульура": 5,
    "Технология": 5,
    "Обществознание": 4,
    "Информатика": 5,
    "Химия": 5,
    "Англиский": 4,
    "История": 4
        }
family = ["Руслан 2005", "Юлия 2004", "Алия 2003", "Глеб 2003", "Никита 2002", "Никита 1999"]
Kiwi = "Добби"

# Действия

#1

average_marks = sum(marks.values())/len(marks)
print("1) Средняя оценка:", average_marks)

#2

names = [item.split()[0] for item in family] + ["Данил"]
names = set(names)
print("2) Уникальные имена:", *names)

#3

sum_len_marks = sum(len(mark) for mark in marks)
print("3) Длина всех названий:", sum_len_marks)

#4

unique = set()
for mark in marks:
    unique.update(mark)
print("4) Уникальные буквы: ", unique)

#5

bin_result = ''.join(format(x,'08b') for x in bytearray(Kiwi,'utf-8')) 
print(") Имя Киви в бинарном виде: ", bin_result)

#6
reversefamily = sorted(family, reverse=True)
print("6) Список родственников в обратном порядке: ",*reversefamily)

#7

day = -(date(2002,4,4) - date.today()).days
print("7) Количесвто дней от моей даты до текущей: ",day)

#8
print("8)")
queue = []

while True:
    index = input("Введите индекс предмета (или 'stop' для остановки): ")
    if index == 'stop':
        break
    else:
        item = input("Введите предмет: ")
        queue.insert(int(index), item)


print("Все предметы в очереди:")
for item in queue:
    print(item)


#9

number = (4 + 4**2 + 2002) % 21 + 1
print("9) Номер: ", number, " - 'Moctezuma I'")

while True:
    try:
        index = int(input("Введите индекс: "))
        break
    
    except ValueError:
        print("Неверный индекс")
    
    
if index >= 0 and index < len(reversefamily):
    reversefamily[index] = "Moctezuma I"
    
print("Новый список:", reversefamily)


#10

class Node():
    def __init__(self, name):
        self.name = name
        self.next = None
        
    def __str__(self):
        return f"{self.name} -> {self.next}"     
        

node6 = Node(family[0])
node5 = Node(family[1])
node5.next = node6
node4 = Node(family[3])
node4.next = node5
node3 = Node(family[2])
node3.next = node4
node2 = Node(family[4])
node2.next = node3
node1 = Node(family[5])
node1.next = node2

print("10) Связный список: ", node1)

#11

number = len("Саттаров Данил Валерьевич") * len([item.split()[0] for item in family]) % 4
print("11) Вариант: ",number, " - числа трибоначчи")

def tribonacci():
    a, b, c = 0, 0, 1
    yield a
    yield b
    yield c

    while True:
        next_number = a + b + c
        yield next_number
        a, b, c = b, c, next_number

print("Пример из 10 чисел: ")
tribo_gen = tribonacci()

for i in range(10):
    print(next(tribo_gen))



