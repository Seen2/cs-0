t=((1,'we'),(2,'are'),(3,'human'),(4,'beings'),(5,'we'))
i=()
s=()

for w in t:
    i=i+(w[0],)
    if w[1] not in s:
        s=s+(w[1],)
print(t)
print(i)
print(s)


# we can use touples for swaping

l=9 
p=4
print('L={},P={}'.format(l,p))
(l,p)=(p,l)

print('L={},P={}'.format(l,p))


# we can use for returning more values from single return statement

def f():
    a=(1,2,3)
    return a
b=()

b=f()
print(b)

#like string touples are also immutable means you can not change value as whole for specific index..remember list are muttable
