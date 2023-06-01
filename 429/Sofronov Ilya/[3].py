from numpy import copy

def maze_to_list(file_name):                    # Принимает текстовый файл лабиринта, возращает лист лабиринта
    
    with open(file_name, 'r') as file:
        maze_list = [i.rstrip() for i in file]
    for i in range(len(maze_list)):
        maze_list[i] = list(maze_list[i])
        
    return maze_list


def save_maze_as(pathway, file_name):           # Принимает пройденный лабиринт и сохраняет в файл
    
    with open(file_name, 'w') as file:   
        for i in pathway:
            for j in i:
                file.write(f"{j}")
            file.write(f"\n")   


def drawPathway(maze_list, path, symbol):      # Принимает лабиринт, путь и символ. Возращает отрисованный путь
    
    Map_show = copy(maze_list) 
    
    for coord in path:
        Map_show [coord[0],coord[1]] = symbol
        
    return Map_show


def get_data(maze_list):                        # Принимает лабиринт. Возвращает координаты аватара и ключа
    
    print('\n Введите данные: \n')
    x_start = int(input('Координаты аватара по x: '))
    y_start = int(input('Координаты аватара по y: '))

    x_key = int(input('Координаты ключа по х : '))
    y_key = int(input('Координаты ключа по у : '))

    maze_list[x_key][y_key] = '*'
    
    avatar = (x_start, y_start)
    key = (x_key, y_key)
    
    return avatar, key


def manhattan_distance(end_point, now_point):   # Принимает нынешнюю и конечную точки, возвращает общее кол-во клеток между ними, без учёта стенок
        
        return abs(end_point[0] - now_point[0]) + abs(now_point[1] - now_point[1])


def Kant_Alg(maze_list, avatar, end, algoritm):  # Сортирует вершины по уровню  (алгоритм Канта)                  
    
    #Запись вида:
    # [расстояние от нач.точки до данной вершины , (координаты данной вершины)]
    # queue - очередь. 0 - начальная точка 

    queue = [(0, avatar)]    
    visit_vertex ={}                        # словарь для хранения числа входных степеней каждой вершины в графе
    visit_vertex[avatar] = (0, avatar)      # начальная точка добавляется с расстоянием 0 и собственными координатами
    visit_vertex =  Kant_Alg_visited(maze_list, queue, visit_vertex, end, avatar, algoritm)
    path = restore_path(None, visit_vertex, avatar, end)
  
    return path


def Kant_Alg_visited(maze_list, queue, visit_vertex, end, avatar, algoritm):    # Обрабатывает очередь, извлекая из нее посещенные вершины, 
                                                                                #обновляет словарь для каждой вершины и создает список соседей
    while queue:

        queue.sort(reverse = True)     
        now_vertex = queue.pop()[1]     # Координаты текущей клетки

        if now_vertex == end:           # Если дошли до конца
            break
            
        if algoritm == 0:               # Если пользуемся алгоритмом Дейкстры
            
            get_step = Dijkstra_make_step(maze_list, now_vertex, visit_vertex, queue, end)
            visit_vertex = get_step[0]
            queue = get_step[1]
            
        else: 
             
            get_step = A_star_make_step(maze_list, now_vertex, visit_vertex, queue, avatar, end)
            visit_vertex = get_step[0]
            queue = get_step[1]

    return visit_vertex


def Dijkstra_make_step(maze_list, now_vertex, visit_vertex, queue, end): # Добавляет все доступные соседние клетки в очередь с приоритетом, которые можно посетить из данной клетки
    
    coords_one_step = [(0, -1),(1, 0),(0, 1),(-1, 0)]           # Относительные координаты соседних клеток (↓, →, ↑, ←)
    
    for x_step, y_step in coords_one_step:                      # Проходим по всем направлениям
 
        x, y = now_vertex[0] + x_step, now_vertex[1] + y_step                               # Координаты соседней клетки
        
        if 0 <= x < len(maze_list) and 0 <= y < len(maze_list) and maze_list[x][y] != '#':  # Вообще находится ли текущая клетка внутри лабиринта и можно ли ее переместить
                
                new_cost = visit_vertex[now_vertex][0] + 1      # Новая стоймость
                
                if visit_vertex.get((x, y)) == None or new_cost < visit_vertex[(x, y)][0]:
                
                    grade = new_cost + manhattan_distance(end, (x, y))                      #  К новой стоимости добавляем расстояние от конца пути. Это будет итоговая стоймость
                
                    queue.append( (grade, (x, y)) )             # Мы добавим каждую клетку только один раз в очередь

                    visit_vertex[(x, y)] = (new_cost, now_vertex)                           # Обновленный словарь
           
    return visit_vertex, queue                                  # Обновленный словарь и очередь


