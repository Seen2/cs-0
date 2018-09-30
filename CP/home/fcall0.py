def g(x):
    print('g')
    print('x=',x)
    def h():
        x='abc'
        print('h')
        print(x)

    x=x+1
    print('g after h')

    print('x=',x)
    h()
    return x
x=1
i=g(x)
print('global returned value=',i)
print(x)





# xpln version of fcall.py[file]
