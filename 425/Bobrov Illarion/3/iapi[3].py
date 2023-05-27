from collections import deque
import numpy as np
import codecs


fil=codecs.open('maze-for-u.txt', "r", "utf_8_sig")    
labir=fil.readlines()
lab=[]
for i in range(len(labir)):
    line=[]
    for j in range(len(labir[i])-2):
        iacheika=labir[i][j]
        line+=iacheika
    lab.append(line)
lab=np.array(lab)

print(lab.shape,len(lab[0]),len(lab[1]))

print(lab[0][0])
graf={}
for i in range(lab.shape[0]):
    for j in range(lab.shape[1]):
        if lab[i][j]!='#':
            q=[]
            if j+1<lab.shape[1] and lab[i][j+1]!='#':
                q.append((i,j+1))
            if j>0 and lab[i][j-1]!='#':
                q.append((i,j-1))
                
            if i+1<lab.shape[0] and lab[i+1][j]!='#':
                q.append((i+1,j))
            if i>0 and lab[i-1][j]!='#':
                q.append((i-1,j))
            graf[(i,j)]=q
           
print(graf[0,1])
print(len(graf))

import random
avatar=(0,0)
klych=(0,0)
while lab[klych]=='#':
    klych=(random.randint(0, len(lab)-1),random.randint(0, len(lab[0])-2))
while lab[avatar]=='#':
    avatar=(random.randint(0, len(lab)-1),random.randint(0, len(lab[0])-2))
    
print(avatar,klych,lab[klych],lab[avatar])
        
def doroga(avatar,klych,graf):
    que=deque([avatar])
    bili=set([avatar])
    last={avatar:None}

    while que:
        a=que.popleft()
        
        if a==klych:
            print("Klysh")
            break
        
        for nex in graf[a]:
            if nex not in bili:
                que.append(nex)
                bili.add(nex)
                last[nex]=a
                
                
    if klych not in last:
        return None,None
    

    put=[]
    yzel=klych
    while yzel is not None:
        put.append(yzel)
        yzel=last[yzel]
    put.reverse()

    return put
       
put=doroga(avatar,klych,graf)
print("Ot avatara do klycha:",put[1:])


from queue import PriorityQueue
vix=(599, 798)
gran=PriorityQueue()
gran.put(klych,0)
last={}
baks={}
baks[klych]=0
last[klych]=None
while not gran.empty():
    a=gran.get()
    if a==vix:
        break
    for nex in graf[a]:
        sena=baks[a]
        if 0<=nex[0]<lab.shape[0] and 0<=nex[1]<lab.shape[1] and lab[nex[0]][nex[1]]!='#' and((nex not in baks) or sena<baks[nex]):
            baks[nex]=sena
            baks[a]=sena
            march=sena+abs(vix[0]-nex[0])+abs(vix[1]-nex[1])
            gran.put(nex,march)
            last[nex]=a
put2=[]
yzel=klych
while yzel is not None:
    put2.append(yzel)
    yzel=last[yzel]
put2.reverse()
print(put2)

otvet=[]

for i in range(lab.shape[0]):
    line = []
    for j in range(lab.shape[1]):
        simv = lab[i, j]
        q = (i, j)
        if q == (klych):
            simv = '*'
        elif q in put:
            simv = '.'
        elif q in put2:
            simv = ','
        line.append(simv)
    otvet.append(line)
    
with open('maze-for-me-done.txt', "w") as f:
    for lines in otvet:
        kartink = ""
        for nom in lines:
            kartink += nom
        f.write(kartink + '\n')