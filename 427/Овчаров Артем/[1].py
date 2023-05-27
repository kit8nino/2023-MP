import queue
import datetime
#Начальные данные 

my_data = ("Овчаров", "Артём ", "Сергеевич", 25, 1, 2003)

my_grades = {"Русский": 5 ,
           "Литература": 5 ,
           "Обществознание": 5 ,
           "Экономика": 5 ,
           "Право": 5 ,
           "Биология": 5 ,
           "Химия": 5 ,
           "История": 5 ,
           "География": 5 , 
           "Алгебра": 5 ,
           "Геометрия": 5 ,
           "Английский": 5 ,
           "Физика": 5 ,
           "Астрономия": 5 ,
           "География": 5 , 
           "Физкультура": 5,
           "ОБЖ":5 }
                  
my_family = ["Сергей 1971", "Виктория 1969", "Дарья 1987", "Зинаида 1987", "Владислав 1997",
           "Алексей 2010 ", "Ксения 2013", "Вероника 2017", "Кирилл 2020", "Зинаида 1936", "Николай 1950",
           "Григорий 1935", "Ала 1952", "Татьяна 1960" , "Игорь 1965", "Игорь 1976", "Илья 1982", "Игорь 1987"]

pet_name = "КняZz"

aztec_names = ["Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Acamapichtli",\
"Tenoch", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl",\
"Moctezuma II", "Cuitláhuac", "Cuauhtémoc","Motelchiuhtzin", "Xochiquentzin",\
"Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]


sum_my_grades=0
sum_school_subjects=""
for  key, value in my_grades.items():
    sum_my_grades+=value
    sum_school_subjects+=key
    
# 1.Средняя оценка в аттестате    
average_grade = sum_my_grades/len(my_grades.values())
print (average_grade)

# 2.Уникальные имена в моей семье 
Uname=[]
Uname.append(my_data[1]) 
for i in my_family:   
    if i.strip("1234567890 ") not in Uname:
       Uname.append(i.strip("1234567890 "))
 
print(Uname)

#3 Общая длина строки из всех названий предметов 
print(len(sum_school_subjects))

#4 Уникальные буквы в названиях предметов
unique_letters = []
for letter in sum_school_subjects:
    if letter not in unique_letters:
        unique_letters.append(letter)
print(unique_letters)


#5 Имя кивы в бинарном виде
print( ' '.join(format(ord(x), 'b') for x in pet_name))

#6 Отсортированный по алфавиту (в обратном порядке) список родственников
my_family.sort(reverse = True)
print(my_family)

#7 Количество дней от моей даты рождения до текущей даты
starting_date = datetime.date(int(my_data[5]),int(my_data[4]),int(my_data[3]))
today_date = datetime.date.today()
cc = str(today_date - starting_date)
print(cc.split()[0], "д. ")
 
#8 FIFO очередь

fifo = queue.Queue()

print("Введите номер предмета , который вы хотите добавить в очередь от 1 до 17,\
 любое другое число не из этого интервала - выход ")
t = True 
subjects = []
for i in my_grades.keys():
    subjects.append(i)
    
while t:
    j = int(input())
    if j>=1 and j<=17:
        fifo.put(subjects[j-1])
    else:
        t = False

while True:
    print(fifo.get(), end=', ')
    if fifo.empty()==True:
        break
print('\n')

#9  поменять имя в отсортированном списке родственников на имя ацтекского правителя

number_of_aztec = (my_data[3] + my_data[4]**2 + my_data[5]) % 21 + 1;
number = int(input("Введите номер  имени родственника  для его замены на имя ацтека: "))   
my_family[number] = aztec_names[number_of_aztec] + " " + "".join(c for c in my_family[number] if  c.isdecimal())
print(*my_family)

#10 создать связный список, например, как словарь, где ключ - имя родственника, а значение (ссылка на следующий элемент) 

sorted_my_family = sorted(my_family, key=lambda x: int(x.split()[1]))
my_family_dict = {}

for i in range(len(my_family)):
    if i == len(sorted_my_family)-1:
        my_family_dict[sorted_my_family[i]] = None
    else:
        my_family_dict[sorted_my_family[i]] = sorted_my_family[i+1]
        
print("Связный список :")

for key, value in my_family_dict.items():
    print(f"{key} -> {value}")
    
#11 написать функцию-генератор 
    
def aliquot(x):
    x_next = 0
    
    for i in range(1, x):
        if x % i == 0:
            x_next += i
    
    if x == x_next :
        print( x_next , " в периоде " )
    elif x_next != 0 : 
        aliquot(x_next)
    #print( x_next , end=' ')
    x_arr.append(x_next)
    x_ar = x_arr[::-1]
    return x_ar

n = int(input("Введите число для начала аликвотной последовательности: "))
x_arr = []
print(f"Аликвотная последовательность числа {n}:")

c = aliquot(n)
c = [n] + c
print (*c)    
    
    
    