<<<<<<< HEAD
from numpy import copy

def converting_map_to_array( file_name ):
    
    with open( file_name , 'r') as f:
        MAP = [i.rstrip() for i in f]
    for i in range(len(MAP)):
        MAP[i]=list(MAP[i])
        
    return MAP


def write_map_in_file ( path, file_name ):
    
    with open( file_name , 'w') as f:   
        for i in Map_show:
            for j in i:
                f.write(f"{j}")
            f.write(f"\n")
    

def search_in_depth ( MAP , start , end ): # поиск в глубину
    
    visit_vertex = {} # словарь посещённых вершин сразу заносим начальную вершину 
    visit_vertex [ start ] = start # ключ- это соседняя вершина , значение - это вершина из которой пришли
    
    queue = [] # очередь (список) по принципу fifo для хранения шагов и последующего их вытаскивания для рассмотрения
    queue.append(start)
    
    visit_vertex = depths_get_visit_vertex ( MAP, queue, visit_vertex )  # получаем словарь посещенных вершин
    
    path = restore_path ( visit_vertex, None, start, end ) # восстанавливаем путь
        
    return path


def search_in_width ( MAP , start , end ): # поиск в ширину
    
    visit_vertex = {}
    visit_vertex [ start ] = start
    
    queue = [] # очередь (список) по принципу lifo для хранения шагов и последующего их вытаскивания для рассмотрения
    queue.append(start)
    
    visit_vertex = widths_get_visit_vertex ( MAP , queue , visit_vertex )  
    
    path = restore_path ( visit_vertex, None, start, end )
        
    return path


def depths_get_visit_vertex ( MAP, queue, visit_vertex): # получение координаты для поиска в глубину
    
    while len(queue) != 0 : # пока мы не прошли все вершины (иначе список будет пуст)
        
        basic_vertex = queue.pop() # вытаскиваем последние из добавленных элементов
            
        get_step = make_step( MAP, basic_vertex, visit_vertex, queue ) # делаем шаг
        queue = get_step[0]
        visit_vertex = get_step[1]
      
    return visit_vertex


def widths_get_visit_vertex( MAP, queue, visit_vertex ):
    
    while len(queue) != 0 :
        
        basic_vertex = queue.pop(0)
            
        get_step = make_step( MAP, basic_vertex, visit_vertex, queue )
        queue = get_step[0]
        visit_vertex = get_step[1]
        
    return visit_vertex
# для жадного .pop(0) , а для дейкстры .pop() ?



def make_step( MAP, basic_vertex, visit_vertex, queue ): # делаем шаг без оценки расстояния
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ] # координаты шагов для рассмотра смежных вершин
    
    for x_step, y_step in coords_one_step:
        
        x, y = basic_vertex[0] + x_step, basic_vertex[1] + y_step # координаты соседней вершины
            
        if 0 < x < len (MAP) and 0 < y < len (MAP[0]): # пока мы не вышли за границы массива
                
            if visit_vertex.get((x, y)) == None and MAP [x][y] != '#': 
                                                               # вершина ещё не посещенная и не является стеной
                visit_vertex[(x, y)] = (basic_vertex) # ключ соседняя вершина ,а значение - вершина из которой пришли
                
                queue.append((x, y)) # добавляем для следующего рассмотрения
               
                
    return queue , visit_vertex


def distance_calculation(end_coord, now_coord):
    # т.к. мы можем перемещаться в четыре стороны , то будем оценивать Манхэттенское расстояние
        return abs(end_coord[0] - now_coord[0]) + abs(end_coord[1] - now_coord[1])



def Grade_algoritm (MAP, start, end , choose_algoritm):
    
    queue = [(0, start)]
    visit_vertex ={}
    visit_vertex [ start ] = (0, start)
    
    visit_vertex =  Grade_get_visit_vertex ( MAP, queue, visit_vertex, end, start, choose_algoritm )
    path = restore_path (None, visit_vertex, start, end )
  
    return path


