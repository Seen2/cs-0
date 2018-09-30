f=open('newstrip.txt','w+')
f.write('***magic*** hy is r    wt')
print(f.read())

w=f.readline().strip()
print(w)
i=0
while w:
    print(w)

    w=f.readline().strip('*')
    print(i)
    i+=i
f.seek(0)
print(f.read())
