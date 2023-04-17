import datetime
import queue

#ФИО, число, месяц, год рождения в виде кортежа
my_data=("Гребнев  Кирилл  Андреевич", 25, 6, 2003)
#предметы в школьном аттестате (не меньше 14), как словарь из названия и оценки
disc_marks= {
    "русский":           5,
    "литература":        5,
    "информатика":       5,
    "алгебра":           5,
    "геометрия":         5,
    "физика":            5,
    "химия":             5,
    "английский":        5,
    "обж":               5,
    "физкультура":       5,
    "чувашский":         5,
    "биология":          5,
    "история":           5,
    "обществознание":    5,
    "черчение":          5
    }
#имена (только) ближайших (до двоюродных включительно) родственников в списке
dict_family_names=["Наталья 1981","Андрей 1979","Кирилл 2003","Валентина 1951","Галина 1956","Николай 1955","Александр 1973","Наталья 1982","Михаил 2007","Александр 2007","Александр 1968","Максим 2009", "Елена 1978"]
family_names=["Наталья","Андрей","Кирилл","Валентина","Галина","Николай","Александр","Наталья","Михаил","Александр","Александр","Максим", "Елена"]
#имя, которое вы бы дали своей домашней пушистой киве (строка)
kiva_name="Люся"
print('[1] Работа со структурами данных')
print(' '*10 )

#Действия

#1___________________вывести среднюю оценку в аттестате_______________________
average_mark=sum(disc_marks.values())/len(disc_marks.values())
print('1) Средняя оценка в аттестате:', average_mark)

#2______вывести уникальные имена среди своих родственников (включая свое)_____
unique_name=[]
for name in family_names:
    if name in unique_name:
        continue
    else:
        unique_name.append(name)
print('2) Уникальные имена среди своих родственников (включая свое):', *unique_name)
#или unique_names=list(set(unique_name))

#3___________________общая длина всех названий предметов______________________
count=0
for i in list(disc_marks):
    count+=(len(i))
print('3) Общая длина всех названий предметов:', count)

#4__________________уникальные буквы в названиях предметов____________________ 
unique_letters = set()
for subject in disc_marks.keys():
    for letter in subject:
        unique_letters.add(letter)
print('4) Уникальные буквы в названиях предметов:', set(unique_letters))

#5_____________имя вашей домашней пушистой кивы в бинарном виде_______________
binary_kiva_name = ''.join(format(ord(x), '08b') for x in kiva_name) 
#  или  binary_kiva_name = list(format(x, 'b') for x in bytearray(kiva_name, "utf-8"))
print('5) Имя вашей домашней пушистой кивы в бинарном виде:', binary_kiva_name)

#6____отсортированный по алфавиту(в обратном порядке) список родственников____
family_names.sort(reverse=True)
print('6) Отсортированный по алфавиту(в обратном порядке) список родственников:', family_names)

#7___________количество дней от вашей даты рождения до текущей даты___________
print('7)', datetime.datetime.today())
date_old = datetime.datetime(day = my_data[1], month = my_data[2], year = my_data[3])
date = date_old
print(date)
print('Количество дней от вашей даты рождения до текущей даты:', (datetime.datetime.today()-date).days)

#8___________FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все___________
q = queue.Queue()  #создание очереди
print('8) Добавьте предмет ')
for i in list(disc_marks):  #добавление новых элементов к очереди - .put()
    q.put(i)
while True:
    index = input("Введите индекс(0-14) для добавления предмета в очередь. Нажмите Enter для остановки ")
    print()
    if index == '':
        break
    else:
        try:
            index = int(index)
            subject = list(disc_marks.keys())[index]
            q.put(subject)
        except (ValueError, IndexError):
            break
print(' FIFO очередь: ')
while True:
    print(q.get(), end=', ')  #возвращение элементов очереди - .get()
    if q.empty()==True: # .empty() возвращает True, если очередь пуста
        break
print('\n')

#9___________по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя___________
actec_prav = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
number = (int(my_data[1]) + int(my_data[2])**2 + int(my_data[3])) % 21 + 1  #номер имени правителя
print('9) Замена имени в отсортированном списке родственников:' )
print('  Под ', number, 'номером имя ацтекского правителя:', actec_prav[number])
index = int(input('  Введите индекс от 0 до 12: ')) #ввод индекса имени родственника
if index < 0 or index > 12:
    print("ERROR")
else:
    family_names[index] = actec_prav[number]
    print('  Обновленный список имён:', family_names)
print('\n')

#10___________количество дней от вашей даты рождения до текущей даты___________
relatives_dict = {}
sorted_relatives = sorted(dict_family_names, key=lambda x: int(x.split()[1]))
print('10) Упорядоченный список родственников по годам рождения:', sorted_relatives)
for i in range(len(sorted_relatives) - 1):
    relatives_dict[sorted_relatives[i]] = sorted_relatives.index(sorted_relatives[i+1])
relatives_dict[sorted_relatives[-1]] = 0
print('  Связный список, где ключ - имя родственника, а значение индекс следующего имени по исходному списку:', relatives_dict)
print('\n')

#11______________________________Функция-генератор____________________________
number = len(my_data[0]) * len (family_names) % 4 #выбор своего варианта

#Аликвотная последовательность
def aliquot(number):
    a = 0
    for i in range(10):
        yield a
        a = a + number
        if a == 0:
            break
        
#Последовательность Сильвестра
def sylvester():
    a = 2
    yield a
    for i in range(9):
        a = a * a + 1
        yield a
        
#Числа трибоначчи
def tribonacci():
    a, b, c = 0, 0, 1
    yield a
    yield b
    yield c
    for i in range(7):
        d = a + b + c
        yield d
        a = b
        b = c
        c = d
        
#Числа Леонардо
def leonardo():
    a, b = 1, 1
    yield a
    yield b
    for i in range(8):
        a, b = b, a + b + 1
        yield b

#Выбор нужной последовательности
if number == 0:
    sequence = aliquot(number)
    sequence_name = 'аликвотной последовательности'
elif number == 1:
    sequence = sylvester()
    sequence_name = 'последовательности Сильвестра'
elif number == 2:
    sequence = tribonacci()
    sequence_name = 'числа трибоначчи'
else:
    sequence = leonardo()
    sequence_name = 'числа Леонардо'

print('11) Была выбрана функция-генератор', sequence_name)
for i, num in enumerate(sequence):
    print( num, end=' ')
    if i >= 9:
        break