def Grade_get_visit_vertex ( MAP, queue, visit_vertex, end, start, choose_algoritm ):

    while queue:
        
        queue.sort(reverse = True)
        basic_vertex = queue.pop()[1]

        if basic_vertex == end:
            break
            
        if choose_algoritm == 0: 
            
            get_step = Dijkstra_make_step( MAP, basic_vertex, visit_vertex, queue, end)
            visit_vertex = get_step[0]
            queue = get_step[1]
            
        elif choose_algoritm == 1:
            
            get_step = Greedy_make_step( MAP, basic_vertex, visit_vertex, queue, start)
            visit_vertex = get_step[0]
            queue = get_step[1]
            
        else:  
            get_step = A_star_make_step( MAP, basic_vertex, visit_vertex, queue, start, end)
            visit_vertex = get_step[0]
            queue = get_step[1]
            
        
    return visit_vertex


def Dijkstra_make_step( MAP, basic_vertex, visit_vertex, queue, end): 
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ]
    
    for x_step, y_step in coords_one_step:
 
        x, y = basic_vertex[0] + x_step, basic_vertex[1] + y_step
        
        if 0 <= x < len (MAP) and 0 <= y < len (MAP) and MAP[x][y] != '#':
                
                new_cost = visit_vertex[basic_vertex][0] + 1
                
                if visit_vertex.get((x, y)) == None or new_cost < visit_vertex[(x, y)][0]:
                
                    grade = new_cost + distance_calculation(end, (x, y)) #  к стоимости добавляем расстояние от конца пути 
                
                    queue.append( (grade, (x, y)) )
                
                    visit_vertex[(x, y)] = (new_cost, basic_vertex)
           
    return visit_vertex, queue



def Greedy_make_step( MAP, basic_vertex, visit_vertex, queue, start): 
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ]
    
    for x_step, y_step in coords_one_step:
 
        x, y = basic_vertex[0] + x_step, basic_vertex[1] + y_step
        
        if 0 <= x < len (MAP) and 0 <= y < len (MAP) and MAP[x][y] != '#':
                
                new_cost = visit_vertex[basic_vertex][0] + 1
                
                if visit_vertex.get((x, y)) == None or new_cost < visit_vertex[(x, y)][0]:
                
                    grade = new_cost + distance_calculation(start, (x, y)) #  к стоимости добавляем расстояние от конца пути 
                
                    queue.append( (grade, (x, y)) )
                
                    visit_vertex[(x, y)] = (new_cost, basic_vertex)
           
    return visit_vertex, queue



def A_star_make_step( MAP, basic_vertex, visit_vertex, queue, start, end): 
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ]
    
    for x_step, y_step in coords_one_step:
 
        x, y = basic_vertex[0] + x_step, basic_vertex[1] + y_step
        
        if 0 <= x < len (MAP) and 0 <= y < len (MAP) and MAP[x][y] != '#':
                
                new_cost = visit_vertex[basic_vertex][0] + 1
                
                if visit_vertex.get((x, y)) == None or new_cost < visit_vertex[(x, y)][0]:
                    #  к стоимости добавляем расстояние от конца пути 
                    grade = new_cost + distance_calculation(start, (x, y)) + distance_calculation(end, (x, y)) 
                
                    queue.append( (grade, (x, y)) )
                
                    visit_vertex[(x, y)] = (new_cost, basic_vertex)
           
    return visit_vertex, queue


      
def restore_path ( visit_vertex, grades_visit_vertex , start , end ):
    
    path = [] 
    coord = end
    # путь восстанавливаем с конца  до начала
    # для методов в ширину и в глубину visit_vertex состоит из одномерных элементов ,a grades_visit_vertex из двумерных
    while coord != start:
        
        path.append(coord)
        
        if visit_vertex != None:   
            coord = visit_vertex[coord] # переприсваиваем ключ значением смежной вершины из словаря 
        else:                           # ключи не повтаряются , но разные ключи могут содержать одинаковые вершины
                                        # т.е. по одному ключу соответствует одна смежная вершина из которой мы пришли
            coord = grades_visit_vertex[coord][1]
                
    path.append(start)    
    path.reverse()
    
    return path


