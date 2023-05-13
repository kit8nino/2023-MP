import datetime
import queue 

my_data = ("Priadko Dmitry",11,10,2003)

attestate ={
            "Physical education": 5,
            "Russian language": 4,
            "English language": 5,
            "Physics": 5,
            "Chemestry": 4,
            "Algebra": 5,
            "Informatics": 5,
            "Geometry": 4,
            "History": 5,
            "Social science": 5,
            "Literature": 4,
            "Geography": 5,
            "Technical drawing": 5,
            "Biology": 5,
            "Visual art": 5,
            }

attestate_list =list(attestate)
family_names =['Антон','Тихон','Прохор','Матвей','Ратибор','Дмитрий']

kiwi_name ="microdude" 


#1 (вывести среднюю оценку в аттестате):

mark_average = sum(attestate.values())/len(attestate)
print("#1\naverage mark= ",mark_average) 

#2 (вывести уникальные имена среди своих родственников (включая свое))

unique_names=list(set(family_names))
print("\n#2\n",unique_names)


#3 (общая длина всех названий предметов)

length =0 
for i in list(attestate):
    length+=(len(i))
print("\n#3\n",length)

#4 (уникальные буквы в названиях предметов)

unique_letter=[]
for key in attestate:
    for ch in key:
        if ch not in unique_letter:
            unique_letter.append(ch)
print("#4\n",unique_letter)

#5 (имя вашей домашней пушистой кивы в бинарном виде)

for i in range(len(kiwi_name)):
    print(bin(ord(kiwi_name[i])))

#6 (отсортированный по алфавиту (в обратном порядке) список родственников)

family_names_sorted = sorted(family_names, reverse=True)
print("#6\n",family_names_sorted)

#7 (количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной))

today = datetime.datetime.today()
my_bday = datetime.datetime(day =my_data[1],year =my_data[3],month=my_data[2])
print((today-my_bday).days) 

#8 (FIFO очередь)

print("Условие выхода: -1, Мин- 1, Макс - 15")
things = queue.Queue()
subject = queue.Queue()
k = int(input())
while k!=-1:
    if(k<1 or k>15):
        print("Некорректное значение")
    else:
        things.put(k)
        subject.put(attestate_list[k-1])
    k = int(input())
print("Вы ввели: ",end='')
while things.empty()!=True:
    print(things.get(), end=', ')
print("\nПо ключам словоря: ",end='')
while subject.empty()!=True:
    print(subject.get(), end=', ')
print()

#9 (поменять имя в отсортированном списке родственников на имя ацтекского правителя)

Aztec = ['Tenoch', 'Acamapochtli', 'Huitzilihitl', 'Chimalpopoca', 'Xihuitl Temoc',
        'Itzcoatl', 'Moctezuma I', 'Atotoztli', 'Axayacatl', 'Tizoc', 'Ahuitzotl',
        'Moctezuma II', 'Cuitlahuac', 'Cuauhtrmoc', 'Tlacotzin', 'Motelchiuhtzin',
        'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Cecetzin', 'Cipac']

number =(my_data[1] + my_data[2]**2 + my_data[3]) % 21 + 1
print(f"#9\nИмя Ацтека по номеру: {number} - ", Aztec[number-1])

g=1
while g!=0:
    index = int(input("Введите интекс от 1 до 6: "))
    if(index <1 or index>6):
        print("Некорректное значение")
    else:
        g=0
family_names_sorted[index-1] = Aztec[number-1]
print("Изменненный список: ", family_names_sorted)

#10 (создать связный список)

def create_node(key, data):
    # Функция для создания нового узла
    return {'key': key, 'data': data, 'next': None}

def add_node(dic, key, data):
    # Функция для добавления нового узла в связный список
    new_node = create_node(key, data)

    # Если список пуст, то новый узел будет первым
    if dic is None:
        return new_node

    # Иначе находим место вставки нового узла
    prev_node = None
    cur_node = dic
    while cur_node is not None and cur_node['data'] <= data:
        prev_node = cur_node
        cur_node = cur_node['next']

    # Вставляем новый узел между prev_node и cur_node
    if prev_node is None:
        new_node['next'] = dic
        return new_node
    else:
        prev_node['next'] = new_node
        new_node['next'] = cur_node
        return dic

def get_linked_list(dic):
    # Функция для получения связного списка в виде словаря, где ключ - имя родственника, а значение - индекс следующего имени по возрастанию года рождения
    result_dict = {}
    cur_node = dic
    index = 0
    while cur_node is not None:
        result_dict[cur_node['key']] = index
        cur_node = cur_node['next']
        index += 1

    return result_dict

dic = None
print("Для выхода -1")
k=0
while k!=-1:
    name = input("Введите имя родственника: ")
    bdyear = int(input("Введите год рождения: "))
    dic = add_node(dic,name,bdyear)
    k = int(input("Выход?(-1): "))
    
result_dict = get_linked_list(dic)
print(result_dict)


#11 (функция-генератор) 
#len("ФИО") * len (family_names) % 4 = 0 -> аликвотная последовательность

def aliquot_sequence(n):
    sequence = [n]
    while True:
        aliquot_sum = sum([i for i in range(1, sequence[-1]) if sequence[-1] % i == 0])
        if aliquot_sum in sequence:
            sequence.append(aliquot_sum)
            break
        sequence.append(aliquot_sum)
    return sequence

n = int(input("#11\nВведите началное число последовательности: "))
print("Последовательность: ", aliquot_sequence(n))