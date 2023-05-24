import datetime as dt
import queue

info = ('Годяев','Владимир','Владиславович',10,8,2003)

certificate ={
    'algebra': 4,
    'geometry': 4,
    'russian lanquage':4,
    'literature':4, #teacher bad, don't like
    'english language':5,
    'physics':5,
    'chemistry':4,
    'biology':5,
    'russian history':4,
    'general history':4,
    'informatics':5,
    'PE':5,
    'social studies':5,
    'geography':5    
    }

Vin_Disel = ['Tatiana 1971', 'Vladislav 1961', 'Alexsander 1991','Valya 1947', 'Alexsander 1943' ,'Sergay 2001', 'Denis 2000', 'Alexsey 1972', 'Luba 1982', 'Raisa 1932','Vladimir 1933']

Kiwa = 'Tremble'

#1 - Avarage Mark
Av_Mark=sum(certificate.values())/len(certificate)
print('№1) Avarage mark is: ',Av_Mark)

#2 Unique Names
Names=[]
for i in range(0,len(Vin_Disel)):
    word = "".join(" " if el.isdigit() else el for el in Vin_Disel[i]).split()
    word=word[0] # Не нашел другого способа избавиться от годов в элементах
    Names.append(word)    
Unique_names = list(set(Names))
print('№2) List of unique names: ',Unique_names)

#3 -Sum of lengths of all the classes names
Keys = list(certificate.keys())
Len_sum = 0
for i in range(0,len(Keys)):
    Len_sum+=len(Keys[i])
print('№3) Len of all the classes names combined:',Len_sum)

#4 Unique letters
Ul =set()
for i in range(0,len(Keys)):
    Ul=Ul|set(Keys[i])
print('№4) Unique letters:',Ul)

#5 Kiwa in robot
Mecha_Kiwa= ' '.join(format(L, 'b') for L in bytearray(Kiwa, "utf-8"))
print('№5) Kiwa in robot: ', Mecha_Kiwa)

#6 Sort Names
Sorted_Names = sorted(Names,reverse=True)
print('№6) Sorted names:',Sorted_Names)

#7 Days from birthday
Bd = dt.date(info[5],info[4],info[3])
today = dt.date.today()
print('№7) I was born',(today-Bd).days,'days ago')

#8 FIFA
Q = queue.Queue()
print('№8) To stop print word "End"')
i=input()
while i!='End':
    Q.put(i)
    i=input()
while not Q.empty():
    print(Q.get(),end = ",")
    
#9 Imposter
print("\n №9) Name number is: " ,(info[3] + info[4]**2 + info[5]) % 21 + 1)
print("Write any Number")
i = int(input())%21
Names[i]='Cecetzin'
print('№9 One of this is not like the others:',Names)

#10 Node
Years=[]
for i in range(0,len(Vin_Disel)):
    Num = "".join(Y if Y.isdigit() else " " for Y in Vin_Disel[i]).split()
    Num=int(Num[0])
    Years.append(Num)
    
Spicok={}
for i in range(0,len(Names)):    
    Spicok[Names[i]] = Years[i]
    Sorted_Spicok=dict(sorted(Spicok.items(),key=lambda item: item[1]))
print("№10): ",Sorted_Spicok)

#11 Tribonachi
print("№11) Generator number: ", len(info)*len(Vin_Disel)%4)
print("№11) How many tribonachi numbers would you like to be generated?")
I=int(input())
def Tribonachi(i):
    fst=0
    scnd=0
    trd=1
    N=[]
    for j in range (0,i):
        n=fst+scnd+trd
        fst=scnd
        scnd=trd
        trd=n
        N.append(n)
    return(N)
print("№11: ", " ".join(map(str,Tribonachi(I))))


















