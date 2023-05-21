import datetime as dt
import queue
import random

def QuickSort_rev(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] > q:
                i += 1
            while A[j] < q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                QuickSort_rev(A, l, j)
                QuickSort_rev(A, i, r)
          


data = ("Voronin Michael Mikhailovich", 28 , 2, 2003) 
certificate = {
                "russian_language":4,
                "literature":5,
                "english_language":5,
                "algebra":4,
                "geometry":4,
                "informatics":5,
                "physics":5,
                "BPE":5,
                "biology":5,
                "chemistry":5,
                "ru_history":5,
                "general_history":5,
                "social_science":5,
                "geography":5,
                "fis_culture":5
                }
family_names = ["Oliver","Jack","Thomas","Jacob","Charley","Thomas","George","Jack","Jacob","Jack"]
kiwa_name = "crab(#12)"

#mean mark
print(" mean mark -> ")
sum_m=sum(certificate.values())
len_m=len(certificate)
avg_m=sum_m/len_m
print("mean mark = ",avg_m)

#unique names

print(" unique names -> ")

unique_names = list(set(family_names))
print("unique names:",unique_names)

#whole length of subjects

print(" whole length of subjects -> ")

len_whole = 0
for key in certificate:
    len_whole += len(key)
print("length of keys in certificate = ",len_whole, "letters")

#unique letters

print(" unique letters -> ")

a = set()
for key in certificate:
    a= a|set(key)
print("unique letters in subjects:",a)

#kiwa name in 1-0 language

print(" kiwa name in 1-0 language -> ")

kiwa_name_bin =  ' '.join(format(ch, 'b') for ch in bytearray(kiwa_name, "utf-8"))
print("kiwa_name_bin: ",kiwa_name_bin)
    
#sort

print(" quicksort -> ")

QuickSort_rev(family_names, 0, len(family_names)-1)
print(family_names)
    
#time

print(" time-> ")

time_now = dt.datetime.today()
time_birth = dt.datetime(day=data[1], month=data[2], year=data[3])
print("days: ",(time_now-time_birth).days)
   
# FIFO

print(" FIFO -> ")

print("end of input : '-1'")
things = queue.Queue(101)
i = int(input())
while i!=-1:
    things.put(i)
    i = int(input())
print("u entered",end=':')
while not things.empty():
    print(things.get(), end=',')
print()

#rulers_of_Tenochtitlan

print(" rulers_of_Tenochtitlan -> ")

number = (data[1] + data[2]**2 + data[3]) % 21 + 1
name = "Luis de Santa María Cipac"
print("enter index to replace")
i = int(input())
if(i>len(family_names)):
    while(i>len(family_names)):
        i-=len(family_names)
family_names[i]=name
print(family_names)

#связный список

print("spisok -> ")
data_enum ={
    "Oliver": 1980,
   "Jack": 1975,
   "Thomas": 1990,
   "Jacob": 1985,
   "Charley":1234,
   "George":4564
    }
sorted_data = sorted(data_enum.items(), key=lambda x: x[1])

linked_list = {}

for i, item in enumerate(sorted_data):
    name = item[0]
    if i < len(sorted_data) - 1:
        next_index = i + 1
        next_name = sorted_data[next_index][0]
        linked_list[name] = next_name
    else:
        linked_list[name] = None

# выводим на экран связный список
for k, v in linked_list.items():
    print(k, "-->", v)

#func - gen

number = len("Voronin Michael Mikhalovich") * len (family_names) % 4
print("variant = ",number)
#2 - tribonachi

print("tribonachi-`")

print("enter upper limit = ")
upper_lim = int(input())

print("0 -> 0")
print("1 -> 0")
print("2 -> 1")

def tribon(xp1,xp2,xp3,k):
    xc = xp1+xp2+xp3
    
    if(xc>upper_lim):
        return xc
    else:
        print(k," -> ",xc)
        k+=1
        return tribon(xc,xp1,xp2,k)

k=3
a = tribon(1,0,0,k)


# the end 

