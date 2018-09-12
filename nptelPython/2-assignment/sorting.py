def descending(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return False
    return True

def valley(l):
    if(len(l)==1):
        return False
    for i in range(len(l)-1):
        if(l[i]==l[i+1]):
            return False
        if l[i]<l[i+1]:
            for j in range(i,len(l)-1):
                if(l[j]==l[j+1]):
                    return False
                if l[j]>l[j+1]:
                    return False
            break
        elif i==len(l)-2:
            return False
    return True


def transpose(m):
    r=len(m)
    c=len(m[0])
    t=[[0 for x in range(r)] for y in range(c)]

    for i in range(r):
        for j in range(c):
            t[j][i]=m[i][j]


    return t
