import math as mt
import numpy as np  
import datetime
import queue
my_name=('Морев Артём Сергеевич','2','7','2003')
my_birthday=(2,7,2003)
my_marks={
    "русский":4,
	"математика":5,
	"физика":5,
	"химия":4,
	"история":4,
	"физкультура":5,
	"обж":5,
    "обществознание":4,
    "биология":5,
    "искусство":4,
    "геометрия":5,
    "английский":3,
    "литература":4,
    "география":5 
    }
family_names=['Шурик',"Сергей",'Сергей',"Артём","Ольга",'Павел','Екатерина','Павел']
kat_name=('Дымок')
# 1 Задание.(СРЕДНЯЯ ОЦЕНКА В АТТЕСТАТЕ)
print('******************************************************************')
average_mark=sum(my_marks.values())/len(my_marks.values())
print('Средняя оценка аттестата',average_mark)
unique_names=[]

# 2 Задание.(Уникальные имена родственников и их даты рождения, используя словарь, где ключ, имя родственника)
unique_names =set(family_names)
print('******************************************************************')
print('Уникальные имена',unique_names)
print('******************************************************************')

# 3 Общая длинна всех названий предметов
length=0
#найдём список ключей словаря:
for a in list(my_marks):
    length+=(len(a))
print("Общая длинна всех названий предметов =",length)
print('******************************************************************')

# 4 (УНИКАЛЬНЫЕ БУКВЫ В НАЗВАНИЯХ ПРЕДМЕТОВ)
#сделаем список множества состоящий из элементов ключей словаря
#1)Функция append() позволяет добавлять в список один новый элемент — например, число, строку или другой список.
#2)Функция extend() работает как append(), но в качестве параметра принимает итерируемый объект: список, кортеж или строку.
#Содержимое этого объекта поэлементно добавляется в другой список.
letters_subject=[]
for i in list(my_marks):
    letters_subject.extend(list(set(i)))
unique_letters=set(letters_subject)
print('УНИКАЛЬНЫЕ БУКВЫ НАЗВАНИЯ ПРЕДМЕТОВ',unique_letters)
print('******************************************************************')

# 5 ИМЯ КИВИ В БИНАРОМ ВИДЕ
#join() – берет все элементы и объединяет их в единый объект (в результате получается одна строка).
#ord() – этот метод принимает символ и преобразует его в соответствующее значение UNICODE.
#format() – метод принимает значение и вставляет его там, где присутствуют заполнители, он также используется для объединения частей строки с заданными интервалами.
#bytearray() – возвращает массив байтов.
#bin() преобразует целое число в двоичную (бинарную) строку с префиксом '0b'
#map-функция для обработки обЪектов без цикла for
print('Строка которую мы взяли для преобразования в двоичный код: ',kat_name)
bin_result=''.join(format(ord(x),'08b')for x in kat_name)
print('РЕЗУЛЬТАТ = ',bin_result)
print('******************************************************************')
    
# 6 отсортированный по алфавиту(в обратном порядке) список родственников
#Если вы хотите, чтобы сортировка выполнялась в обратном порядке, передайте обратный аргумент, как True.
#В Python есть встроенная функция sorted(), которая используется для создания отсортированного списка из итерируемого объекта.
family_names.sort(reverse=True)
print('Отсортированный список родственников в обратном алфавитном порядке',family_names)
print('******************************************************************')

# 7 количество дней от моей даты рождения до текущей даты (должна быть всегда актуальной);
#Сначала нужно импортировать класс datetime из модуля datetime, после чего создать объект
# datetime. Модуль предоставляет метод now(), который возвращает текущие дату и время с 
#учетом локальных настроек.
#datetime включает различные компоненты. Так, он состоит из объектов следующих типов
#date — хранит дату
#time — хранит время
#datetime — хранит дату и время
dt_now = datetime.datetime.now()#текущая дата(обновляемая)
birth_date = datetime.datetime(year=2003,month=7,day=2)
difference_of_days=(dt_now-birth_date).days
print('Количество дней от даты рождения до текущей даты',difference_of_days)
print('******************************************************************')

# 8 Вывод FIFO очереди
q=queue.Queue()
for i in list(my_marks):
    q.put(i)
print('ДОБАВИМ ПРЕДМЕТ')
while True:
    subject=input('Нажмите Enter,чтобы прекратить ввод с клавиатуры: ')
    if subject=='':
        break
    else:
        q.put(subject)    
print('СПИСОК ВСЕХ ПРЕДМЕТОВ')
while True:
    print(q.get())
    if q.empty()==True:
        break
print('\n')

    
# 9 АЦТЕКСКИЙ ПРАВИТЕЛЬ
Aztec=['Tenōch','Ācamāpichtli','Huītzilihhuitl','Chīmalpopōca','Xīhuitl Tēmoc','Itzcōhuātl','Motēuczōma Ilhuicamīna',
       'Atotoztli','Āxāyacatl','Tīzocic','Āhuitzotl','Motēuczōma Xōcoyōtl','Cuitlāhuac','Cuāuhtēmoc','Tlacotzin',
       'Motelchiuhtzin', 'Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']
Number = (int(my_name[1]) + int(my_name[2]) ** 2 + int(my_name[3])) % 21 + 1   
print('Индекс типа от 1 до ' +str(len(family_names))+ ' чтобы изменить имя члена семьи на ' + Aztec[Number-1])   
familylist=sorted(family_names)    
print(familylist)    
index=int(input())    
familylist[index-1]=Aztec[Number-1]
print(familylist)


# 10 ЗАДАНИЕ
# Словарь с датами рождения родственников
relatives = {}
while True:
    relative_name = input("Введите имя родственника (или 'стоп' для выхода): ")
    if relative_name == "стоп":
        break    
    relative_birthdate = input("Введите дату рождения родственника в формате ДД.ММ.ГГГГ: ")
    relatives[relative_name] = relative_birthdate
print(relatives)
sorted_relatives = sorted(relatives.items())
if Number <= len(sorted_relatives):
    relative_name_to_replace = sorted_relatives[Number-1][0]
    Aztec = Aztec[Number-1]
    del relatives[relative_name_to_replace]
    relatives[Aztec] = sorted_relatives[Number-1][1]
    print(f"Имя родственника '{relative_name_to_replace}' заменено на '{Aztec}'")
else:
    print(f"Нет родственника с индексом {Number} в списке, на этот раз без ацтеков")
print('----------------------------------------------------------------------------------------------------------------------')
print("Новый (или не тронутый) словарь с родственниками:")
print(relatives)    

#11 ФУНКЦИЯ ГЕНЕРАТОР
print("11)функцию-генератор, вариант определяется как number = len(ФИО) * len (family_names) % 4:)")
numberr=len(my_name[0]) * len (family_names) % 4   
print(numberr,'-Номер, получившийся по формуле - аликвотной последовательности:')    
def aliquot_sequence(number):
    a = 0
    for i in range(10):
        yield a
        a = a + number
        if a == 0:
            break

    
    
    
    
    
    
    
    
    
    
    
    
