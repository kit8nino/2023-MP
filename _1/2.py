import datetime
import queue

my_data = ("Морозов Никита Сергеевич", 17, 6, 1987)
attestate = {
            "физра": 4,
            "география": 3,
            "геометрия": 4,
            "информатика": 3,
            "ОБЖ": 5
            }
family_names = ['Толя', 'Катя', 'Катя', 'Ярослава']
kiwa_name = 'Пипидастр'

mean_mark = sum(attestate.values()) / len(attestate)
print('Mean mark: ', mean_mark)

unique_names = []
for name in family_names:
    if name in unique_names:
        continue
    unique_names.append(name)
print(unique_names)
print(*set(family_names)) # (f_names[0], f_names[1]....

print(*bytearray(kiwa_name, 'utf-8'))

today = datetime.datetime.today()
my_bday = datetime.datetime(day=my_data[1],
                            month=my_data[2],
                            year=my_data[3])
print((today - my_bday).days)

stuff = queue.Queue()
i = int(input())
while i != -1:
    stuff.add(i)
    i = int(input())
    
print(stuff)