import time

def t():
    return 100

t0=time.clock()
t()
t1=time.clock()

print(t1-t0)
