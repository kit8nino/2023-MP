from datetime import datetime

about_me = ('Софронов Илья Сергеевич', '28.02.2004')

school_grades = {'Математика' : 5, 
                 'Русский язык' : 5, 
                 'Литература' : 4, 
                 'Физика' : 4, 
                 'Информатика' : 5, 
                 'ОБЖ' : 5, 
                 'Химия' : 4, 
                 'Технология' : 5, 
                 'Иностранный язык' : 4, 
                 'Биология' : 5, 
                 'География' : 5, 
                 'Физкультура' : 5, 
                 'История' : 5, 
                 'Обществознание' : 4 }

family = ['Сергей 1976', 
          'Ольга 1979', 
          'Ульяна 2008', 
          'Матвей 2005', 
          'Николай 1954', 
          'Любовь 1957', 
          'Вера 1953 ', 
          'Александр 1950']

kiwa = 'Харчок'

def average_grade(school_grades):
    count = 0
    sum = 0
    for key in school_grades:
        count += 1
        sum += school_grades[key]
    return print('1) Средний балл по аттестату: ', sum/count)

def get_unique_names(family):
    unique_names = []
    for name_birth in family:
        name, birth = name_birth.split()
        if name not in unique_names:
            unique_names.append(name)
    return print('2) Уникальные имена среди своих родственников:', *unique_names)

def len_of_subjects(dict):
    sum = 0
    for k in dict:
        len_k = len(k) - k.count(" ")
        sum += len_k
    return print('3) Общая длина всех названий предметов:', sum)
    
def unique_letter(dict):
    subjects = []
    for k in dict:
        subjects.append(k)
    result_string = ' '.join(subjects)
    unique_letters = set(result_string.replace(" ", ""))
    print('4) Уникальные буквы в названиях предметов:',unique_letters)
    
def bin_kiwa(kiwa):
    bin_kiwa = ' '.join(format(ord(x), 'b') for x in kiwa)
    return print('5) Имя кивы в бинарном виде: ', bin_kiwa)

def sort_family(family):
    unique_names = []
    for name_birth in family:
        name, birth = name_birth.split()
        if name not in unique_names:
            unique_names.append(name)
    unique_names.sort(reverse=True)
    return print('6) Отсортированный по алфавиту в обратном порядке список родственников:', *unique_names)

def days(birthdate):
    birthdate_str = '28.02.2004'
    birthdate = datetime.strptime(birthdate_str, '%d.%m.%Y')
    today = datetime.now()
    days_since_birth = (today - birthdate).days
    return print('7) Количество дней с момента рождения:', days_since_birth)

def fifo(school_grades):
    queue = []
    print('8) FIFO очередь:\n')
    for subject, grade in school_grades.items():
        print(f'{subject}: {grade}')
    print()
    while True:
        index = input('Введите индекс (название) предмета (для остановки введите "Стоп"): ')
        if index == 'Стоп':
            break
        if index not in school_grades.keys():
            print('Предмета с таким индексом (названием) нет в словаре.')
            print()
        else:
            queue.append(index)
    print('Очередь предметов для добавления:')
    print()
    for item in queue:
        print(item)
    print()
    for item in queue:
        school_grades[item] = input(f'Введите оценку для предмета "{item}": ')
    print()
    print('Итоговые оценки:')
    for subject, grade in school_grades.items():
        print(f'{subject}: {grade}')
        
def actek_ruler():
    #номер правителя = (28+2**2+2004)%21 + 1 = 21 - Cipac
    actek = 'Cipak'
    print('9) Заменить родственника на ацтека')
    print()
    unique_names = []
    for name_birth in family:
        name, birth = name_birth.split()
        if name not in unique_names:
            unique_names.append(name)
    unique_names.sort(reverse=True)
    print(*unique_names)
    
    p = 0
    while p != 1:
        index = input('Введите индекс (имя) родственника (для остановки введите "Стоп"): ')
        if index == 'Стоп':
            p = 1
        elif index not in unique_names:
            print('Родственника с таким индексом (именем) нет в отсортированном списке\n')
        else:
            p = 1
            
    for i in range(len(unique_names)):
        if unique_names[i] == index and index!= 'Стоп':
            unique_names[i] = actek
    print()
    return print('Список родственников c ацтецким правителем:\n', *unique_names)

def function_generation():
    #number = len('Софронов Илья Сергеевич') * len ('Сергей Ольга Ульяна Матвей Николай Любовь Вера Александр') % 4 = 0
    print('\n11)')
    num = int(input('Введите число:'))
    seq = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            seq.append(i)
    return print('Аликвотная последовательность:', *seq)
    
average_grade(school_grades)
print()
get_unique_names(family)
print()
len_of_subjects(school_grades)
print()
unique_letter(school_grades)
print()
bin_kiwa(kiwa)
print()
sort_family(family)
print()
days(about_me)
print()
fifo(school_grades)
print()
actek_ruler()
function_generation()