def Draw_Map ( MAP , path ,sign ):# отрисовка пути на карте
    
    Map_show = copy(MAP) 
    
    for coord in path:
        Map_show [coord[0],coord[1]] = sign
        
    return Map_show


def get_data (MAP):
    
    print('\n\t ВХОДНЫЕ ДАННЫЕ \n')
    x_start = int(input('Координаты аватара : '))
    y_start = int(input('Координаты аватара : '))

    x_key = int(input('Координаты ключа по х : '))
    y_key = int(input('Координаты ключа по у : '))

    MAP [x_key][y_key] = '*'
    
    start = (x_start , y_start)
    key = ( x_key , y_key )
    
    return start , key
 
    
# ПОЛУЧЕНИЕ НАЧАЛЬНЫХ ДАННЫХ

MAP =  converting_map_to_array( 'maze-for-u.txt' )

Data = get_data(MAP)
start = Data[0]
key = Data[1]

end_up = (1,1)
end_lower = (598,798)

if distance_calculation ( key , end_up) < distance_calculation ( key , end_lower ):
    end = end_up
    print('Ближайший выход - верхний.')
else:
    end = end_lower
    print('Ближайший выход - нижний.')

    
Dijkstra_algoritm = 0
Greedy_algoritm =1
A_star = 2



# ********** ПОИСК В ГЛУБИНУ ********** #

path_key = search_in_depth( MAP , start , key )
path_end = search_in_depth( MAP , key , end )

# запишем путь от старта до ключа алгоритмом поиска в глубину
Map_show = Draw_Map ( MAP , path_key , '.' )

print('\n\t********** ПОИСК В ГЛУБИНУ **********\n')
print('\nКолличество шагов от старта до ключа : ', len(path_key) )
print('Колличество шагов от старта до выхода : ', len(path_end) + len(path_key) )

# ********** ПОИСК В ШИРИНУ ********** #

path_key = search_in_width ( MAP , start , key )
path_end = search_in_width ( MAP , key, end )

print('\n\t********** ПОИСК В ШИРИНУ **********\n') 
print('\nКолличество шагов от старта до ключа : ', len(path_key) )
print('Колличество шагов от старта до выхода : ', len(path_end) + len(path_key) )

# ********** Дейкстра ********** #

path_key = Grade_algoritm (MAP, start, key, Dijkstra_algoritm)
path_end = Grade_algoritm (MAP, key, end, Dijkstra_algoritm)

print('\n\t********** Дейкстра **********\n') 
print('\nКолличество шагов от старта до ключа : ', len(path_key) )
print('Колличество шагов от старта до выхода : ', len(path_end) + len(path_key) )

# ********** Жадный алгоритм ********** #

path_key = Grade_algoritm (MAP, start, key, Greedy_algoritm)
path_end = Grade_algoritm (MAP, key, end, Greedy_algoritm)

print('\n\t********** Жадный алгоритм **********\n') 
print('\nКолличество шагов от старта до ключа : ', len(path_key) )
print('Колличество шагов от старта до выхода : ', len(path_end) + len(path_key) )

# ********** A* ********** #

path_key = Grade_algoritm (MAP, start, key, A_star)
path_end = Grade_algoritm (MAP, key, end, A_star)

# запишем путь от ключа до выхода алгоритмом  A*
Map_show = Draw_Map ( Map_show , path_end , ',' )
write_map_in_file ( Map_show , 'maze-for-me-done.txt')

print('\n\t********** A* **********\n') 
print('\nКолличество шагов от старта до ключа : ', len(path_key) )
print('Колличество шагов от старта до выхода : ', len(path_end) + len(path_key) )
print('\n Путь хранится в текстовом файле maze-for-me-done.txt ,\n где путь от старта до ключа реализован методом поиска в глубину, а путь от ключа до выхода алгоритмом А*')

