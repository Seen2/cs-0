i=input('Enter the list seprated by comma:')

l=i.split(',')


for i in range(len(l)):
    
    for j in range(len(l)):
        print(l)
        if int(l[j])>int(l[i]):
            (l[i],l[j])=(l[j],l[i])
            

    



print(l)
