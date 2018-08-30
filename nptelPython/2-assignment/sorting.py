def descending(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return False
    return True

def valley(l):
    for i in range(len(l)-1):
        #print("in 1st ")
        if l[i]<l[i+1] and i==len(l)//2:
            for j in range(i,len(l)-1):
                #print("in 2nd ")
                if l[j]>l[j+1] :
                    return False
            break
        elif i==len(l)-2:
            return False
    return True


def transpose(m):
    r=len(m)
    c=len(m[0]) 
    t=[[0]*(r-1)]*(c-1)
    print('r={},c={}'.format(r,c))
    for i in range(r):
        for j in range(c):
            print(i,j)
            t[j].append(m[i][j])
    return t


print(transpose([[1,4,9]]))




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
