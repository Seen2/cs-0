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
            y=n
        if '('==s[n] and y>n:
            print(s)
            s.replace(s[y],'')
            s.replace(s[n],'')
            print(s)
        n=n-1
    return (r==0)



