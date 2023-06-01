# [1] работа со структурными данными

my_info = ("святов кирилл олегович", 9, 8, 2003)
marks = {"русский": 4,"литература": 5,"алгебра": 5,"геометрия": 5,"информатика": 5,"история россии": 4,"история всеобщая": 5,"физика": 4,"физра": 5,"астрономия": 5,"прокрастинация": 5,"прогуливание": 3,"поглаживание котят": 5,"запоминание имен": 2,}
family_names = ["рома","таня","ваня","маша","наташа","ваня","катя","оля","рома","алиса"]
kiwa_name = "мк-15"

#N1 вывести среднюю оценку в аттестате;
print("N1 вывести среднюю оценку в аттестате")
average_mark = sum(marks.values()) / len(marks)
print(average_mark)

#N2 вывести уникальные имена среди своих родственников (включая свое);
print("\nN2 вывести уникальные имена")
unique_names = list(set(family_names))
unique_names.append((my_info[0])[7:13])
print(*unique_names)

#N3 общая длина всех названий предметов;
print("\nN3 общая длина всех названий предметов")
len_marks = 0
for i in marks:
    len_marks += len(i)
print(len_marks)

#N4 уникальные буквы в названиях предметов;
print("\nN4 уникальные буквы в названиях предметов")
unique_letters,x,z=[],[],0
for i in marks:
    for j in i:
        for k in x:
            if j == k:
                z+=1
        if z==0:
            x.append(j)
        z=0
for i in x:
    for j in marks:
        for k in j:
            if i == k:
                z+=1
    if z==1:
         unique_letters.append(i)
    z=0        
print(*unique_letters)

#N5 имя вашей домашней пушистой кивы в бинарном виде;
print("\nN5 имя вашей домашней пушистой кивы в бинарном виде")
kiwa_name_bin =  ''.join(format(ord(x), '08b') for x in kiwa_name)
print(kiwa_name_bin)

#N6 отсортированный по алфавиту (в обратном порядке) список родственников;
print("\nN6 отсортированный по алфавиту (в обратном порядке) список родственников")
def quicksort(nums, f, l):
    if f >= l: 
        return
    i, j = f, l
    p = nums[(l + f) // 2]
    while i <= j:
        while nums[i] > p: i += 1
        while nums[j] < p: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        quicksort(nums, f, j)
        quicksort(nums, i, l)
unique_names.remove("кирилл")
quicksort(unique_names, 0, len(unique_names)-1)
print(*unique_names)

#N7 количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной);
print("\nN7 количество дней от вашей даты рождения")
import datetime as dt
time_now = dt.datetime.today()
time_birth = dt.datetime(day=my_info[1], month=my_info[2], year=my_info[3])
print((time_now-time_birth).days)
#7174

#N8 FIFO очередь
print("\nN8 FIFO очередь")
import queue
q = queue.Queue(100)
a = int(input("чтобы выйти из очереди, введите: '0'\n"))
while a!=0:
    q.put(a)
    a = int(input())
print("полученная очередь: ",end='')
while not q.empty():
    print(q.get(),end=' ')
print()

#N9 по введеному индексу, поменять имя ... на имя ацтекского правителя
print("\nN9 по введеному индексу, поменять имя ... на имя ацтекского правителя")
number = (my_info[1] + my_info[2]**2 + my_info[3]) % 21 + 1
print(number, "= Diego de San Francisco Tehuetzquititzin")
a = int(input("введите индекс:"))
if(a>len(unique_names)):
    while(a>len(unique_names)):
        a-=len(unique_names)
unique_names[a-1]='Tehuetzquititzin'
print(*unique_names)

#N10 связный список
print("\nN10 связный список")
family_years = {"таня": 1990,"рома": 1993,"оля": 1987,"наташа": 2000,"маша":2005,"катя":2010,"ваня":1978,"алиса":2020}
sorted_fy,linked_list = sorted(family_years.items(), key=lambda x: x[1]),{}
for i,j in enumerate(sorted_fy):
    name = j[0]
    if i < len(sorted_fy) - 1:
        k = i + 1
        next_name = sorted_fy[k][0]
        linked_list[name] = next_name
    else:
        linked_list[name] = 'ваня'
for i,j in linked_list.items():
    print(i,":",j)

#N11 функция генератор
print("\nN11 функция генератор")
num = len(my_info[0])*len(family_names)%4
print(num, "- аликвотной последовательности")
n = int(input("введите число, от которого мы будем считать последовательность: "))
def alikvot(n):
    print(n,end=', ')
    a = 0
    for i in range(1,n):
        if n%i == 0:
            a += i
    if a != 0:
        return alikvot(a)
    else: 
        print('0')
alikvot(n)
