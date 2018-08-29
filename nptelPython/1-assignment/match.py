def match(s):
    l=len(s)-1
    while l>0:
        if s[l]==')':
            print(l)
            for i in range(0,l):
                if s[i]=='(':
                    print(i)
                    print('s inside of for:'+str(s))
                    s=s.replace(s[i],'')
                    print('s inside of for:'+str(s))
                    s=s.replace(s[l],'')
                    print('s inside of for:'+str(s))
                    break
            print('s out of for:'+str(s))

        l=l-1
    return s

