import datetime

my_data = ("Морозов Никита Сергеевич", 17, 6, 1987)
disc_marks = {
    "русский": 4, 
    "литература": 5, 
    "алгебра": 5, 
    "история": 3, 
    "ОБЖ": 5
    }
family_names = ["Саша", "Серёга", "Ярослава", "Оля", "Серёга"]
kiwa_name = "Снежиночка"

average_mark = sum(disc_marks.values()) / len(disc_marks.values())
unique_names = []
for name in family_names:
    if name in unique_names:
        continue
    unique_names.append(name)

u_names = set(family_names)
for i in u_names:
    print(i)
    
for ch in bytearray(kiwa_name, 'utf-8'):
    print(bin(ch))
    
sorted_names = sorted(family_names)
family_names.sort()
print(*family_names)