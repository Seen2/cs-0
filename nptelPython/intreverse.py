def intreverse(n):
    r=0
    i=len(str(n))-1
    while(n>0):
        r=r+(n%10)*10**i
        n=n//10
        i=i-1
    return r

def matched(s):
    n=len(s)-1
    r=0
    y=0
    while(n>=0):

        if ')'==s[n]:
            r=r+1
            y=n
            print('case1:s[n]='+str(s[n])+str(n))

        if '('==s[n] and y>n:
            r=r-1
            print('case2:'+str(n)+','+str(y))

        n=n-1
    return (r==0)



