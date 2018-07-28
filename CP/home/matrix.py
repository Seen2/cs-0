m=int(input('enter number of rows:'))
n=int(input('enter number of columns:'))
l=[]
r=[]
print('enter matrix elements:')
for i in range(m):
    for j in range(n):
        e=float(input())
        r.append(e)

    l.append(r)
    del(r)
    r=[]


print('here is matrix:')

for i in l:
    for j in i:
    
        print(j,end='\t')

    print('')

o=int(input('enter no. of  rows of second matrix:'))

p=int(input('enter no.  of column of second matrix:'))

k=[]
r=[]
print('enter second matrix:')
for i in range(o):
    for j in range(p):
        e=float(input())
        r.append(e)
    

    k.append(r)
    del(r)
    r=[]

print('here is second matrix:')
for i in k:
    for j in i:
        print(j,end='\t')


    




if m!=o or n!=p:
    print('\naddition for this order is not possible..')
    exit(0)


print('resultent matrix')


for i in range(m):
    for j in range(n):
        print(l[i][j]+k[i][j],end='\t')

    print('')

print('end')

print('multiplication...')



for i in range(m)
