print('enter number of item in list')
n=int(input())
print('enter items')
l=[]
for i in range(n):
    item=input()
    l.append(item)
print('here vertical')
for w in l:
    print(w)

print('here whole')

print(l)
print('lets play with integer')
print('crete list of intiger no. of item is:')
n=int(input())
li=[]
print('enter item')

for i in range(n):
    item=int(input())
    li.append(item)

s=0

for n in li:
    print(n)
    s=s+n;

print(s)
print(li)
