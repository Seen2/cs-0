s=input('enter something:')
print('how i slice its part let me show you')
for i in range(len(s)):
    print(s[i:len(s)]) #string slice=string[start index:end index]

for i in range(len(s)):
    print(s[:i])    # substring default initial interval of zero





print('\n\v')
for i in range(len(s)):
    print(s[i:])


print('\v')
print('step slice')
for i in range(len(s)):
    print(s[i:len(s):i+1]) #string[start:end:steplength]



print('\v')
print('step slice')


for i in range(len(s)):
    print(s[::-1]) #string[start:end:-steplength] reverse





s='standard'
print(s[::-1])


print('-ive index print')
for i in range(len(s)):
    print(s[-len(s)+i])

