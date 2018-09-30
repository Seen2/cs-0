l=[]
print('enter num. of item to make list')
n=int(input())
print('enter items')

for i in range(n):
    item=input()
    l.append(item)
print(l)
print('enter pos to delete')
i=int(input())
del l[i]
print(l)
print('time to pop out')
print('enter pos')
i=int(input())
print(l.pop(i))
print(l)
print('time to pop out')
print('enter pos')
i=int(input())
print(l.pop(i))
print(l)
print('time to remove')
i=input()
if i in l:
    l.remove(i)
else:
    print('check the list..')


print(l)
