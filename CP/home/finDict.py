

def efffib(n,d):
    global i

    i +=1
    if n in d.keys():
        return d[n]
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        d[n]=efffib(n-1,d)+efffib(n-2,d)
        return efffib(n-1,d)+efffib(n-2,d)

def fib(n):
    global i
    i+=1
    if n==1:
        return 0
    if n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)

n=int(input('enter term no.:'))
d={}
i=0

print('efffib(n)=',efffib(n,d))
print('efffib calls={}'.format(i))
i=0

print('fib(n)=',end='')
print(fib(n))

print('fib calls=',i)

d={}
i=0

print('efffib(n)=',efffib(n,d))
print('efffib calls={}'.format(i))



