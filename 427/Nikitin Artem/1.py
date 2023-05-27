
import pdb
data=('Никитин', 'Артём', 'Владимирович', 26, 10, 2003 )
subjects={
    'Русский язык':4,
    'Литература':4,
    'Алгебра':4,
    'Физика':5,
    'Химия':4,  
    'Геометрия':4,
    'Физическая культура':5,
    'ОБЖ':5,
    'Обществознание':5,
    'Музыка':5,
    'ИЗО':5,
    'История':4,
    'Английский язык':4,
    'Технология':5
    }
list_of_names=["Татьяна 1971","Галина 1936","Ольга 1994","Владимир 1950","Юля 1990","Нина 1967","Андрей 1987"]
pet="Пуси-Джуси"

#1 задание
print("'1 задание'\n")
mark=0
for i in subjects:
    mark+=(subjects[i])
sred_mark=mark/len(subjects)
print("Средний балл ",sred_mark,"\n")

#2 задание
print("'2 задание'\n")
a=[]
b=[]
for i in list_of_names:
    a.append(i.split())
for i in range(len(a)):
    if a[i][0] not in b:
        b.append(a[i][0])
b.append(data[1])
print(b, "\n")

#3 задание
print("'3 задание'\n")
summ=0
for i in subjects.keys():
    summ+=len(i)
print("Общая длинна всех предметов ",summ,"\n")

#4 задание
print("'4 задание'\n")
a1=""
c=[]
for i in subjects.keys():
    a1+=i
for i in range(len(a1)):
    if a1[i] not in c and a1[i]!=" ":
        c.append(a1[i])
print(c,"\n")

#5 задание
print("'5 задание'\n")
bin_pet=""
for i in pet:
    bin_pet+=format(ord(i),'08b')
print("Имя моего питомца в бинарном коде ",bin_pet,"\n")

#6 задание
print("'6 задание'\n")
rez=[]
Pravda=True
dictionary={}
alfavet=["Я","Ю","Э","Ъ","Ы","Ь","Щ","Ш","Ч","Ц","Х","Ф","У","Т","С","Р","П","О","Н","М","Л","К","Й","И","З","Ж","Ё","Е","Д","Г","В","Б","А"]
for i in range(len(b)):
    k=b[i]
    dictionary[b[i]]=alfavet.index(k[0])
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            d.pop(k)
            return k
while Pravda:
    if dictionary=={}:
        Pravda=False
    for i in range(len(alfavet)):
            if i in dictionary.values():
                rez.append(get_key(dictionary,i))
print(rez,"\n")

#7 задание
print("'7 задание'\n")
import datetime
from datetime import date
a=date.today()
my_birth=datetime.date(2003,10,26)
print("Количество дней от моей даты рождения",(a-my_birth).days,"\n")

#8 задание
print("'8 задание'\n")
Pravda=True
a=[]
subjects=list(subjects)
print("Введите индексы предметов от 1 до 14: пробел, чтобы выйти")
while Pravda:
    c=input()
    if c==' ':
        Pravda=False
    try:
        c1=int(c)
        if  int(c)>len(subjects) or int(c)<=0:
            print("Введён неверный индекс")
        else:
            c=int(c)
            a.append(subjects[c-1])
    except ValueError:
        print("Введён неверный индекс")
print(a)
    
#9 задание
print("\n'9 задание'\n")
number=(my_birth.day+my_birth.month**2+my_birth.year)%21+1
my_aztec_name="Axayacatl"
print("Список родственников ",rez)
print("Ведите индекс от 1 до ",len(rez))
Pravda=True
while Pravda:
    c=input()
    try:
         c1=int(c)
         if  int(c)>len(b) or int(c)<=0:
             print("Введён неверный индекс")
         else:
             c=int(c)
             rez[c-1]=my_aztec_name
             print(rez)
             Pravda=False
    except ValueError:
        print("Введён неверный индекс")

#10 задание
a=[]
print("\n'10 задание'\n")
for i in list_of_names:
    a.append(i.split())
for i in range(len(a)):
    name=a[i][0]
    date=a[i][1]
    a[i][0]=date
    a[i][1]=name
a.sort()
for i in range(len(a)):
    name=a[i][0]
    date=a[i][1]
    a[i][0]=date
    a[i][1]=name
dic=dict()
for i in range(len(a)):
    if i==len(a)-1:
        dic[a[i][0]]=0
    else:
        dic[a[i][0]]=i+1
print(dic,"\n")

#11 задание
print("\n'11 задание'\n")
number=len(data[0]+data[1]+data[2])*len(b)%4
#последовательность аликвот
print("Ведите число которое ходите разложить в последовательность аликвот \n")
n=int(input())
Pravda=True
spisok=[]
c1=0
spisok.append(n)
def find_deliteli(n):
    c=0
    if n==1:
        return(0)
    else:
        for i in range(1,n):
            if n%i==0:
                c+=i
        return(c)
while Pravda:
    j=find_deliteli(n)
    spisok.append(j)
    n=j
    if n==0:
        Pravda=False
        print(spisok)
    if c1>1 and (spisok[c1]==spisok[c1-1] or spisok[c1]==spisok[c1-2]) :
        Pravda=False
        print(spisok)
    c1+=1