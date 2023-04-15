from datetime import datetime
import queue

###Исходные данные###

#ФИО+дата рождения
my_data = ("Белова Анастасия Алексеевна", 11, 11, 2003) 

#предметы в школьном аттестате, как словарь из названия и оценки
disk_marks = {"русский язык": 5,"литература": 5,"алгебра": 5,"геометрия": 5,"история": 5,
              "информаика": 5,"обж": 5,"физкультура": 5,"обществознание": 5,"черчение": 5,
              "химия": 5,"физика": 5,"география": 5,"английский язык": 5,"биология": 5} 

#имена (только) ближайших (до двоюродных включительно) родственников в списке и их год рождения через пробел (в одной строке);
family_names = ["Анастасия 2003", "Евгения 1980", "Алексей 1977", "Александр 2018",
                "Валентина 1954", "Александр 1950", "Татьяна 1973", "Юлия 1996",
                "Юрий 1972", "Людмила 1973", "Илья 2002", "Ольга 1995", "Нина 1946"] 
 
#имя, которое вы бы дали своей домашней пушистой киве (строка)
kiwa_name = "Гомункул" 

###Действия###

###1.Вывести среднюю оценку в аттестате###
average_mark = sum(disk_marks.values())/len(disk_marks.values())
print("1.Средняя оценка в аттестате:", average_mark)

###2.Вывести уникальные имена среди своих родственников (включая свое)###
unique_names = list(set(family_names))
print("2.Уникальные имена среди родственников:\n", unique_names)

###3.общая длина всех названий предметов###
lenght_disk_marks = [0]*len(disk_marks.values())
count = 0
disk_marks_string = ""
for i in disk_marks.keys():
    lenght_disk_marks[count] = i
    disk_marks_string += lenght_disk_marks[count]
    count += 1
print("3.Общая длина всех названий предметов:", len(disk_marks_string))

###4.уникальные буквы в названиях предметов###
unique_letter = {}
for letter in disk_marks_string:
    if letter in unique_letter:
        unique_letter[letter]+=1
    else:
        unique_letter[letter]=1
print(f"4.Уникальные буквы в названиях предметов: {', '.join(unique_letter)}")

###5.имя вашей домашней пушистой кивы в бинарном виде###
bin_kiwa_name = list(format(c, 'b') for c in bytearray(kiwa_name, "utf-8"))
print("5.Имя пушистой кивы в бинарном виде:", bin_kiwa_name)

###6.отсортированный по алфавиту (в обратном порядке) список родственников;###
family_names.sort(reverse=True)
print("6.Отсортированный по алфавиту (в обратном порядке) список родственников:\n", family_names)

###7.количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)###
print("7.Количество дней от даты рождения до текущей даты: {}".format((datetime.now() - datetime(day=int(my_data[1]), month=int(my_data[2]), year=int(my_data[3]))).days))

###8.FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все###
q = queue.Queue()
print('   Чтобы прекратить ввод нажмите Enter: ')
for i in list(disk_marks):
    q.put(i)
while True:
    subject = input('   ')
    if subject == '':
        break
    else:
        q.put(subject)
print("8. FIFO очередь из всех предметов: ")
while True:
    print(q.get(), end=', ')
    if q.empty()==True:
        break
print('\n')

###9.по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя###
new_name = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']
number = (int(my_data[1]) + int(my_data[2])**2 + int(my_data[3])) % 21 + 1
print("   Числу", number, "соответствует имя правителя - ", new_name[number])
index = int(input("   Введите индекс от 0 до 11: "))
if index < 0 or index > 11:
    print("ERROR")
else:
    family_names[index] = new_name[number]
    print("9.Обновленный список имён:\n", family_names)
    
###10.создать связный список, например, как словарь, где ключ - имя родственника, ####
###а значение (ссылка на следующий элемент) - индекс следующего имени по исходному списку,####
###упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться неизменным ###
family_names_new = {"Нина 1946":1, "Александр 1950":2, "Валентина 1954":3, "Юрий 1972":4, "Людмила 1973":5, "Татьяна 1973":6,
                    "Алексей 1977":7,"Евгения 1980":8, "Ольга 1995":9, "Юлия 1996":10, "Илья 2002":11, "Анастасия 2003":12, "Александр 2018":0}
print("10.Список, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку, упорядоченному по годам рождения:\n", family_names_new)

###11.Написать функцию-генератор###
number_generator = len(my_data[0]) * len (family_names) % 4 #выбор своего варианта

###Аликвотная последовательность###
def aliquot(number_generator):
    a = 0
    for i in range(10):
        yield a
        a = a + number_generator
        if a == 0:
            break
        
###Последовательность Сильвестра###
def sylvester():
    a = 2
    yield a
    for i in range(9):
        a = a * a + 1
        yield a
        
###Числа трибоначчи###
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
        
###Числа Леонардо###
def leonardo():
    a, b = 1, 1
    yield a
    yield b
    for i in range(8):
        a, b = b, a + b + 1
        yield b

#Выбор нужной функции
if number_generator == 0:
    sequence = aliquot(number_generator)
    sequence_name = "аликвотной последовательности"
elif number_generator == 1:
    sequence = sylvester()
    sequence_name = "последовательности Сильвестра"
elif number_generator == 2:
    sequence = tribonacci()
    sequence_name = "числа трибоначчи"
else:
    sequence = leonardo()
    sequence_name = "числа Леонардо"

print(f"11.Была выбрана функция-генератор {sequence_name}:")
for i, num in enumerate(sequence):
    print(num, end=' ')
    if i >= 9:
        break