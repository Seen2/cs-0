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
    t=[[0 for x in range(r)] for y in range(c)]
    print('r={},c={}'.format(r,c))
    for i in range(r):
        for j in range(c):
            t[j][i]=m[i][j]
            print(t)
        print(t)
    return t


print(transpose([[1,4,9]]))

