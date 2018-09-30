print('enter a number')
g=1
n=float(input())
c=0.0
while abs(g*g-n)!=0.0 and abs(c-g)!=0.0:
    c=g
    g=(g+n/g)/2;
    print(g)

print('root is {}'.format(g))
