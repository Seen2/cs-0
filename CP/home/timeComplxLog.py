def setIntToStr(i):
    digits='0123456789'
    if i<=0:
        return '0'
    res=''
    while i>0:
        res=res+digits[i%10]
        i=i//10

    return res

n=int(input('enter an integer:'))
print(setIntToStr(n))
