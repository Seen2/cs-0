def descending(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return False
    return True

def valley(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            flag+=1







'''
def descending(l):
    s=len(l)
    if s==0 :
        return l

    for i in range(s):
        if(i<s-1):
            t=l[i]
            l[i]=large(l[i+1:])
            l[i+1]=t
    return l


print(descending([4,4,3]))
       

def large(l):
    large=l[0]
    for i in range(len(l)):
        if large<l[i]:
            large=l[i]

    return large
'''
