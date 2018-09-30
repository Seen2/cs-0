s=input('enter something:')
print('as python treat big string as sequence  of characters')
for w in s:
    #print(w,end='')
    for c in w:
        print(c)

print('\v')
for w in s:
    print(w,end='\t')




for w in s[::-1]:
    print(w)
