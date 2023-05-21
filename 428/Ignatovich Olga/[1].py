import datetime
import queue
from operator import itemgetter


my_data = ("Игнатович Ольга Дмитриевна", 21, 10, 2003)
disc_marks = {
    "русский": 4, 
    "литература": 5, 
    "алгебра": 5,
    "геометрия": 4,
    "история": 3,
    "география": 3,
    "биология": 4,
    "обществознание": 5,
    "музыка": 3,
    "физика": 4,
    "информатика": 5,
    "физкультура": 4,
    "ИЗО": 5,
    "ОБЖ": 5
    }
family_names = ["Ирина", "Дмитрий", "Алёна", "Татьяна", \
                "Алексей","Светлана","Сергей","Татьяна","Алексей"]

family_names_date = {
    "Ирина": "2001", 
    "Дмитрий": '1993', 
    "Алёна": '1980',
    "Татьяна(младшая)": '2004',
    "Алексей(старший)": '1999',
    "Светлана": '1988',
    "Сергей": '1978',
    "Татьяна": '1990',
    "Алексей": '2000'
    }

kiwa_name = "Брусничка"

#1

average_mark = sum(disc_marks.values()) / len(disc_marks.values())
print("Средние значение аттестата: ", average_mark)

#2

unique_names=set(family_names)
print("Уникальные имена: ", *unique_names, "Ольга")

#3

pred=[0]*len(disc_marks.values())
count=0
stroka_bykv=""
for i in disc_marks.keys():
    pred[count]=i
    stroka_bykv+=pred[count]
    count+=1
print("Число букв в предметах: ",len(stroka_bykv))

#4
lenght=sum(disc_marks.values())
#print(lenght)
k = {}
for i in stroka_bykv:
    if i in k:
        k[i] += 1
    else:
        k[i]=1
print("Число уникальных букв: ",k)

#5

print("Бинарный код кивы: ",*bytearray(kiwa_name, 'utf-8'))

#6

alf=list(set(family_names))
alf.sort(reverse= True)
print("Обратный порядок имен: ", *alf)

#7

today = datetime.datetime.today()
my_bday = datetime.datetime(day=my_data[1],
                            month=my_data[2],
                            year=my_data[3])
print("Количество дней от дня рождения до текущей даты: ", (today-my_bday).days)

#8

q=queue.Queue()
for i in disc_marks.keys():
    q.put(i)
    
while True:
    slovo=input('Введите новый предмет или stop: ')
    if slovo=='stop':
        break
    else:
        q.put(slovo)
        
while True:
    print(q.get())
    if q.empty()==True:
        break

#9

i=int(input('Введите число от 0 до 7: '))
number_drevnii=(my_data[1]+my_data[2]**2+my_data[3])%21+1

drevnii=["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Itzcoatl", "Moctezuma I",
    "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac",
    "Cuauhtémoc", "Coanacoch", "Totoquihuatzin", "Quinatzin", "Ixtlilxochitl",
    "Nezahualcoyotl", "Maxtla", "Tlacaelel", "Tlacopan", "Tlatoani Diego"]

alf[i-1]=drevnii[number_drevnii-1]

print("Замена на ацтекского правителя: ", *alf)


#10

sort_family=dict(sorted(family_names_date.items(), key=itemgetter(1)))

print('Сортировка имен по годам рождения: ', sort_family)

#11

fio=my_data[0]
#number = (len(fio) * len(family_names)) % 4
#print(number)

def sylvester():
    e=1.264084735305302
    for i in range(7):
        step=2**(i+1)
        b = int((e**step) + 0.5)
        yield b
    

posled=sylvester()
print('Функция-генератор: последовательность Сильвестра')

for i, num in enumerate(posled):
    print(num)
