import datetime
import queue

a=('Исайкина','Мария', 'Андреевна','20','04','2003') 
b={'Геометрия':5,'Алгебра':5,'Информатика':5,'Физика':5,'Химия':5,'Биология':5,'История':5,'Литература':5,'Русский язык':5,'Физическая культура':5,'Английский язык':5,'Музыка':4,'Экономика':4,'География':5}
c=['Татьяна 1954','Сергей 1953','Ирина 1979','Андрей 1977','Анна 2010','Анатолий 1981','Владимир 1952','Владимир 1983','Валентина 1955']
d="Акечи"

#1
sum=0
k=0
for i,j in b.items():
    sum+=int(j)
    k+=1
print("Средняя оценка атестата: ",sum/k)

#2
l=[0]*(len(c)+1)
l[0]=a[1]
c1=[0]*(len(c)+1)
c1[0]=a[1]
o=0
print("Уникальные имена среди моих родственников:", end=" ")
for i in range(1,len(c)+1):
    c1[i]=c[i-1].strip('1234567890 ')
    l[i]=c[i-1].strip('1234567890 ')
for i in range(0,len(c)+1):
    for j in range(0,len(c)+1):
        if (i!=j) and (c1[i]==l[j]):
            o=1
    if (o==0):
        print(c1[i], end=' ')
    o=0        
    
#3
p=0
sum=0
for i in b.keys():
    sum+=len(i)
print("\nОбщая длина всех названий предметов:",sum)

#4
m=[]
n=[]
for i in b.keys():
    m+=i
    n+=i
o=0
print("Уникальные буквы в названиях предметов:", end=" ")
for i in range(0,len(m)):
    for j in range(0,len(m)):
        if (i!=j) and (m[i].lower()==n[j].lower()):
            o=1
    if (o==0):
        print(m[i].lower(),end=' ')
    o=0
    
#5
m=list(d)
print("\nИмя моей домашней пушистой кивы в бинарном виде:", end=" ")
for i in range(0,len(d)):
    m[i]=int(ord(m[i]))
    m[i]=bin(m[i])
    print(m[i][2:], end=" ")

#6
print("\nOтсортированный по алфавиту (в обратном порядке) список родственников:", end=" ")
l.pop(0)
l.sort(reverse=True)
for i in range(0,len(l)):
    print(l[i],end=" ")

#7
print("\nКоличество дней от моей даты рождения до текущей даты:", end=" ")
date_now=datetime.date.today()
date_birth=datetime.date(int(a[5]),int(a[4]),int(a[3]))
print((str(date_now-date_birth)).split()[0])

#8
print("FIFO очередь, в которую можно добавляются предметы по вводимому с клавиатуры индексу (от 1 до 14, число вне интервала - команда остановки):", end=' ')
och=queue.Queue()
i=0
p=[0]*len(b)
j=0
for i in b.keys():
    p[j]=i
    j+=1
i=1
while (i>=1) and (i<=14):
    i=int(input())
    if (i>=1) and (i<=14):
        och.put(p[i-1])
    else:
        break
while not och.empty():
    print(och.get(), end=" ")

#9
nom=(int(a[3]) + (int(a[4]))**2 + int(a[5])) % 21 + 1
print("\nВведите индекс (от 1 до 9), чтобы поменять имя одного из родственников на имя ацтекского правителя, получаемого под номером", nom,":", end=" ")
i=int(input())
if (i>=1) and (i<=9):
    l[i-1]="Уитцилиуитль"
else:
    print("См. интервал!")
for i in range(0,len(l)):
    print(l[i],end=" ")

#10
print("\nCвязный список, где ключ - имя родственника, а значение - индекс следующего имени: ", end=' ')
c2=[0]*len(c)
o=0
f=0
for i in range(0,len(c)):
    c2[i]=c[i].split()
for i in range(0,len(c)):
    for j in range(0,len(c)):
        if (c2[j][1]>c2[i][1]):
            f=c2[i]
            c2[i]=c2[j]
            c2[j]=f
dictionary=dict()
dictionary[c2[0][0]]=1
for i in range(1,len(c2)):
    dictionary[c2[i][0]]=i+1
print(dictionary)

#11

def tribon(t1,t2,t3):
    return t1+t2+t3
p=[]
for i in range(0,len(l)):
    p+=list(l[i])
num=(len(a[0])+len(a[1])+len(a[2]))*len(p)%4
print("\nФункция-генератор под номером",num, ":",end=" ")
#числа трибоначчи
f=[0]*1000
f[0]=0
f[1]=0
f[2]=1
print(f[0], f[1],f[2], end=" ")
j=0
while f[j+2]<=999999:
    f[j+3]=tribon(f[j+2],f[j+1],f[j])
    print(f[j+3], end=" ")
    j+=1