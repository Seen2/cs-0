def fib(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return fib(x-2)+fib(x-1)



n=int(input('enter number of terms:'))
for i in range(n):
    print(fib(i))
