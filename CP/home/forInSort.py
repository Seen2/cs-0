l=[]
print('enter number of items')
n=int(input())
print('enter items')
for i in range(n):
    item=input()
    l.append(item)

print(l)
ll=""
s=''
for w in l:
    if len(w)<10:
        s=s+'\t'+w
    elif len(w)>10:
        ll=ll+'\t'+w
    else:
        pass
print(l)
print(ll)
print(s)


print('lets count our instance in list\n enter letter')
o=(input())
t=0
for w in l:
    c= w.lower().count(o)
    t=t+c

print('total=',t)


def search(s,l=['Nidhi','Pragya','Kajal','Shreyashi','Shweta','Sibi']):
    for w in l:
        if s.lower()==w.lower():
            return True

    return False
print('whom you love')
lo=input()
print('you are shintu',search(lo))
