import random

#список целых чисел от 0 до 999999;
list_of_int_numbers = list(range(0, 100000))

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
list_of_random_numbers = []
for e in range(99999):
    list_of_random_numbers.append(random.uniform(-1, 1))

#42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month 
#(можно случайных, можно равномерно распределённых), сортировать по модулю числа;
numbers_compl=[]
while len(numbers_compl)<42000:
    coef=random.uniform(0,3/4)
    compl_numb=complex(coef,coef)
    numbers_compl.append(compl_numb)

#сортировка пузырьком

#Указатель на отсортированную часть
sorted_index = len(list_of_int_numbers)
while True:
    #Счётчик обменов
    number_of_swap = 0
    #Перебор индексов не отсортированной части
    for i in range(0, sorted_index-1):
        if list_of_int_numbers[i] > list_of_int_numbers[i+1]:
            list_of_int_numbers,list_of_int_numbers[i+1] = list_of_int_numbers[i+1], list_of_int_numbers[i]
            number_of_swap += 1
    sorted_index -= 1
    #Если обменов не было заканчиваем
    if number_of_swap == 0:
        break
print(list_of_int_numbers)

#сортировка расчёской
step = int(len(list_of_random_numbers)/1.247)
swap = 1
while True:
    swap = 0
    i = 0
    while i + step < len(list_of_random_numbers):
        if list_of_random_numbers[i] > list_of_random_numbers[i+step]:
            list_of_random_numbers[i], list_of_random_numbers[i+step] = list_of_random_numbers[i+step], list_of_random_numbers[i]
            swap += 1
        i = i + 1
    if (step == 1 and swap == 0):
        break
    step = int(step/1.247)
    if step < 1:
        step = 1
print(list_of_random_numbers)

#сортировка "Гномья"
def gnome_sort_compl(arr):
    n = len(arr)
    i = 1
    while i < n:
        if (arr[i-1].real**2+arr[i-1].imag**2)**(1/2) <= (arr[i].real**2+arr[i].imag**2)**(1/2):
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            if i > 1:
                i -= 1
    return arr
#Очень долго компиллируется, запускать на свой страх и риск
#sort_gnom= gnome_sort_compl(numbers_compl)
#print (sort_gnom)
