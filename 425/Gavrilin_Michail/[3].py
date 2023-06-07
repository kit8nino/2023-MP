import heapq
import random
import numpy as np
import scipy.integrate
import matplotlib.pyplot as py
import random as r
import matplotlib.pyplot as plt 
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def exist(self):
        return len(self.elements) != 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    def remove(self, n):                                       
        lowest_priority = self.elements[0][0]
        i = 0
        while i < n and self.exist() and self.elements[0][0] == lowest_priority:
            heapq.heappop(self.elements)
            i += 1
    def leng(self):
        return len(self.elements)
def evristic(point_1,point_2,type_search):
    if type_search == "A":    
        (x1,y1) = point_1 
        (x2,y2) = point_2 
        return abs(x2 - x1) + abs(y2 - y1)
    elif type_search == "D": 
        return 0
    else:
        print("Error 1")
class Graph_grid:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = [] 
        self.weights = {}   
        
    def inside(self, point):        
        (x, y) = point
        return 0 <= x < self.width and 0 <= y < self.height
    
    def reachable(self, point):     
        return point not in self.walls
    
    def draw_grid(self):            
        for i in range(self.height):
            print("")
            for j in range(self.width):
                if(i,j) in self.walls:
                    print("#",end='')
                else:
                    print(". ",end='')
            
    def neighbors(self, point):        
        (x, y) = point
        results = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        results = filter(self.inside, results)
        results = filter(self.reachable, results)
        
        return results
    
    def cost(self, cur_point, point):     
        return 1                            
def A_search(graph, start, finish, upper_limit,upper_limit_front,type_search):
    
    search_bound  = PriorityQueue()
    search_bound.put(start,0)
    
    point_log ={}
    point_log[start]=None
    
    costs={}    
    costs[start] = 0 
    
    counter = 0
    
    while search_bound.exist():
        
        counter +=1
        current_point = search_bound.get()
        
        if counter % 500 ==0:
            print("iter: ",counter)
        
        if search_bound.leng()>upper_limit_front:
            n=abs(upper_limit_front-search_bound.leng())
            search_bound.remove(n)
            
        if counter > upper_limit:
            print("over the limit")
            return get_path_part(point_log,start,current_point)                        
        
        if current_point == finish:
            if type_search == "A":     
                print("A* completed -> path found")
            elif type_search == "D":
                print("Dijkstra completed -> path found")
            else:
                print("Error 3 ")
            break
        
        for point in graph.neighbors(current_point):
            
                neighbour_cost = costs[current_point]+graph.cost(current_point, point)
           
        if point not in costs or neighbour_cost < costs[point]:
               
            costs[point] = neighbour_cost
        point_log[point] = current_point
               
        priority = neighbour_cost + evristic(point,finish,type_search)
        search_bound.put(point,priority)
               
    return get_path(point_log,start,finish)
def get_path(log, start, finish, ):
    
    current_point = finish
    path = [current_point]
    
    while current_point != start:
        
        current_point = log[current_point]
        path.append(current_point)
        
    path.append(start)
    path.reverse() 
    
    return path

def get_path_part(log, start, last_point):
    
    current_point = last_point
    path = [current_point]
    
    while current_point != start:
        
        current_point = log[current_point]
        path.append(current_point)
        
    path.append(start)
    path.reverse() 
    
    return path
def write_path(height,width,start,key,finish,walls,path_k,path_e,output_filename):
    
    print ("start of file processing ", output_filename)
    counter = 0
    
    
    with open(output_filename, 'w') as f:
        for i in range(height):
            counter+=1
            if counter %10 ==0:
                print("created line ->", counter)
            
            for j in range(width):
                point =(j,i)
                if point in walls:
                    f.write('#')
                elif point in path_k and point != start and point != finish and point != key:                 
                        f.write('.')
                elif point in path_e and point != start and point != finish and point != key:        
                        f.write(',')            
                elif point == start:
                    f.write('S')
                elif point == key:                    
                    f.write('*')
                elif point == finish:
                    f.write('E')
                else:
                    f.write(' ')
            f.write('\n')
                   


def get_key(walls, width, height):
    upper_limit = 100
    counter =0
    while counter < upper_limit+1:  
        counter +=1
        x= random.randint(1,width-1)
        y= random.randint(1,height-1)
        key=(x,y)
        if key not in walls:
            return key 
        if counter >= upper_limit:
            print("insert key position -> ")
            print("x = ")
            x=int(input())
            print("y = ")
            y=int(input())
            key=(x,y)
            return key 
start_v = (1,0)         



finish_v = (798,599)      


upper_limit_v = 100000      
upper_limit_front = 100000  
 

input_filename="maze-for-u.txt"     
output_filename="maze-for-me-done.txt"
 
with open(input_filename, 'r') as f:
    lines = f.readlines()
    
width = max(len(line) for line in lines)-1 

height = len(lines)

walls_f = []

for j in range(height):
    for i in range(width):
        if lines[j][i] == '#':
            walls_f.append((i, j))
        
print("input file",input_filename)
print('maze width:', width)
print('maze height:', height)


maze = Graph_grid(width, height)

maze.walls = walls_f

maze.weights = {}  

print("created by struct graf")

key = get_key(maze.walls, width,height)

print("key coord -> ",key)
print("start processing by key")
type_search ="D"
path_to_key = A_search(maze,start_v,key,upper_limit_v,upper_limit_front, type_search)

print("exit coord -> ",finish_v)
print("processing key to exit ->")
type_search ="A"
path_to_exit = A_search(maze,key,finish_v,upper_limit_v,upper_limit_front, type_search)
 
write_path(height,width,start_v,key,finish_v,walls_f,path_to_key,path_to_exit,output_filename)

print("script done")

