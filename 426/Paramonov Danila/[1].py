import numpy as np

FIO = ("Парамонов", "Данила", "Александрович", 30, "Июля", 2003)
birthdate = (30, 7, 2003)
certificate = {"Математика": 4, "Русский язык": 5, "Литература": 5, "Физика": 4, "Химия": 4, "Биология": 5, "Английский язык": 5, "Информатика": 5, "География": 5, "Обществознание": 5, "История": 5, "ОБЖ": 5, "Музыка": 5, "Физкультура": 5, "МХК":5} 
family_names = ["Даня 2003", "Александр 1982", "Елена 1980", "Артём 2005", "Ольга 1958", "Татьяна 1956", "Сергей 1955","Владимир 1959", "Ирина 1986", "Ольга 1978", "Александр 1982", "Вера 1938", "Елена 1935"]
kivas_name = "Мотильда"

# №1 Средняя оценка в аттестате

average_mark = sum(certificate.values()) / len(certificate)
print("Средняя оценка в аттестате:", average_mark)
print()

# №2 Уникальные имена среди родственников 

sort_f_n = sorted(family_names, key=lambda x: x.split()[0])
sorted_f_n = [x.split()[0] for x in sort_f_n]
name_list = [len(sorted_f_n)] 
unique_names = list(set(sorted_f_n)) 
print(unique_names)
print()

# №3 Общая длина всех названий предметов

lenght = certificate.keys()
subject_length = sum(len(name) for name in lenght)
print("Общая длина названий предметов:", subject_length)
print()

# №4 Уникальные буквы в названиях предметов

letters_list = []
for word in certificate:
    for letter in word:
        if letter.isalpha(): 
            letters_list.append(letter)
    
unique_letters= list(set(letters_list)) 
print("Уникальные буквы в названиях предметов",unique_letters)
print()

# №5 Имя домашней пушистой кивы в бинарном виде

bin_kiva_name = ' '.join(format(ord(char), 'b') for char in kivas_name)
print("Имя домашней пушистой кивы в бинарном виде:", bin_kiva_name)    
print()

# №6 Отсортированный по алфавиту (в обратном порядке) список родственников

sort_f_n = sorted(sorted_f_n, reverse=True)
sorted_f_n = sort_f_n
print("Отсортированный по алфавиту (в обратном порядке) список родственников: ",sorted_f_n)
print()

# №7 Количество дней от даты рождения до текущей даты.

import datetime

birthdate = datetime.date(2004, 1, 29)
today = datetime.date.today()
days_since_birthday = (today - birthdate).days
print("Количество дней от даты рождения до текущей даты:", days_since_birthday)
print()

# №8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все

queue = []
print("Введите индекс элемента, который нужно добавить в очередь (для остановки введите stop): ")
while True:
    try:
        index = int(input())
        queue.append(index)
    except:
        break
print("Очередь:", queue)

# №9 По введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя

number = (30 + 7**2 + 2003) % 21 + 1
print(number)
ruler = ["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]
print(len(ruler))
n=3
i=2
while i < n:
    index = int(input("Введите индекс родственника для замены имени: "))
    if (index <= len(sorted_f_n)):
        i += 1
        if index < number:
            number -= index
        sorted_f_n[index-1] = ruler[number-1]
        print("Изменённый список родственников:",sorted_f_n)
        print()
    elif index > len(sorted_f_n):
        print("Максимально допустимый индекс = 13, веедите число < 13")
        i = 2

# №10 Cоздать структуру данных, похожую на словарь, но представляющую связный список. В этой структуре ключами будут имена родственников, а значениями будут индексы следующих имен в исходном списке. Исходный список останется неизменным. Элементы в структуре данных будут упорядочены в соответствии с годами рождения родственников.

names_list = [item.split()[0] for item in family_names]
numbers_list = [int(item.split()[1]) for item in family_names]
# numbers_list.sort()
family_dict = {}
sorted_ind = sorted(range(len(numbers_list)), key = lambda k: numbers_list[k])
for i in range(len(sorted_ind)-1):
    family_dict[names_list[sorted_ind[i]]] = sorted_ind[i+1]
family_dict[names_list[sorted_ind[-1]]] = None
print("Связный список: ",family_dict)

# №11 Функция-генератор 

def generate_sequence(family_names):
    number = len("ПарамоновДанилаАлександрович") * len(family_names) % 4
    count = 0  # инициализируем счетчик
    if number == 0:
        # Аликвотная последовательность
        n = 1
        while count < 30:  # limit to 30 elements
            yield n
            n += sum(1 for i in range(1, n) if n % i == 0)
            count += 1
    elif number == 1:
        # Последовательность Сильвестра
        a, b = 2, 3
        yield a
        yield b
        count += 2
        while count < 30:  # ограничение до 30 элементов
            c = a + b + 1
            yield c
            a, b = b, c
            count += 1
    elif number == 2:
        # Числа трибоначчи
        a, b, c = 0, 0, 1
        while count < 30:  # ограничение до 30 элементов
            yield c
            a, b, c = b, c, a + b + c
            count += 1
    elif number == 3:
        # Числа Леонардо
        a, b = 1, 1
        yield a
        yield b
        count += 2
        while count < 30:  # ограничение до 30 элементов
            c = a + b + 1
            yield c
            a, b = b, c
            count += 1
sequence = generate_sequence(family_names)
sequence_list = list(sequence)
print(sequence_list)
