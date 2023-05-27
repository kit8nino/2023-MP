import datetime 
from collections import deque

N=("Сухов Алексей Михайлович", 5, 9, 2003)
Att={'Русский язык': 5, 'Литература': 5, 'Английский': 5, 'Алгебра': 5, 'Геометрия': 5, 'Информатика': 5, 'История России': 5, 'Всеобщая история': 5, 'Обществознание': 5, 'География': 5, 'Биология': 5, 'Физика': 5, 'Астрономия': 5, 'Химия': 5}
C=['Мария 1982', 'Михаил 1977', 'Геннадий 1941', 'Лариса 1941', 'Анастасия 2010', 'Алексей 2003', 'Иван 2003', 'Ольга 1953','Виктор 1956' ]
kiva='Жерар'

#1
s=(Att.get('Русский язык')+Att.get('Литература')+Att.get('Английский')+Att.get('Алгебра')+Att.get('Геометрия')+Att.get('Информатика')+Att.get('История России')+Att.get('Всеобщая история')+Att.get('Обществознание')+Att.get('География')+Att.get('Биология')+Att.get('Физика')+ Att.get('Астрономия')+ Att.get('Химия'))/14
print('1) Средняя оценка аттестата:', s)
print()

#2
print('2) Уникальные имена:', list(set(C)))
print()

#3
x=len('Русский язык')+len('Литература')+len('Английский')+len('Алгебра')+len('Геометрия')+len('Информатика')+len('История России')+len('Всеобщая история')+len('Обществознание')+len('География')+len('Биология')+len('Физика')+len('Астрономия')+len('Химия')
print('3) Общая длина названий предметов:', x)
print()
import datetime 
from collections import deque

#4
u = []    
for i in list(Att):                           
    u += i                              
print("4) Уникальные буквы в названиях предметов:" , set(list(u))) 
print()

#5
bk= ' '.join(format(x, 'b') for x in bytearray(kiva, 'utf-8'))
print('5) Имя кивы в бинарном виде:',bk) 
print()

#6
C.sort(reverse=True)
print('6) Отсортированный по алфавиту (в обратном порядке) список родственников:', C)
print()

#7
today = datetime.date.today()
dr = datetime.date(2003, 9, 5)
raz = abs(dr - today)
traz=raz.days
print('7) Количество дней от моей даты рождения до текущей даты:', traz)
print()

#8
k = int(input("Введите количество элементов FIFO-списке:"))
p = [] 

for j in range(1, k + 1):
    e_f = input("Введите "+ str(j)+ "-й " + " элемент списка FIFO")
    p.append(e_f)
    
print("Введённая очередь:", p)


stop = input("Введите команду остановки: ")

while True:
    index = int(input("Введите индекс элемента: "))
    element = input("Введите элемент: ")                 
    if element == stop:
        break
    p.insert(index , element)                          
    
print("8) Полученная FIFO очередь:" , p)                   
print()

#9
p = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
            'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
            'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
            'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']

number = (5 + 9 ** 2 + 2003) % 21 + 1
print("Индекс правителя: ", number)
print()

C.sort()       
print(C)

index = int(input("Введите индекс из отсортированного списка:"))

C[index] = p[number]    
print("9) Список с замененным именем родственника:", C)
print() 

#10 
C_date=['Мария 1982', 'Михаил 1977', 'Геннадий 1941', 'Лариса 1941', 'Анастасия 2010', 'Алексей 2003', 'Иван 2003', 'Ольга 1953']
slovar={}
for i in range(len(C_date)):
    if i==len(C_date)-1:
        slovar[C_date[i]]=0
    else:
        slovar[C_date[i]]=i+1
print('10. Связный список:', slovar)
print()

number = len("Сухов Алексей Михайлович") * len (C) % 4
print(number , "= генератор аликвотной последовательности")

#11
number = int(input('Введите число любое натуральное число:'))
def ap(num):
    b = []
    apos = [num]
    while num >= 1:
        for i in range(1, num):
            if num == 1:
                aliquotPos.append(0)
            elif num % i == 0:
                b.append(i)
        summ = sum(b)
        apos.append(summ)
        num = summ
        b = []
    return apos
    
print('11. Аликвотная последовательность от вашего числа:',ap(number))
print()
