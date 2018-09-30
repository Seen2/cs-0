

#Covert to binary

num=abs(float(input('enter the number:')))
inum=int(num)
fnum=num-inum
iN=[]
print('\v')
fnum=fnum*2
if inum==0:
    print(0,end='')
while inum!=0:

    
    iN.append(inum%2)
    inum=inum//2


fN=[]
while fnum!=0.0:
    f=int(fnum)

    fN.append(f)     #taking obtained whole no.
    fnum=fnum-f
    fnum=fnum*2      #multiplying it by 2 and shifting it ith power back doesn't effect the number


    #round(fnum,5)

#print(iN)
#print(fN)

for j in range(1,len(iN)+1):
    print(iN[-j],end='')

print('.',end='')

for k in range(len(fN)):
    print(fN[k],end='')

print('')
