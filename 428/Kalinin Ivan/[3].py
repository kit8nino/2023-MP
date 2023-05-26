
import heapq
import random

# чтение из файла
def read_file(file_name):
    file = open(file_name)
    double_mas = []

    for row in file:
        strok=[]
        for stolb in row:
            if stolb == "\n":
                continue
            strok.append(stolb)
        double_mas.append(strok)
    return double_mas

# запись в файл
def write_file(file_name, mas):
    f = open(file_name,'w') 
    for link in mas:
        for dink in link:
            f.write(str(dink))
        f.write("\n")
    f.close()
    
# функции для проверки корректности координат (чтобы были не в стене)

def check(one):
    if MAP[one[0]][one[1]] == "#":
        return True
    
    else:
        return False

def check_coord(one):
    while check(one):
        x0=one[0]
        x1=one[1]
        if x1 != len(MAP[0]):
            x1+=1
            one= (x0, x1)
        else :
                x0+=1
                one= (x0, x1)
    return(one)

# функция для построения маршрута

def set_coord(mas, shagi1, shagi2, key):
    x0=key[0]
    y0=key[1]
 
    for coord1 in shagi1:
        x1=coord1[0]
        y1=coord1[1]
        mas[x1][y1] = "."
    
    for coord2 in shagi2:
         x2=coord2[0]
         y2=coord2[1]
         mas[x2][y2] = ","
    mas[x0][y0] = "*"
    return mas

# поиск в глубину

def dept_search(mas, start, finish):
    steck = [(start, [start])]
    visit = set()
   
    while steck:
        (point), summ = steck.pop()
        x0 = point[0]
        y0=point[1]
        if point == finish:
            print("Длинна Маршрута до ключа == ", len(summ))
            return summ
        if point in visit:
            continue
        visit.add(point)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            y, x = y0 + dy, x0 + dx
            new_point = (x, y)
            if 0 <= y < len(mas) and 0 <= x < len(mas[0]) and mas[x][y] != "#" and (x, y) not in visit:
                steck.append((new_point, summ + [new_point]))
    return None

# А* поиск

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_search(mas, start, finish, max_shagov):
    stack = [(0, start, [start])]
    visit = set()
    while stack:
        f, point, summ = heapq.heappop(stack)
        x0 = point[0]
        y0 = point[1]
        if point == finish:
            print("Длинна Маршрута от ключа до выхода == ", len(summ))
            return summ
        if point in visit:
            continue
        visit.add(point)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = x0 + dx, y0 + dy
            new_point = (x, y)
            if 0 <= x < len(mas) and 0 <= y < len(mas[0]) and mas[x][y] != "#" and (x, y) not in visit:
                new_summ = summ + [new_point]
                g = len(new_summ)
                h = heuristic(new_point, finish)
                f = g + h
                if len(stack) < max_shagov:
                    heapq.heappush(stack, (f, new_point, new_summ))
                else:
                    heapq.heappushpop(stack, (f, new_point, new_summ))
                    
    return None

# читаем файл 

file_name = 'maze-for-u.txt'
MAP = read_file(file_name)

# Задаем начальные координаты

avatar = (int(len(MAP[0])/2), int(len(MAP)/2)) #начинаем из середины лабиринта
key = (random.randint(1, len(MAP)-1), random.randint(1, len(MAP[0])-1)) #ключ выбираем случайно
exit_maze = (len(MAP)-1, len(MAP[0])-2) #выход устанавливаем на нижней стенке

# Проверяем, чтобы они были не в стене

avatar = check_coord(avatar)
key = check_coord(key)
print("Старт ==", avatar)
print("Ключ ==", key)
print("Выход ==", exit_maze, "\n")

path1 = dept_search(MAP, avatar, key)
path2 = A_search(MAP, key, exit_maze, 10000)
if path1 != None and path2 != None:
    set_coord(MAP, path1, path2, key)
    print("Общий маршрут -->", len(path1)+len(path2))
elif path1 == None:
    print("От входа до ключа не добраться :(")
elif path2 == None:
    print("Выхода нет, скоро рассвет...")


# Записываем пройденный маршрут в файл

file_name1 = 'mase-for-me-done.txt'
write_file(file_name1, MAP)
