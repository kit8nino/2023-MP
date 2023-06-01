import random


birthday = int(input("Введите день вашего рождения: "))
birthmonth = int(input("Введите месяц вашего рождения: "))

# Создание списков целых и вещественных чисел
int_list = list(range(1000))
float_list = [random.uniform(-1, 1) for i in range(50000)]

# Создание списка точек комплексной плоскости
complex_list = []
for i in range(42000):
  x = random.uniform(-birthday/birthmonth, birthday/birthmonth)
  y = random.uniform(-birthday/birthmonth, birthday/birthmonth)
  complex_list.append(complex(x,y))

# Создание списка слов из книги
with open("Мастер и Маргарита.txt", "r") as f:
  text = f.read()
  word_list = text.split()

# Сортировка списков разными алгоритмами

# Сортировка пузырьком целых чисел
def bubble_sort(int_list):
  n = len(int_list)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if int_list[j] > int_list[j+1]:
        int_list[j], int_list[j+1] = int_list[j+1], int_list[j]

bubble_sort(int_list)

# Сортировка Шелла вещественных чисел
def shell_sort(float_list):
  n = len(float_list)
  gap = n//2
  while gap > 0:
    for i in range(gap,n):
      temp = float_list[i]
      j = i
      while j >= gap and float_list[j-gap] > temp:
        float_list[j] = float_list[j-gap]
        j -= gap
      float_list[j] = temp
    gap //= 2

shell_sort(float_list)

# Сортировка деревом точек комплексной плоскости по модулю
def tree_sort(complex_list):
  sorted_list = []
  for c in complex_list:
    added = False
    if not sorted_list:
      sorted_list.append(c)
      added = True
    else:
      insert_node(c, sorted_list)
      added = True

def insert_node(c, tree_list):
  if abs(c) < abs(tree_list[0]):
    tree_list.insert(0, c)
    return
  elif abs(c) > abs(tree_list[-1]):
    tree_list.append(c)
    return
  else:
    for i in range(len(tree_list)-1):
      if abs(c) > abs(tree_list[i]) and abs(c) < abs(tree_list[i+1]):
        tree_list.insert(i+1, c)
        return

tree_sort(complex_list)

# Сортировка слиянием слов из книги
def merge_sort(word_list):
  if len(word_list) > 1:
    mid = len(word_list)//2
    left_half = word_list[:mid]
    right_half = word_list[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        word_list[k] = left_half[i]
        i += 1
      else:
        word_list[k] = right_half[j]
        j += 1
      k += 1

    while i < len(left_half):
      word_list[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      word_list[k] = right_half[j]
      j += 1
      k += 1

merge_sort(word_list)

# Вывод отсортированных списков
print("Отсортированный список целых чисел: ", int_list)
print("Отсортированный список вещественных чисел: ", float_list)
print("Отсортированный список точек комплексной плоскости: ", complex_list)
print("Отсортированный список слов: ", word_list)