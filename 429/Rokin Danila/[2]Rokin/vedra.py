'''Сортровка ведер для комплексных чисел'''
'''Сначала печатает массив комплексных чисел, потом отсортированный массив,
потом массив модулей'''

import random as rnd
import numpy as np
'''
a=[]
for i in range(4):
    a.append(rnd.randint(1,18))
print(a)
Сортировки 13,7,11,14
'''

random_array=[]
Numbers=42000

dataBir=9/7
random_array = np.sqrt(np.random.uniform(0, dataBir,Numbers)) * np.exp(1.j * np.random.uniform(0, 2 * np.pi, Numbers))
print(random_array,len(random_array))


###################################################

'''Сортировка ведрами'''

Range=10
#int(input("Введите диапозон ведер:"))
Kolvo_veder = round(Numbers / Range)

'''Создание ведер'''

Masiv_veder=[]
for i in range(Kolvo_veder):
   Masiv_veder.append([])


'''Заполнение ведер'''

for i in range(len(random_array)):
    index_vedra = int(abs(random_array[i])*10000 / (Range+1))
    Masiv_veder[index_vedra].append(random_array[i])
    if len(Masiv_veder[index_vedra])>1:
        for j in range(len(Masiv_veder[index_vedra])-1,-1,-1):
            for k in range(j-1,-1,-1):
                if abs(Masiv_veder[index_vedra][j]) < abs(Masiv_veder[index_vedra][k]):
                    Masiv_veder[index_vedra][j],Masiv_veder[index_vedra][k]=Masiv_veder[index_vedra][k],Masiv_veder[index_vedra][j]                   
                else:
                    continue
arrSorted=sum(Masiv_veder,[])
absMassiva=[abs(arrSorted[i]) for i in range(len(arrSorted))]
print(arrSorted,len(arrSorted),absMassiva)
