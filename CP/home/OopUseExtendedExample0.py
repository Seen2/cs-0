from ExtendedExample0V1 import *

Shintu=person('Shintu Tiwari',1998,3,9)


mark=gurus('Mark Zuckerberg',1985,2,2)
bill=gurus('Bill gates',1956,10,2)


print(Shintu)


print(bill)
print(mark)


p1=Shintu
p2=mark
p3=bill

l=[p1,p2,p3]

nl=sorted(l)
print(p2<p1)
for g in nl:
    print(g)

M=UGgurus('Mark Zuckerberg',1985,2,2,3,'owmer of facebook')
B=UGgurus('Bill gates',1956,10,2,4,'Owner of Microsoft')

print(M)
print(B)