def A_star_make_step(maze_list, now_vertex, visit_vertex, queue, avatar, end): 
    
    coords_one_step = [(0, -1),(1, 0),(0, 1),(-1, 0)] 
    
    for x_step, y_step in coords_one_step:
 
        x, y = now_vertex[0] + x_step, now_vertex[1] + y_step
        
        if 0 <= x < len (maze_list) and 0 <= y < len (maze_list) and maze_list[x][y] != '#':
                
                new_cost = visit_vertex[now_vertex][0] + 1
                
                if visit_vertex.get((x, y)) == None or new_cost < visit_vertex[(x, y)][0]:
                    
                    grade = new_cost + manhattan_distance(avatar, (x, y)) + manhattan_distance(end, (x, y)) #  Добавляем расстояние от конца пути
                
                    queue.append( (grade, (x, y)) )
                
                    visit_vertex[(x, y)] = (new_cost, now_vertex)
           
    return visit_vertex, queue      # Обновленный словарь и очередь
      

def restore_path(visit_vertex, grades_visit_vertex, avatar , end):
    # Восстанавливает путь от конечной точки до начальной, используя значения из словаря 

    path = []               # Записываем координаты пути
    location = end             
    while location != avatar:  # От конечной до начальной точки перебираем координаты
        
        path.append(location)  # Добавляем текущую координату в список path
        
        if visit_vertex != None:            #Значит, двигаемся вдоль Дейкстры         
            
            location = visit_vertex[location]             #Записываем координату предыдущего шага

        else:                               #Иначе, двигаемся вдоль А*                                           
            
            location = grades_visit_vertex[location][1]   #Записываем координату предыдущего шага с помощью кортежа
                
    path.append(avatar)    
    path.reverse()
    
    return path
 
    
# Данные

maze_list =  maze_to_list( 'C:/Users/User/Desktop/papka/[3]/maze-for-u.txt' )

data = get_data(maze_list)
avatar = data[0]
key = data[1]
print('Введённые координаты аватара и ключа: ',data)

upper_end = (1,2)
print('Координаты верхнего выхода:', upper_end)
lower_end = (600,798)
print('Координаты нижнего выхода:', lower_end)

if manhattan_distance(key, upper_end) < manhattan_distance(key, lower_end): # Так как выхода может быть два, выбираем ближайший
    end = upper_end
    print('Ближайший выход из алгоритма - верхний.')
else:
    end = lower_end 
    print('Ближайший выход из алгоритма - нижний.')

    
Dijkstra = 0
A_star = 1

path_key = Kant_Alg(maze_list, avatar, key, Dijkstra)

def getStar(pathway, avatar):      # Принимает лабиринт, путь и символ. Возращает отрисованный путь
  
    Map_show = copy(pathway) 
    Map_show[avatar[0],avatar[1]] = '*'
        
    return Map_show

pathway = drawPathway(maze_list, path_key, '.' )
  

print('\nРаботает Алгоритм Дейкстры...\n') 
print('\nКоличество шагов от аватара до ключа : ', len(path_key))

path_end = Kant_Alg(maze_list, key, end, A_star)

pathway = drawPathway(pathway, path_end, ',' )
pathway = getStar(pathway, avatar)
save_maze_as(pathway, 'maze-for-me-done.txt')


print('\nРаботает А*...\n') 
print('Количество шагов от ключа до выхода : ', len(path_end) + len(path_key))
print('\n Файл сохранен как `maze-for-me-done.txt!`\n')

