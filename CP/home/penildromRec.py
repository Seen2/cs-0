def pen(s,a,b):
    if a==b:
        return True
    if s[a]==s[b]:
        return pen(s,a+1,b-1)

    else:
        return False




s=input('enter:')

if s=='':
    print('it is penildrom if you will...')
    exit(0)
print('you check it as case sensative press y else press n')
opt=input()
if opt =='N' or opt=='n':
    s=s.lower()

else: 
    pass

if pen(s,0,len(s)-1)==True:
    print('String is penildrom ')

else:
    print('string  is not penildrom')

