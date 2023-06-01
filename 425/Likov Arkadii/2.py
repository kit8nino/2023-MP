import random
import cmath
import numpy as np
import re
import codecs

q=[]
for i in range(1000000):
    q.append(i)
random.shuffle(q)
print('Исходный список:\n',q,'\n')

w=len(q)
while w>0:
    e=q[0]
    for i in range(w):
        if q[i]<e:
            e=q[i]
    q.remove(e)
    q.append(e)
    w-=1
print('Отсортированный список:\n',q,'\n')


q=np.random.uniform(-1,1,(1000000))
print('Исходный список:\n',q,'\n')
w=len(q)
i=1
while i<w:
    if q[i-1]<=q[i]:
        i+=1
    else:
        a=q[i]
        q[i]=q[i-1]
        q[i-1]=a
        i-=1
        if i==0:
            i=1
print('Отсортированный список:\n',q,'\n')

R=12.5
e=(R**(2)/2)**(0.5)
print('Модуль комплексного числа R<=',e,'\n')
rt=[]
for i in range(42000):
    Re=np.random.uniform(-e,e)
    Im=np.random.uniform(-e,e)
    rt.append(complex(Re,Im))
w=len(rt)
s = 0
end = w - 1

while s <= end:

    for i in range(s,end, 1):

        if abs(rt[i]) > abs(rt[i + 1]):
            a=rt[i]
            rt[i] =rt[i+1]
            rt[i+1] =a
    end -= 1 
    for i in range(end, s, -1):
 
        if abs(rt[i - 1]) > abs(rt[i]):
            a=rt[i]
            rt[i] = rt[i-1]
            rt[i-1] =a
    s += 1 
print('Отсортированный список:\n',rt,'\n')




file= codecs.open( "C:/1/tress.txt", "r", "utf_8_sig" )

f=file.read()

l= re.sub(r'[^\w\s]','', f)

t=l.split()

length = len(t) 
for i in range(1, len(t)):
        k = len(t[i])
        t=t[i]
        j = i-1
        
        while j >=0 and k < len(t[j]) :
            
            t[j+1] = t[j]
            
            j -= 1
       
        t[j+1] = t 
print(t)
file.close()