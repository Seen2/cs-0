import fibRec
def applyNew(L,k,f):
    map(f,L,k)
    print(L)
    print(k)



def apply(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])


L=[3,-9,6,-7.8,9.7]
k=[3,-9,6,-7.8,7,-9,6,-7,9.7]
apply(L,abs)
print(L)
apply(L,int)
print(L)
apply(L,fibRec.fib)
print(L)
applyNew(L,k,abs)
applyNew(L,k,int)
applyNew(L,k,fibRec.fib)
#inverse


def applyfn(f,i):
    for j in range(len(f)):
        i=f[j](i)
        print(i)

i=-9.356800
print(i)
f=[abs,int,fibRec.fib]
applyfn(f,i)
print('done')



#map() function apply argument function to the all other list within as argument
