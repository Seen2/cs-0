def f(x,n,e):
    return x**e-n
def g(x,n,e):
    return e*x**(e-1)

n=float(input('enter number to find root:'))
e=float(input('rooth exponent :'))

p=float(input('enter a point near if you will:'))
pr=None
i=0
while g(p,n,e)!=0 and abs(f(p,n,e))>=0.001 and p!=pr:
    pr=p
    p=p-f(p,n,e)/g(p,n,e)
    i =i+1
    print('i=',i,'p={}'.format(p))


print('root={}'.format(p))
