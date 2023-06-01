import datetime
import queue
im = ("Лыков Аркадий Михайлович", 25, 2, 2003)
predmet = {
    "Русский": 3, 
    "литература": 4, 
    "алгебра": 3,
    "геометрия":3,
    "физика":3,
    "английиский":4,
    "химия":3,
    "биология":4,
    "информатика":3,
    "география":5,
    "обществознание":5,
    "астрономия":5,
    "история": 5, 
    "ОБЖ": 5,
    "Физкультура":5
    }
semia = ["Гоша", "Дима", "Марина","Артем","Ева" ,"Денчик", "Ира","Гоша"]
ima = "Gloryi"

q = sum(predmet.values()) / len(predmet.values())
print('№1 : '+ str(q)+'\n')

 #2
q = []
for name in semia:
    if name in q:
        continue
    q.append(name)
print('№2 :')

q=set(semia)
for i in q:
    print(i)

 #3

q=0

for i in list(predmet):
    q+=(len(i))
print('\n'+'№3  : ',q,'\n')   
 
 #4

q=[]
for i in list(predmet):
     q.extend( list(set(i)))
w=set(q)
print('№4 : ',*w,'\n')
   
 #5    
print('№5 :'+'\n')
for char in bytearray(ima, 'utf-8'):
    print(bin(char))


 #6
        
sq=sorted(list(semia),reverse=True)
sq = list(reversed(semia))
print('\n','№6 :')
for i in sq:
    print(i)
    
 #7

q=datetime.datetime.today()
date_old=datetime.datetime(day=25,month=2,year=2003)
print('\n','№7 :','\n',q-date_old)

 #8
q=queue.Queue()
for i in list(predmet):
    q.put(i)
print('\n','№8  Добавьте предмет ','\n')
while True:
    w=input('Нажмите Enter,чтобы прекратить ввод с клавиатуры: ')
    if w=='':
        break
    else:
        q.put(w)
print('\n','Выввод всех предметов:')
while True:
    print(q.get())
    if q.empty()==True:
        break
print('\n')
#9 
atsteki=['Теноч','Акамапичтли','Уицилиуитль','Чимальпопока','Шиуитль Темок','Ицкоатль','Моктесума I','Атотоцтли','Ахаякатль','Тизок','Ауисотль','Моктесума II','Куитлауак','Куаутемок','Тлакоцин','Мотельчиуцин','Сочикенцин','Хуаницин','Техуэцкитицин','Сечетцин','Сипак']
i=int(input('Введите индекс списка имен Родственников,отсортированный по алфавиту (в обратном порядке):'))
n=(im[1]+(im[2])**2+im[3])%21+1
print('\n','Имя ',sq[i],' поменяно на ',end='')
sq[i]=atsteki[n-1]
print(sq[i])

#10
q = { "Дима":1,"Ева":2 ,"Гоша":3,"Денчик":4, "Марина":5,"Артем":6,"Ира":7,"Гоша":0}
print(q) 
#11
q=len(im[0])*len(semia)%4
print('q=',q)
def divisors(n):
    for i in range(1,n):
        if n % i==0:
            yield i

n=int(input('Введите значение числа n ,с которого начнётся последовательность n= '))
q=0
w=[]

while n!=0:
    a=0
    for i in divisors(n):
        a += i
    n=a
    w.append(a)
    q+=1
    if q==500:
        break
print('\n','Аликвотная последовательность: ',w)

atsteki=['Ицкоатль','Моктесума I','Атотоцтли','Ахаякатль','Тизок','Ауисотль','Моктесума II','Куитлауак','Куаутемок']
i=int(input('Введите индекс списка имен Родственников,отсортированный по алфавиту (в обратном порядке):'))
n=(im[1]+(im[2])**2+im[3])%21+1
while n>=9:
    n-=9
print('\n','Имя ',sq[i],' поменяно на ',end='')
sq[i]=atsteki[n]
print(sq[i])