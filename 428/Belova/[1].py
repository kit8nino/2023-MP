from datetime import datetime
import queue

###Исходные данные###
my_data = ("Белова Анастасия Алексеевна", 11, 11, 2003)
disk_marks = {
    "русский язык": 5,
    "литература": 5,
    "алгебра": 5,
    "геометрия": 5,
    "история": 5,
    "информаика": 5,
    "обж": 5,
    "физкультура": 5,
    "обществознание": 5,
    "черчение": 5,
    "химия": 5,
    "физика": 5,
    "география": 5,
    "английский язык": 5,
    "биология": 5
    }
family_names = ["Анастасия", "Евгения", "Алексей", "Александр", "Валентина", "Александр", "Татьяна", "Юлия", "Юрий", "Людмила", "Илья", "Ольга"]
kiwa_name = "Гомункул"

###Действия###
###1###
average_mark = sum(disk_marks.values())/len(disk_marks.values())
print("1.Средняя оценка в аттестате:", average_mark)

###2###
unique_names = list(set(family_names))
print("2.Уникальные имена среди родственников:", unique_names)

###3###
lenght_disk_marks = [0]*len(disk_marks.values())
count = 0
disk_marks_string = ""
for i in disk_marks.keys():
    lenght_disk_marks[count] = i
    disk_marks_string += lenght_disk_marks[count]
    count += 1
print("3.Общая длина всех названий предметов:", len(disk_marks_string))

###4###
unique_letter = {}
for letter in disk_marks_string:
    if letter in unique_letter:
        unique_letter[letter]+=1
    else:
        unique_letter[letter]=1
print("4.Уникальные буквы в названиях предметов:", unique_letter)

###5###
bin_kiwa_name = list(format(c, 'b') for c in bytearray(kiwa_name, "utf-8"))
print("5.Имя пушистой кивы в бинарном виде:", bin_kiwa_name)

###6###
family_names.sort(reverse=True)
print("6.Отсортированный по алфавиту (в обратном порядке) список родственников:", family_names)

###7###
print("7.Количество дней от даты рождения до текущей даты: {}".format((datetime.now() - datetime(day=int(my_data[1]), month=int(my_data[2]), year=int(my_data[3]))).days))

###8###
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

###9###
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
    print("9.Обновленный список имён:", family_names)