l1=input('enter the list of integer seprated by comma:')

l1=l1.split(',')
print(l1)
l2=input('enter the list of same length as before with differ values:')
l2=l2.split(',')

print(l2)

l3=[]



for i in range(len(l1)):
    try:
        assert not len(l1)==0
        assert not len(l2)==0
        l3.append(int(l1[i])/int(l2[i]))
    except ZeroDivisionError:
        l3.append('Nan')
    
    except:
        raise('check the length of both list')


print('out of the loop')
print(l3)
