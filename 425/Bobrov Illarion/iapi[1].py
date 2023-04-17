from datetime import datetime
import queue
import matplotlib as mp
import numpy as np

#svoi fio i data rozdenia
my_data=("Bobrov","Illarion","Ivanovich",29,1,2004)

#atestat s osenkami
atestat={"russkii":4,
         "matematika":5,
         "informatica":5,
         "fizica":4,
         "angliiskii":4,
         "fiskultura":5,
         "himia":4,
         "literatura":4,
         "istoria":4,
         "obhestvoznanie":4,
         "geografia":4,
         "biologia":4,
         "obz":5,
         "kultura":5}

#imena rodni i ix god
name_rodstveniki=["ivan 1999","natacha 2000","toma 1977","tana 1966","ivan 1998","irina 2001"]

#ima pitomsa
name_pitomes="lika"

#1 srednia osenka v atestate
srednaia_osenka=sum(atestat.values())/len(atestat.values())
print("#1 srednia osenka v atestate:",srednaia_osenka)

#2 ynikalnie imena rodstvennikov
tolko_imena_rodstvenikov=[""]*len(name_rodstveniki)
for i in range(0,len(name_rodstveniki)):
    perem=name_rodstveniki[i]
    q=0
    ima=""
    while perem[q]!=" ":
        ima+=perem[q]
        q=q+1
    tolko_imena_rodstvenikov[i]=ima
print("#2 ynikalnie imena rodstvennikov:",tolko_imena_rodstvenikov,my_data[1])

#3 obchaia dlinna vsex nazvanii predmetov
name_predmetov_slitno=""
for i in atestat.keys():
    name_predmetov_slitno+=i
print("#3 obchaia dlinna vsex nazvanii predmetov:",len(name_predmetov_slitno))

#4 unikalnie bukvi i nazvaniax predmetov
unikalnie_bukvi=""
for i in range(0,len(name_predmetov_slitno)):
    if name_predmetov_slitno[i] not in unikalnie_bukvi:
        unikalnie_bukvi+=name_predmetov_slitno[i]
print("#4 unikalnie bukvi i nazvaniax predmetov:",unikalnie_bukvi)

#5 ima pitomsa v binarnom kode
name_pitomes_v_binarnomkode = ''.join(format(ord(x), '08b') for x in name_pitomes)
print("#5 ima pitomsa v binarnom kode:",name_pitomes_v_binarnomkode)

#6 po alfavitu s konca imena rodstvennikov
tolko_imena_rodstvenikov.sort(reverse=True)
print("#6 po alfavitu s konca imena rodstvennikov:",tolko_imena_rodstvenikov)

#7 dni ot moego denrozdenia do segodna
print("#7 dni ot moego denrozdenia do segodna:",format((datetime.now() - datetime(day=int(my_data[3]), month=int(my_data[4]), year=int(my_data[5]))).days))

#8 fifo ochered s komandoi ostanovki
slovo=""
fifo=[]
slovo=input("#8\nDla ostanovki vvedite 'q':\n")
while slovo!="q":
    fifo.append(slovo)
    slovo=""
    slovo=input()
print("#8 fifo ochered s komandoi ostanovki:",fifo)

#9 zamena imeni rodstvennika s imenem adsteka
nomer_adsteka = (int(my_data[3]) + int(my_data[4])**2 + int(my_data[5])) % 21 + 1
adsteki= ['Tenoch',
          'Acamapochtli',
          'Huitzilihitl',
          'Chimalpopoca',
          'Xihuitl Temoc',
          'Itzcoatl',
          'Moctezuma I',
          'Atotoztli',
          'Axayacatl',
          'Tizoc',
          'Ahuitzotl',
          'Moctezuma II',
          'Cuitlahuac', 
          'Cuauhtrmoc', 
          'Tlacotzin', 
          'Motelchiuhtzin',
          'Xochiquentzin',
          'Huanitzin',
          'Tehuetzquititzin',
          'Cecetzin',
          'Cipac']
print("#9\nVipalo",nomer_adsteka,"eto",adsteki[nomer_adsteka])
nomer_rodstvennika=int(input("Vvedite № rodstvennika do 6: "))
if nomer_rodstvennika>6 or nomer_rodstvennika<0:
    print("Vi nepravilno vveli nomer")
else:
    tolko_imena_rodstvenikov[nomer_rodstvennika-1]=adsteki[nomer_adsteka]
print("#9 zamena imeni rodstvennika s imenem adsteka:",tolko_imena_rodstvenikov)

#10 svaznii spisok
name_rodstveniki_po_godam=["tana 1966","toma 1977","ivan 1998","ivan 1999","natacha 2000","irina 2001"]
name_rodstveniki_po_godam_s_klyshom={}
for i in range(len(name_rodstveniki_po_godam)):
    if i==len(name_rodstveniki_po_godam)-1:
        name_rodstveniki_po_godam_s_klyshom[name_rodstveniki_po_godam[i]]=0
    else:
        name_rodstveniki_po_godam_s_klyshom[name_rodstveniki_po_godam[i]]=i+1
print(name_rodstveniki_po_godam_s_klyshom)

#11 funksia generator
vipavshii_nomer=(len(my_data)*len(tolko_imena_rodstvenikov)%4)
def alikvodnaia():
    n=12
    while n!=0:
        sum=0
        yield n
        for i in range(1,n):
            if n%i==0:
                sum+=i
        n=sum
        
def silvestr():
    n=2
    yield n
    for i in range(10):
        n=n*n+1
        yield n
        
def tridonashi():
    n,q,w=0,0,1
    yield n
    yield q
    yield w
    for i in range(10):
        e=n+q+w
        yield e
        n=q
        q=w
        w=e 
        
def leonardo():
    n,q=1,1
    yield n
    yield q
    for i in range(10):
        n,q=q,n+q+1
        yield q  
        
if vipavshii_nomer==0:
    ima_funksii="alikvodnaia"
    funcsia=alikvodnaia()
elif vipavshii_nomer==1:
    ima_funksii="silvestr"
    funcsia=silvestr()
elif vipavshii_nomer == 2:
    ima_funksii="tridonashi"
    funcsia=tridonashi()
else:
    ima_funksii="leonardo"
    funcsia=leonardo()
print("#11\nVipal nomer:",vipavshii_nomer,". Eto:",ima_funksii)
for i, chislo in enumerate(funcsia):
    print(chislo)
    if i>=10:
        break