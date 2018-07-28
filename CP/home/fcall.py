x=4
def f():
    x=8  #we have to assign variavle to operate it as local var.
         #it means that you cant change global variable as local if you have to change you have to assign it locally
    x=x+1
    print('f,x=',x)
    

def g(a):
    print('g,x=',x)
    return a
print(f())
print(g(f()))
print(x)
