def large(l):
    large=l[0]
    for i in range(len(l)):
        if large<l[i]:
            large=l[i]

    return large

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
       


