def genTest():
    yield 1        #any thing with yield is genrator
    yield 2
    yield 3

foo=genTest()


for i in range(3):
    print(foo.__next__())
    print(type(foo))


#let me show application of gernator


def genFib(fib_1,fib_2,n):
    for i in range(n):
        next=fib_1+fib_2

        print(next)

        yield next


        fib_1=fib_2
        fib_2=next


n=int(input('enter no. of terms'))

genFib(0,1,n)
