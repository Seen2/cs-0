def sumprimes(l):
    sum=0
    for i in range(len(l)):
        if checkPrime(l[i]):
            sum += l[i]

    return sum

def checkPrime(n):
    flag=0
    for i in range(1,n+1):
        if n%i==0:
            flag +=1

    if flag==2:
        return True
    return False


print(sumprimes([3,3,1,13]))
'''def sumprimes(l):
    large=l[0]
    for i in range(len(l)):
        if large<l[i]:
            large=l[i]
    for i in range(large):
        if 
    '''
