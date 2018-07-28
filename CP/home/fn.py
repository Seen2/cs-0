def f(x):
    x +=1
    global y
    y=5
    print('in f(x),y=5,y=',y)
    print('in f(x) x=4 2nd 10 ,x=',x)
    return x


x=3
print('x=3,x=',x)
x=f(x)
print('after call x=4,x=',x,'y=5,y=',y)

x=9
print('x=9,x=',x)
z=f(x)
print('z=10,z={}.x=9,x={}'.format(z,x))

