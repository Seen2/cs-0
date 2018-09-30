s=input('enter something:')

print('length=',len(s))

print('\nenter what you want to search index for in prev. string')
i=input()

print('search =',s.find(i))
print('enter word you want to count in first string')
c=input()
print('here',s.count(c))
print('\n enter the word or charecter to find all location')
a=input()
l=s.find(a)
i=0
while i<len(s):
    print(l)
    l=s.find(a,l+1)
    i=i+1


#string.find(searchstr,startindex,endindex)
