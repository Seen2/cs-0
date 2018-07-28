s=['king','emperror','empire','kingdom']
print(type(s))
print(s)
i=[1,0,0,1]
print(type(i))
print(i)

m=[1,'you','shintu',s,i]
print(type(m))
print(m)


for i in range(len(s)):
    print(s[i])

print(s[::-1])
print(s[:len(s)+1:-1])

#list are muttable...again if you will..


#now some delete operations within list..


# del(list[index])  remove specific element..
# pop(list) remove element from end..
# remove(value) remove first occurence of specific value within list

l=[1,2,3,4,5]
print(l)

del(l[2])
print(l)

l.remove(5)
print(l)

l.pop()
print(l)

# here are some more list operations
s='hello'
print(s)
print(s.split()) 


#convert string to list over specific cherector  string_name.split('chr')

print(list(s)) #cover string to list
print('_'.join(list(s))) # join list specific chr 'chr'.join(list)



#here are some sorting and reversing

l=[2,9,0,1,7,4]

l.sort()  #mutate the list
print(l)

l.reverse()
print(l)

l=[2,9,0,1,7,4]
print(sorted(l)) # doesn't mutate list rather gives new version 





