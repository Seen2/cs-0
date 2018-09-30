liist=[]
n=int(input('enter number of item to add:'))
print('enter item to add')
for i in range(n):
    item=input()
    liist.append(item)

print(liist)


print('you need to add more item press y else press other key')
i=input()
if i=='y':
    print('how many number of item to add')
    m=int(input())
    print('enter items')
    for k in range(n,n+m):
        item=input()
        liist.append(item)

    print('here is updated ones\n',liist)


else:
    pass
print('you want to oberide the list\n enter y to override\n other to exit')
i=input()
if i=='y':
    print('\n enter item no.')
    k=int(input())
    if k>len(liist):exit(0)
    print('enter to over ride')
    ov=input()
    liist[k-1]=liist[k-1]+ov
print(liist)

print("\you want to insert item in list press y")
i=input()
if i=='y':
    print('enter position')
    i=int(input())
    print('what to insert')
    ins=input()
    liist.insert(i,ins)

print('updated list',liist)
