def match(s):
    l=len(s)-1
    while l>0:
        if s[l]==')':
            print(l)
            for i in range(0,l):
                if s[i]=='(':
                    print(i)
                    s=s[:i-1]+s[i:]
                    print(s)
                    s=s[:l-1]+s[l:]
                    break
            print('s out of for:'+str(s))

        l=l-1
    return s
print(match('(7)a('))

