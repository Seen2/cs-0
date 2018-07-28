n=input('enter file name:')
f=open(n,'r')
c=int(input('enter number of text to read:'))
print(f.read(c))
i=1
#read() step next with c
#while f.read(i)!=None:
 #   print(f.read(i))

#as read method return Strimg so you can use all string method
print(f.read(c).upper())

#readlines()
print('\v')
print(f.readlines())

print('\v')
print(f.read().upper())
print('\v')
#strip() eliminate space chrctrs frm file
#pass argumenr will delete that char from file while reading
print(f.read().strip())
print('\v')
u=f.readline()
print(u)
while u:
    print(f.readline())
    u=f.readline()

f.close()
