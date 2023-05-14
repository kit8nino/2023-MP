import random as rnd

def selectionsort(list_num):
    current = 0
    while current != len(list_num):
        for i in range (current, len(list_num)):
            minimum = list_num[i]
            ind  = i
            for j in range (i+1,len(list_num)):
                if list_num[j]<minimum:
                    minimum = list_num[j]
                    ind = j
                    list_num[i], list_num[ind] = list_num[ind], list_num[i]
        current += 1
    return (list_num)

def LSD(list_num):
    max_digit = max([len(str(i)) for i in list_num])
    interim = [[] for i in range (10)]
    for dig in range (max_digit):
        for num in list_num:
            digit = (num//10**dig)%10
            interim[digit].append(num)
        list_num = [num for digs in interim for num in digs]
        interim = [[] for i in range (10)]
    return (list_num)

def countingsort(list_num):
    max_num = max(list_num)
    count = 0
    interim = [0]*(max_num+1)
    for i in range (len(list_num)):
        interim[list_num[i]] += 1 
    for num in range(max_num):
        while interim[num]>0:
            list_num[count] = num
            count += 1
            interim[num] -= 1
    return (list_num)

def maxheap(list_num, size, root_ind):
    max_el = root_ind
    left_branch = (2*root_ind)+1
    right_branch = (2*root_ind)+2
    if left_branch<size and list_num[left_branch]>list_num[max_el]:
        max_el = left_branch
    if right_branch<size and list_num[right_branch]>list_num[max_el]:
        max_el = right_branch
    if max_el!=root_ind:
        list_num[root_ind], list_num[max_el] = list_num[max_el], list_num[root_ind]
        maxheap(list_num, size, max_el)
        
def heapsor(list_num):
    for count in range (len(list_num), -1, -1):
        maxheap(list_num, len(list_num), count)
    for i in range (len(list_num)-1, 0, -1):
        list_num[i], list_num[0] = list_num[0], list_num[i]
        maxheap(list_num, i, 0)
    return (list_num)        

list_of_int = [i for i in range(1000000)]
rnd.shuffle(list_of_int)
list_of_float = [rnd.uniform(-1,1) for i in range (99999)]
list_of_complex = [complex(rnd.randint(0,100),rnd.randint(0,100)) for i in range (42000)]
list_of_abs = [abs(i) for i in list_of_complex]
list_of_str = []
with open("text_for_2.txt") as file:
    list_of_str = file.read().split()
list_of_bin = [int(bin(int.from_bytes(i.encode(), 'big')), 2) for i in list_of_str]
print ("Отсортированный список целых чисел:", countingsort(list_of_int))
print ("Отсортированный список вещественных чисел:", selectionsort(list_of_float))
print ("Отсортированный список слов (по иx представлению в численном виде):", [i.to_bytes((i.bit_length() + 7) // 8, 'big').decode() for i in LSD(list_of_bin)])
print ("Отсортированный список модулей комплексных чисел:", heapsor(list_of_abs))

