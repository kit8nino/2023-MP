import random
import re
import codecs
# Исходные данные

List1 = list(range(10))
random.shuffle(List1)
List2 = [random.uniform(-1, 1) for _ in range(9)]
birth_day = 4
birth_month = 4
r = birth_day / birth_month
List3 = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(12)]
sorted_List3 = sorted(List3, key=lambda x: abs(x))


book = 'book.txt'
with open(book, 'r', encoding='utf-8') as file:
    text = file.read()
    List4 = re.findall(r'\b[A-Za-z]+\b', text)




# 8)Сортировка выбором. O(n^2)
def selection_sort(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# 2)Сортировка пузырьком. O(n^2)
def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

# 4) Сортировка вставкой.
def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(1, len(nums)):
            if abs(nums[j])<abs(nums[j-1]):
                (nums[j]),(nums[j-1])=(nums[j-1]),(nums[j])
            else:
                break
        
                

# 10) Быстрая сортировка. O(nlogn) или O(n^2)
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    elem = nums[0]
    left = list(filter(lambda x: x<elem, nums))
    center = [i for i in nums if i == elem]
    right = list(filter(lambda x: x>elem, nums))

    return quick_sort(left) + center + quick_sort(right)





# Проверка
selection_sort(List1)
print(List1)
bubble_sort(List2)  
print(List2)
insertion_sort(List3)
print(List3)
print(quick_sort(List4))

 



